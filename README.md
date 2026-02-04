# Simulasi Ransomware PoC (Educational Purpose)

Repository ini berisi simulasi sederhana cara kerja Ransomware menggunakan Python. Proyek ini dibuat untuk memenuhi tugas mata kuliah Keamanan Siber.

## Komponen Utama
* `kunci.py`: Script pengunci (Encryption) & pengirim kunci ke Telegram.
* `selamatkan.py`: Script penawar (Decryption) untuk mengembalikan file.
* `target.txt`: File simulasi yang menjadi korban.

## Cara Kerja
1. **Encryption**: Menggunakan library `cryptography` dengan algoritma Fernet (AES).
2. **Exfiltration**: Kunci enkripsi dikirim secara otomatis ke Telegram Bot API milik attacker.
3. **C2 Communication**: Menggunakan jalur HTTPS agar tidak dicurigai oleh firewall sederhana.

## Disclaimer
Proyek ini hanya untuk **tujuan edukasi**. Dilarang keras menggunakan script ini untuk aktivitas ilegal. Penulis tidak bertanggung jawab atas penyalahgunaan kode ini.
