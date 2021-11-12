import os
import json

# fungsi untuk mengosongkan layar
def mengosongkan_layar():
   # untuk linux dan mac os
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # untuk windows os
      _ = os.system('cls')
      
# fungsi mencek entah satu berkas ada atau tidak
def cek(berkas):
    return os.path.exists(berkas)

def memasukkan_data_nilai():
    # membuat variable daftar_nilai
    daftar_nilai = []

    # sebelum memasukkan daftar baru, muat dulu data lama supaya jangan terhapus
    # mencek entah berkas data ada
    berkas = cek("data_sekolah.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("data_sekolah.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat daftar nilai dari data yang telah ada
        with open("data_sekolah.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["nilai"]:
                nama = i["nama"]
                gender = i["gender"]
                nilai = i["nilai"]
                daftar_nilai.append({"nama": nama, "gender": gender, "nilai": nilai})
        
    # fungsi loop untuk memasukkan data baru
    keluar = False
    
    while keluar == False:
        # mengosongkan layar
        mengosongkan_layar()
        
        # menampilkan formulir isian
        print("*" * 30)
        print("SD Negeri Hilizamara'u\n".center(30))
        print("Memasukkan Nilai Siswa".center(30))
        print("*" * 30)
        nama = input("Nama                : ")
        jenis_kelamin = False
        while jenis_kelamin == False:
            gender = input("Jenis kelamin (l/p) : ")
            if gender == "l" or gender == "p":
                jenis_kelamin = True
            else:
                print("Silakan memasukkan l atau p untuk gender")
                
        nilai  = input("Nilai               : ")
        print("*" * 30)
        
        # menyimpan data ke daftar nilai
        daftar_nilai.append({"nama": nama, "gender": gender, "nilai": nilai})

        # bagian berikut hanya memastikan entah masih ada data yang mau dimasukkan
        # bila ada, maka proses dimulai kembali dari atas
        # kalau tidak proses dihentikan dan data dimasukkan ke database
        masih_ada = input("Masih ada lagi? (y/t) ")

        if masih_ada == "t":
            keluar = True
            mengosongkan_layar()
                
    # menyimpan data ke berkas daftar
    with open('data_sekolah.json', 'w') as berkas:
        data = {"nilai": daftar_nilai}
        json.dump(data, berkas)
        

# fungsi untuk menampilkan daftar nilai ke layar   
def menampilkan_daftar_nilai():

    # mendeklarasikan berbagai variable
    daftar_nilai = []
    
    # menampilkan judul
    mengosongkan_layar()
    print("*" * 30)
    print("SD Negeri Hilizamara'u\n".center(30))
    print("Daftar Nilai Siswa".center(30))
    print("*" * 30)
    print("Nama: nilai")
    
    # memuat data dari database
    # mencek dulu entah berkas data ada
    berkas = cek("data_sekolah.json")
    if (berkas == False):
        print("Database kosong.")
    elif (berkas == True) and (os.stat("data_sekolah.json").st_size == 0):
        print("Database kosong.")
    else:
        # memuat daftar nilai yang lama dari database
        with open("data_sekolah.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["nilai"]:
                nama = i["nama"]
                gender = i["gender"]
                nilai = i["nilai"]
                print(f"{nama} ({gender}): {nilai}")

    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()


# fungsi untuk membuat backup
def membuat_backup():

    print()
    print("Sebentar yah... sedang membuat backup")
    print("*")
    print("*")
    print("*")
    print("*")

    # mendeklarasikan berbagai variable
    daftar_nilai = []

    # memuat data lama dari database
    # mencek entah berkas data ada
    berkas = cek("data_sekolah.json")
    if (berkas == False):
        print("Database kosong. Tak ada yang perlu di-backup.")
    elif (berkas == True) and (os.stat("data_sekolah.json").st_size == 0):
        print("Database kosong. Tak ada yang perlu di-backup.")
    else:
        # memuat daftar nilai yang lama dari database
        with open("data_sekolah.json") as f:
            json_data = json.load(f)
            # memuat daftar nilai
            for i in json_data["nilai"]:
                nama = i["nama"]
                gender = i["gender"]
                nilai = i["nilai"]
                daftar_nilai.append({"nama": nama, "gender": gender, "nilai": nilai})

                # membuat backup
                # di sini bisa dibuat fungsi menyimpan ke server
                # untuk sementara data di simpan ke data_backup.json saja.
                with open("backup_server.json", "w") as f:
                    data = {"nilai": daftar_nilai}
                    json.dump(data, f)

    print()
    print("No awai. Saohagölö!!!!!!")
    print("Mangawuli ba golayama!")
    print()
    # bagian berikut hanya untuk menunggu
    # supaya pesan backup sempat dibaca
    selesai = input("Tekan Enter untuk keluar ")
    if selesai == "y":
        print("Lau bale!")
    else:
        print("Bye!")

    mengosongkan_layar()
    
#    
#
# program mulai dari sini
#

keluar = False

while keluar == False:
    # mengosongkan layar
    mengosongkan_layar()

    # Menampilkan pilihan operasi
    print("*" * 30)
    print("SD Negeri Hilizamara'u\n".center(30))
    print()
    print("Daftar Nilai Siswa".center(30))
    print()
    print("*" * 30)
    print("Silakan memilih:")
    print("1. Memasukkan data nilai")
    print("2. Menampilkan daftar nilai")
    print("3. Membuat backup data")
    print("4. Keluar")
    print("*" * 30)
    print()

    pilihan = input("Pilihan Anda: ")

    if pilihan == "3":
        membuat_backup()   
    elif pilihan == "2":
        menampilkan_daftar_nilai()
    elif pilihan == "1":
        memasukkan_data_nilai()
    else:
        keluar = True    

