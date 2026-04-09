# 📚 Folio — Personal Public Wiki

Website dokumentasi pribadi berbasis Django. Bisa dibaca publik tanpa login, tapi hanya admin yang bisa menulis dan mengedit.

---

## ✨ Fitur

- **Halaman publik** — semua orang bisa membaca tanpa login
- **Markdown editor** — EasyMDE dengan live preview side-by-side
- **Syntax highlighting** — kode otomatis diwarnai
- **Admin dashboard** — kelola semua halaman dalam satu tempat
- **Draft / Published** — kontrol visibilitas halaman
- **Search** — cari halaman berdasarkan judul & isi
- **Auto slug** — URL otomatis dibuat dari judul
- **Responsive** — nyaman di HP maupun desktop
- **Autosave** — editor otomatis menyimpan draft lokal

---

## 🚀 Setup (Pertama Kali)

### Cara cepat (pakai script):

```bash
cd folio
chmod +x setup.sh
./setup.sh
```

### Cara manual:

```bash
# 1. Buat virtual environment
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
# venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Migrasi database
python manage.py migrate

# 4. Buat akun admin
python manage.py createsuperuser

# 5. Jalankan server
python manage.py runserver
```

Buka browser: **http://127.0.0.1:8000**

---

## 🗂 Struktur URL

| URL | Keterangan |
|-----|-----------|
| `/` | Homepage — daftar semua halaman publik |
| `/page/<slug>/` | Halaman wiki (publik) |
| `/login/` | Login admin |
| `/admin-dashboard/` | Dashboard admin |
| `/admin-dashboard/create/` | Buat halaman baru |
| `/admin-dashboard/edit/<slug>/` | Edit halaman |
| `/admin-dashboard/delete/<slug>/` | Hapus halaman |
| `/django-admin/` | Django built-in admin |

---

## 📁 Struktur Project

```
folio/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── wiki/
│   ├── migrations/
│   ├── templates/wiki/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── page_detail.html
│   │   ├── page_form.html
│   │   ├── page_confirm_delete.html
│   │   ├── admin_dashboard.html
│   │   └── login.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── manage.py
├── requirements.txt
└── setup.sh
```

---

## 🔄 Menjalankan Setelah Setup

```bash
source venv/bin/activate
python manage.py runserver
```

---

## 📝 Cara Pakai

1. Buka `http://127.0.0.1:8000/login/`
2. Login dengan akun admin yang sudah dibuat
3. Klik **New Page** di dashboard
4. Tulis konten dengan Markdown di editor
5. Pilih status **Published** agar halaman muncul publik
6. Klik **Create Page**

---

## ⚙️ Konfigurasi

Edit `config/settings.py`:

- `TIME_ZONE` → sesuaikan timezone (default: `Asia/Jakarta`)
- `SECRET_KEY` → ganti dengan key acak untuk keamanan
- `DEBUG` → set ke `False` untuk production
