# 🎓 Student Grade Prediction API

API ini dibuat menggunakan **FastAPI** untuk memprediksi **nilai akhir (G3)** seorang siswa berdasarkan data input seperti nilai sebelumnya, absensi, dan faktor akademik lainnya. Model machine learning dilatih menggunakan dataset akademik dan disimpan dalam format `.pkl`.

---

## 🚀 Fitur

- Endpoint untuk prediksi nilai akhir siswa (`/predict`)
- Preprocessing otomatis (scaling, encoding, dll)
- Validasi input menggunakan Pydantic
- Visualisasi data terpisah via dashboard (contoh: Looker Studio)

---

## 📁 Struktur Project

## ⚙️ Cara Menjalankan

### 1. Clone Repositori

```bash
git clone https://github.com/Daivageralda/titanic-fastapi.git
cd titanic-fastapi
```

### 2. Buat Virtual Environment

```bash
python -m venv .env
source .env/bin/activate  # Command Prompt: .env\Scripts\activate
```

### 3. Install Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan API

```bash
fastapi dev
```

### 5. Akses Swagger UI

Buka browser ke:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🧪 Contoh JSON Input

```json
{
  "Name": "John Doe",
  "Pclass": 2,
  "Sex": "male",
  "Age": 30,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 13.5,
  "Embarked": "S"
}
```

## ✅ Contoh Output

```json
{
  "name": "John Doe",
  "prediction": 1,
  "result": "Survived"
}
```
