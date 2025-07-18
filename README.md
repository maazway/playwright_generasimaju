# 🧪 Playwright Automation untuk GenMaju

Proyek ini digunakan untuk **otomatisasi testing** website [www.generasimaju.co.id](https://www.generasimaju.co.id) dengan **Python + Playwright + Pytest**.  
Tes bisa dijalankan manual atau otomatis (jadwal via GitHub Actions), dan hasilnya langsung dikirim ke email dalam bentuk **HTML report**.

---

## 🚀 Fitur

- Test otomatis dengan **Playwright (Python)**
- Struktur rapi pakai **Page Object Model**
- HTML report dari `pytest-html`
- Kirim hasil ke beberapa email secara otomatis
- Bisa dijalankan manual atau otomatis (jam 05.00 & 17.00 WIB) dengan Github Action

---

## 🧱 Struktur Folder

```bash
playwright_generasimaju/
│
├── pages/                  # Page Object (halaman web yang akan diotomasi)
│   ├── homePage.py
│   └── loginPage.py
│
├── tests/                  # Kumpulan test case
│   ├── login/
│   │   └── test_login_valid.py
│   └── home/
│       └── test_click_artikel.py
│
├── utils/                  # Fungsi tambahan (seperti kirim email)
│   └── email_report.py
│
├── conftest.py             # Setup browser otomatis (Playwright fixture)
├── run_tests.py            # File utama untuk menjalankan dan mengirim hasil tes
├── .env                    # Menyimpan kredensial seperti email & nomor HP
└── .gitignore              # File/folder yang tidak di-push ke Git
```

---

## ⚙️ Cara Menggunakan

### 1. Clone repo dan masuk ke folder proyek

```bash
git clone https://github.com/maazway/playwright_generasimaju.git
cd playwright_generasimaju
```

### 2. Buat virtual environment dan aktifkan
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# atau
source venv/bin/activate  # Mac/Linux
```

### 3. Install semua dependencies
```bash
pip install -r requirements.txt
playwright install
```

### 4.  Siapkan file .env
```bash

```

### 5. Jalankan semua test
```bash
python run_tests.py
```

### 6. Jalankan test tertentu (misal test login saja)
```bash
python run_tests.py tests/login/test_login_valid.py
```
