# 🛡️ Malicious URL Detection & REST API

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow / Keras](https://img.shields.io/badge/TensorFlow-Keras-orange.svg?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-API-lightgrey.svg?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Zararlı, oltalama (phishing) ve şüpheli bağlantıları tespit etmek amacıyla geliştirilmiş Makine Öğrenmesi / Derin Öğrenme tabanlı **Zararlı URL Tespit Sistemi**. Bu proje; veri ön işleme, model eğitimi, model test adımları ve eğitilen modelin gerçek zamanlı olarak sorgulanabileceği bir **Flask RESTful API** servisinden oluşur.

---

## 📌 İçindekiler

- [Genel Bakış](#-genel-bakış)
- [Özellikler](#-özellikler)
- [Proje Mimarisi & Dosya Yapısı](#-proje-mimarisi--dosya-yapısı)
- [Kurulum](#-kurulum)
- [Kullanım Adımları](#-kullanım-adımları)
  - [1. Veri Hazırlama & Ön İşleme](#1-veri-hazırlama--ön-işleme)
  - [2. Model Eğitimi](#2-model-eğitimi)
  - [3. Model Testi](#3-model-testi)
  - [4. REST API Sunucusunu Başlatma](#4-rest-api-sunucusunu-başlatma)
- [API Uç Noktaları](#-api-uç-noktaları)
- [Kullanılan Teknolojiler](#-kullanılan-teknolojiler)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

---

## 📖 Genel Bakış

Siber güvenlikte kullanıcıları tehdit eden en yaygın vektörlerden biri kötü amaçlı bağlantılardır. Bu proje:
- Güvenli ve zararlı URL'leri etiketlenmiş veri setleri (`mix_labels.csv`) üzerinden analiz eder.
- Metin işleme / öznitelik çıkarımı yöntemlerini kullanarak Keras/TensorFlow tabanlı bir sınıflandırma modeli (`new_model.keras`) eğitir.
- Eğitilen modeli harici uygulamalara, tarayıcı eklentilerine veya güvenlik duvarlarına entegre edilebilmesi için hafif bir **Flask REST API** üzerinden servis eder.

---

## ✨ Özellikler

- **Veri Manipülasyonu & Analiz:** `pandas` ile veri setini temizleme, sınıfları dengeleme ve etiketleme.
- **Derin Öğrenme / ML Modeli:** Yüksek doğrulukla zararlı ve güvenli URL'leri ayırt edebilen Keras tabanlı derin öğrenme mimarisi.
- **RESTful Entegrasyon:** Gerçek zamanlı URL denetimi sağlayan Flask API.
- **Test ve Doğrulama:** Test komut dosyası ile model başarımını ve örnek URL tahminlerini hızla değerlendirebilme imkânı.

---

## 📂 Proje Mimarisi & Dosya Yapısı

```text
malicious_url/
├── mix_labels.csv        # Etiketlenmiş eğitim ve test veri seti (URL & Label)
├── pandas_framework.py   # Veri analizi, temizleme ve veri çerçevesi işlemleri
├── label.py              # URL etiketleme ve veri dönüşüm fonksiyonları
├── machine_learning.py   # Model mimarisi tanımlama, derleme ve eğitim (Training)
├── new_model.keras       # Eğitilmiş ve serileştirilmiş Keras modeli
├── test_model.py         # Eğitilen modelin metrik ve örnek URL testleri
├── f_restapi.py          # Tahmin isteklerini karşılayan Flask REST API servisi
└── README.md             # Proje dokümantasyonu
```

---

## 🚀 Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin:

### 1. Depoyu Klonlayın
```bash
git clone [https://github.com/beyza-ozben/malicious_url.git](https://github.com/beyza-ozben/malicious_url.git)
cd malicious_url
```

### 2. Sanal Ortam Oluşturun ve Aktif Edin (Önerilen)
```bash
# Sanal ortam oluşturma
python3 -m venv venv

# Linux / macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install --upgrade pip
pip install tensorflow keras pandas flask scikit-learn numpy
```

---

## 🛠️ Kullanım Adımları

### 1. Veri Hazırlama & Ön İşleme
Veri setini (`mix_labels.csv`) incelemek, temizlemek ve model için hazır hale getirmek için:
```bash
python pandas_framework.py
```

### 2. Model Eğitimi
Yeni bir model eğitmek ve ağırlıkları `new_model.keras` olarak kaydetmek için:
```bash
python machine_learning.py
```

### 3. Model Testi
Eğitilen modelin doğruluğunu test etmek ve örnek linkler üzerindeki performansını görmek için:
```bash
python test_model.py
```

### 4. REST API Sunucusunu Başlatma
Modeli HTTP üzerinden tahmin yapabilir hale getiren Flask sunucusunu ayağa kaldırmak için:
```bash
python f_restapi.py
```
Sunucu varsayılan olarak `http://127.0.0.1:5000` adresinde çalışacaktır.

---

## 🔌 API Uç Noktaları

### URL Güvenlik Kontrolü

- **URL:** `/predict`
- **Metot:** `POST`
- **Headers:** `Content-Type: application/json`

#### Örnek İstek (Request)
```bash
curl -X POST [http://127.0.0.1:5000/predict](http://127.0.0.1:5000/predict) \
     -H "Content-Type: application/json" \
     -d '{"url": "[http://suspicious-banking-login.com](http://suspicious-banking-login.com)"}'
```

#### Örnek Yanıt (Response)
```json
{
  "url": "[http://suspicious-banking-login.com](http://suspicious-banking-login.com)",
  "prediction": "Malicious",
  "confidence": 0.962
}
```

---

## 💻 Kullanılan Teknolojiler

- **Programlama Dili:** Python 3.x
- **Derin Öğrenme / Makine Öğrenmesi:** TensorFlow, Keras, Scikit-learn
- **Veri Analizi:** Pandas, NumPy
- **API Servisi:** Flask

---

## 🤝 Katkıda Bulunma

Katkı sağlamak isterseniz:
1. Depoyu fork'layın (`Fork` butonu).
2. Yeni bir özellik dalı oluşturun (`git checkout -b feature/YeniOzellik`).
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni bir özellik eklendi'`).
4. Dalınızı uzak depoya gönderin (`git push origin feature/YeniOzellik`).
5. Bir **Pull Request** açın.

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında lisanslanmıştır. Detaylar için lisans dosyasına göz atabilirsiniz.
