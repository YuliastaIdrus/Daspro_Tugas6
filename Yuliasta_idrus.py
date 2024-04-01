print("\n ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈program sederhana pemesanan tiket bioskop≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print("\nSilahkan mengisi data diri anda")
nama = input("masukkan nama pengunjung bioskop:")
usia = int(input("masukkan usia anda: "))

print("\n ≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈Welcome To Cinema XXI≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈")
print("Nama Pengunjung :",nama)

print("Usia Pengunjung:",usia)
if usia>=19:
    print("anda boleh ikut nonton")
else:
    print("Maaf anda tidak bisa ikut nonton")

   # Daftar film beserta harga
daftar_film = {
    "Drama": {
        "Romantis": 45.000,
        "Tragis": 50.000,
        "Komedi Romantis": 40.000
    },
    "Komedi": {
        "Parodi": 35.000,
        "Romantis": 40.000,
        "Hitam": 45.000
    },
    "Aksi": {
        "Laga": 20.000,
        "Superhero": 30.000,
        "Misi Rahasia": 50.000
    },
    "Horor": {
        "Falak": 45.000,
        "The nun": 45.000,
        "Annabelle": 50.000
    }
}

# Menampilkan pilihan genre film
print("Pilih genre film:")
for key in daftar_film:
    print(key)

# Meminta pengguna untuk memilih
pilihan_genre = input("Masukkan nama genre film yang Anda pilih: ").strip()

# Memeriksa apakah genre tersebut termasuk dalam daftar film
if pilihan_genre in daftar_film:
    print(f"\nGenre film yang Anda pilih adalah {pilihan_genre}.")
    # Jika genre yang dipilih adalah "Horor" atau "Aksi" atau "Komedi", tampilkan pilihan sub-genre
    if pilihan_genre == "Horor" or pilihan_genre == "Aksi" or pilihan_genre == "Komedi" or pilihan_genre == "Drama":
        print("Pilihan sub-genre:")
        for sub_genre, harga in daftar_film[pilihan_genre].items():
            print(f"{sub_genre} - Harga: Rp{harga}")
        pilihan_sub_genre = input("\nMasukkan sub-genre yang Anda pilih: ")
        if pilihan_sub_genre in daftar_film[pilihan_genre]:
            harga_film = daftar_film[pilihan_genre][pilihan_sub_genre]
            print(f"\n\nAnda memilih film genre {pilihan_genre} dengan sub-genre {pilihan_sub_genre}.")
            print(f"Harga film: Rp{harga_film}")
        else:
            print("Sub-genre yang Anda pilih tidak valid.")
    else:
        print(f"Anda memilih film genre {pilihan_genre}.")
else:
    print("Genre yang Anda pilih tidak valid.")