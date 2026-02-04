from cryptography.fernet import Fernet

# Teks di dalam input() cuma label, jangan diisi kunci di sini
print("--- PROGRAM PENYELAMAT FILE ---")
kunci_input = input(" wtYig18tYdRuBUiKZ7ZlGC8Xgvb2OdVYafLI2nx475o= ").strip()

try:
    # Mengubah teks input menjadi format bytes yang dipahami Fernet
    cipher = Fernet(kunci_input.encode())

    with open("target.txt", "rb") as f:
        data_terkunci = f.read()

    # Proses membuka gembok
    data_asli = cipher.decrypt(data_terkunci)

    with open("target.txt", "wb") as f:
        f.write(data_asli)

    print("\n✅ BERHASIL! File 'target.txt' sudah normal kembali.")
    print(f"Isi file asli: {data_asli.decode()}")

except Exception as e:
    print(f"\n❌ GAGAL! Error: {e}")
    print("Pastikan kuncinya pas (44 karakter) dan tidak ada spasi yang tertinggal.")
