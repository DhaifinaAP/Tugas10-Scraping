# Web Scraping Pinterest Automation

## Deskripsi Proyek
Proyek ini adalah skrip Python yang digunakan untuk mengambil data pin dari Pinterest berdasarkan kata kunci pencarian yang dimasukkan pengguna. Data yang diambil berupa URL konten, sumber gambar, dan deskripsi, yang kemudian disimpan ke dalam file CSV.

## Prasyarat
Sebelum menjalankan proyek ini, pastikan Anda telah menginstal perangkat lunak dan requirements berikut:
- **Python 3.x**
- **Google Chrome** (versi terbaru)
- **Chromedriver** (dikelola oleh `webdriver_manager`)
- **Requirements**:
  - `pandas`
  - `selenium`
  - `webdriver-manager`

## Instalasi

1. **Clone repository ini** (jika proyek ini di-host di repositori git):
   ```bash
   git clone https://github.com/username/project-name.git
   cd project-name
   ```

2. **Instal dependensi Python**:
   Gunakan `venv` untuk mengelola environment Python. Lalu, jalankan:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Proyek

1. **Jalankan skrip Python**:
   Pastikan Anda berada di direktori proyek, lalu jalankan skrip dengan perintah berikut:
   ```bash
   python scraping.py
   ```

2. **Proses skrip**:
   - Skrip akan membuka Chrome dalam mode incognito dan mengakses halaman Pinterest dengan pencarian berdasarkan kata kunci yang Anda tentukan.
   - Skrip akan menggulir ke bawah hingga lima kali untuk memuat lebih banyak konten.
   - Setelah itu, skrip akan mengumpulkan data dari elemen yang terlihat di halaman.
   - Data yang diambil akan disimpan dalam file `pinterest_data.csv`.

## Struktur File
- **scraping.py**: Skrip utama proyek yang berfungsi untuk mengambil data dari Pinterest.
- **pinterest_data.csv**: File hasil pengumpulan data dari Pinterest yang berisi URL konten, sumber gambar, dan deskripsi.

## Masalah dan Solusi Umum
- **Error "Unable to locate element"**: Pastikan elemen pada halaman masih menggunakan selektor yang sama. Elemen dapat berubah karena pembaruan pada halaman web.
- **Browser tidak terbuka atau terdeteksi sebagai tidak aman**: Pastikan Anda menggunakan versi `ChromeDriver` yang cocok dengan versi Chrome Anda.
- **Data tidak muncul**: Pastikan kata kunci pencarian yang digunakan menghasilkan konten yang valid dan halaman berhasil dimuat dengan benar.
