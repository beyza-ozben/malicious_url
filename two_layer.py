import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras import layers

# Veriyi oku ve işleme al
with open('banking_phishing.txt', 'r') as file:
    lines = file.readlines()

# URL ve etiketleri ayırın (örneğin, her satırda 'url,phishing' formatı varsa)
urls = []
labels = []

for line in lines:
    url, label = line.strip().split(',')  # ',' ile ayrıldığını varsayıyoruz
    urls.append(url)
    labels.append(1 if label == 'phishing' else 0)  # 'phishing' etiketi 1, diğerleri 0 olacak

# Veriyi DataFrame'e dönüştür
data = pd.DataFrame({
    'url': urls,
    'label': labels
})

# Özellikler ve etiketleri ayırın
X = data['url']  # URL sütunu, burada özellik olarak ele alınıyor
y = data['label']

# URL'leri vektörize edin veya işlenebilir bir forma sokun
# Örnek: Basit bir metin vektörleştirme (TF-IDF gibi bir yöntem)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)

# Veriyi eğitim ve test setlerine ayırın
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=64)

# Veriyi ölçeklendirin
scaler = StandardScaler(with_mean=False)  # with_mean=False çünkü sparse matris ile çalışıyoruz
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Modeli oluşturun
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Çıktı katmanı
])

# Modeli derleyin
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğitin
model.fit(X_train, y_train, epochs=100, batch_size=64, validation_split=0.2)

# Modelin performansını değerlendirin
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test kaybı: {loss}, Test doğruluğu: {accuracy}')
