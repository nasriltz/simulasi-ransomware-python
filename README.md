# Simulasi Ransomware PoC (Educational Purpose)

Proyek ini mensimulasikan cara kerja Ransomware modern yang menggunakan algoritma enkripsi standar industri (AES) dan memanfaatkan Telegram Bot API sebagai jalur pencurian kunci (Exfiltration) agar penyerang dapat menerima kunci dekripsi secara jarak jauh (remote).

## Persiapan Lingkungan

    OS: Kali Linux / Termux (Android)

    Library Python: cryptography, requests

    Alat Komunikasi: Telegram Bot API (@BotFather)

## Komponen Utama
* 'kunci.py': Script pengunci (Encryption) & pengirim kunci ke Telegram.
* `selamatkan.py`: Script penawar (Decryption) untuk mengembalikan file.
* `target.txt`: File simulasi yang menjadi korban.

## Cara Kerja
1. **Encryption**: Menggunakan library `cryptography` dengan algoritma Fernet (AES).
2. **Exfiltration**: Kunci enkripsi dikirim secara otomatis ke Telegram Bot API milik attacker.
3. **C2 Communication**: Menggunakan jalur HTTPS agar tidak dicurigai oleh firewall sederhana.

## Cara Mencegah:

   jangan menjalankan script atau aplikasi dari sumber tidak dikenal.

   Pantau lalu lintas jaringan (Network Monitoring) untuk mendeteksi aktivitas API yang mencurigakan.

   Selalu lakukan backup data secara offline (Cold Backup).

## Kesimpulan 

Simulasi ini menunjukkan betapa mudahnya malware berkomunikasi dengan server luar menggunakan layanan legal seperti Telegram.
