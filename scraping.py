import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Pengaturan untuk mode incognito dan menghindari deteksi Selenium
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Menonaktifkan deteksi otomasi
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Menonaktifkan fitur otomatisasi
chrome_options.add_experimental_option("useAutomationExtension", False)  # Menonaktifkan ekstensi otomatisasi

# Inisialisasi driver menggunakan WebDriver Manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # Buka URL Pinterest setelah login berhasil
    pinterest_url = "https://id.pinterest.com/search/pins/?rs=ac&len=2&q=interior-ideas&eq=interior-&etslf=23711"
    driver.get(pinterest_url)

    # Scroll ke bagian bawah halaman
    last_height = driver.execute_script("return document.body.scrollHeight")
   # Scroll ke bagian bawah halaman
    scroll_count = 0  # Inisialisasi counter untuk jumlah scroll
    max_scrolls = 5    # Tentukan jumlah maksimum scroll

    while scroll_count < max_scrolls:
        # Scroll ke bawah
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Tunggu beberapa detik untuk memuat lebih banyak konten
        time.sleep(2)

        # Hitung tinggi baru
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Tinggi baru ditetapkan ke tinggi terakhir setelah scrolling
        last_height = new_height

        # Increment counter setelah satu scroll dilakukan
        scroll_count += 1
        
    try:
        # Tunggu hingga elemen yang menunjukkan bahwa halaman Pinterest telah dimuat
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[role="listitem"]')))
        print("Halaman Pinterest berhasil dimuat.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menunggu halaman Pinterest untuk dimuat: {e}")

    # Ambil semua elemen dengan class tertentu
    items = driver.find_elements(By.CSS_SELECTOR, '[role="listitem"]')
    if not items:
        print("Elemen tidak ditemukan. Pastikan selektor CSS sesuai.")
    else:
        print(f"Ditemukan {len(items)} elemen.")

    # Buat list untuk menyimpan data
    data = []

    # Loop melalui setiap elemen dan ambil data yang diperlukan
    for index, item in enumerate(items):
        try:
            # Ambil nilai dari atribut data-test-pin-id
            pin_id_element = item.find_element(By.CSS_SELECTOR, 'div[data-test-id="pin"]')
            pin_id = pin_id_element.get_attribute("data-test-pin-id")  # Mengambil nilai pin ID

            # Ambil elemen <img> untuk alt dan src
            img_element = item.find_element(By.CSS_SELECTOR, 'img.hCL.kVc.L4E.MIw')
            img_alt = img_element.get_attribute("alt")
            description = img_alt.split(": ")[-1] if ": " in img_alt else img_alt  # Ambil deskripsi setelah tanda ": (This may contain: *)"
            
            img_src = img_element.get_attribute("src")  # Mengambil sumber gambar
            
            # Tambahkan data ke list dengan nomor urut
            data.append([index + 1, f'https://id.pinterest.com/pin/{pin_id}', img_src, description])
        except Exception as e:
            print(f"Terjadi kesalahan saat mengambil data dari item: {e}")

    # Ubah list menjadi DataFrame dengan tambahan kolom untuk nomor urut
    df = pd.DataFrame(data, columns=["No", "Url Content", "Image Source", "Description"])

    # Tampilkan DataFrame
    print(df)

    # Simpan DataFrame ke file CSV
    df.to_csv('pinterest_data.csv', index=False)

except Exception as e:
    print(f"Terjadi kesalahan saat proses login atau pengalihan ke Pinterest: {e}")
finally:
    # Tutup driver
    driver.quit()