# 🧪 Playwright Automation: GenerasiMaju.co.id

Ini adalah proyek **automated testing** berbasis **Python + Playwright + Pytest** untuk website [www.generasimaju.co.id](https://www.generasimaju.co.id/). Setiap hasil tes akan dikirim otomatis melalui email lengkap dengan HTML report.

---

## 🚀 Fitur

- ✅ Test otomatis dengan **Playwright** (Python)
- ✅ Struktur modular dengan **Page Object Model**
- ✅ Support banyak test case di folder `tests/`
- ✅ **HTML report** dari `pytest-html`
- ✅ **Email notifikasi** hasil test ke beberapa penerima
- ✅ Support test **manual maupun GitHub Actions (CI)**

---

## 🗂️ Struktur Folder

playwright_generasimaju/
├── pages/ # Page Object untuk setiap halaman
│ └── home_page.py
├── tests/ # Test case per fitur
│ └── login/
│ └── test_login.py
├── utils/
│ └── email_report.py # Fungsi kirim email dengan attachment
├── .env # Variabel email (jangan di-push)
├── .gitignore
├── conftest.py # Fixture Playwright untuk pytest
├── run_tests.py # Entry point: jalankan test + kirim email
├── requirements.txt
└── README.md