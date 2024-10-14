from prettytable import PrettyTable

premi_data = []  # Menyimpan data-data premi
users = {}  # Menyimpan data-data user
admin = {"yuda": "000"}  # Akun admin

def menu():
    while True:
        print("\n--- Halaman Utama ---")
        print("1. Login Sebagai Admin")
        print("2. Login Sebagai User")
        print("3. Registrasi User Baru")
        print("4. Keluar")
        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            login_admin()
        elif pilihan == '2':
            login_user()
        elif pilihan == '3':
            regis_user()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

def regis_user():
    username = input("Masukkan username baru: ")
    if username in users:
        print("Username sudah terdaftar.")
    else:
        password = input("Masukkan password: ")
        users[username] = password
        print("User berhasil terdaftar.")

def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")

    if username in admin and admin[username] == password:
        print(f"Selamat datang, Admin {username}.")
        menu_admin()
    else:
        print("Username atau password salah.")

def login_user():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"Selamat datang, {username}.")
        menu_user(username)
    else:
        print("Username atau password salah.")

def hitung_premi(tingkat_penyakit):
    if tingkat_penyakit == "ringan":
        return 50000
    elif tingkat_penyakit == "sedang":
        return 100000
    elif tingkat_penyakit == "berat":
        return 200000
    else:
        return 300000

def buat_premi(username):
    umur = input("Masukkan umur anda: ")
    tingkat_penyakit = input("Masukkan tingkatan penyakit (ringan/sedang/berat/ekstrem): ").lower()
    premi = hitung_premi(tingkat_penyakit)
    status_pembayaran = input("Apakah Anda ingin membayar premi sekarang? (ya/tidak): ").lower()
    print("--------------------------------------------------------")

    if status_pembayaran == 'ya':
        print(f"Pembayaran sebesar {premi} berhasil dilakukan.")
        premi_data.append({"user": username, "umur": umur, "tingkat_penyakit": tingkat_penyakit, "premi": premi, "status_pembayaran": "dibayar"})
    else:
        print("Premi tidak dibayar.")
        premi_data.append({"user": username, "umur": umur, "tingkat_penyakit": tingkat_penyakit, "premi": premi, "status_pembayaran": "belum dibayar"})

    print("Premi berhasil dihitung dan status pembayaran diperbarui.")

def ubah_premi(username):
    user_premi = [data for data in premi_data if data['user'] == username]
    if not user_premi:
        print("Anda belum menghitung premi.")
        return
    
    print("Data Premi Anda:")
    table = PrettyTable()
    table.field_names = ["Nomor", "User", "Umur", "Tingkatan Penyakit", "Premi", "Status Pembayaran"]
    for idx, data in enumerate(user_premi, 1):
        table.add_row([idx, data['user'], data['umur'], data['tingkat_penyakit'], data['premi'], data['status_pembayaran']])
    print(table)

    nomor = int(input("Masukkan nomor premi yang ingin diubah: ")) - 1
    if 0 <= nomor < len(user_premi):
        umur_baru = input("Masukkan umur baru: ")
        tingkat_penyakit = input("Masukkan tingkatan penyakit baru (ringan/sedang/berat/ekstrem): ").lower()
        premi = hitung_premi(tingkat_penyakit)
        status_pembayaran = input("Apakah Anda ingin membayar premi sekarang? (ya/tidak): ").lower()

        user_premi[nomor]['umur'] = umur_baru
        user_premi[nomor]['tingkat_penyakit'] = tingkat_penyakit
        user_premi[nomor]['premi'] = premi

        if status_pembayaran == 'ya':
            print(f"Pembayaran sebesar {premi} berhasil dilakukan.")
            user_premi[nomor]['status_pembayaran'] = "dibayar"
        else:
            user_premi[nomor]['status_pembayaran'] = "belum dibayar"

        print("Data premi berhasil diubah.")
    else:
        print("Nomor premi tidak valid.")

def lihat_premi():
    if not premi_data:
        print("Belum ada data premi.")
    else:
        table = PrettyTable()
        table.field_names = ["Nomor", "User", "Umur", "Tingkatan Penyakit", "Premi", "Status Pembayaran"]
        for idx, data in enumerate(premi_data, 1):
            table.add_row([idx, data['user'], data['umur'], data['tingkat_penyakit'], data['premi'], data['status_pembayaran']])
        print(table)

def menu_user(username):
    while True:
        print("\n--- Halaman User ---")
        print("1. Buat Premi")
        print("2. Ubah Data Premi")
        print("3. Lihat Data Premi Saya")
        print("4. Keluar")
        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            buat_premi(username)
        elif pilihan == '2':
            ubah_premi(username)
        elif pilihan == '3':
            lihat_data_premi(username)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

def lihat_data_premi(username):
    user_premi = [data for data in premi_data if data['user'] == username]
    if not user_premi:
        print("Anda belum menghitung premi.")
    else:
        table = PrettyTable()
        table.field_names = ["Nomor", "User", "Umur", "Tingkatan Penyakit", "Premi", "Status Pembayaran"]
        for idx, data in enumerate(user_premi, 1):
            table.add_row([idx, data['user'], data['umur'], data['tingkat_penyakit'], data['premi'], data['status_pembayaran']])
        print(table)

def menu_admin():
    while True:
        print("\n--- Halaman Admin ---")
        print("1. Buat Data Premi Baru")
        print("2. Lihat Semua Data Premi")
        print("3. Ubah Data Premi")
        print("4. Hapus Data Premi")
        print("5. Keluar")
        pilihan = input("Masukkan Pilihan: ")

        if pilihan == '1':
            buat_premi_admin()
        elif pilihan == '2':
            lihat_premi()
        elif pilihan == '3':
            ubah_data_premi_admin()
        elif pilihan == '4':
            hapus_data_premi()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

def buat_premi_admin():
    username = input("Masukkan username pemohon: ")
    umur = input("Masukkan umur pemohon: ")
    tingkat_penyakit = input("Masukkan tingkatan penyakit (ringan/sedang/berat/ekstrem): ").lower()
    premi = hitung_premi(tingkat_penyakit)
    status_pembayaran = input("Apakah Anda ingin membayar premi sekarang? (ya/tidak): ").lower()
    print("--------------------------------------------------------")

    if status_pembayaran == 'ya':
        status_pembayaran = "dibayar"
        print(f"Pembayaran sebesar {premi} berhasil dilakukan.")
    else:
        status_pembayaran = "belum dibayar"

    premi_data.append({
        "user": username,
        "umur": umur,
        "tingkat_penyakit": tingkat_penyakit,
        "premi": premi,
        "status_pembayaran": status_pembayaran
    })

    print("Data premi berhasil dibuat.")

def ubah_data_premi_admin():
    lihat_premi()
    if not premi_data:
        return
    
    nomor = int(input("Masukkan nomor premi yang ingin diubah: ")) - 1
    if 0 <= nomor < len(premi_data):
        umur_baru = input("Masukkan umur baru: ")
        tingkat_penyakit = input("Masukkan tingkatan penyakit baru (ringan/sedang/berat/ekstrem): ").lower()
        premi = hitung_premi(tingkat_penyakit)
        status_pembayaran = input("Apakah Anda ingin membayar premi sekarang? (ya/tidak): ").lower()

        premi_data[nomor]['umur'] = umur_baru  # Update umur
        premi_data[nomor]['tingkat_penyakit'] = tingkat_penyakit
        premi_data[nomor]['premi'] = premi

        if status_pembayaran == 'ya':
            premi_data[nomor]['status_pembayaran'] = "dibayar"
        else:
            premi_data[nomor]['status_pembayaran'] = "belum dibayar"

        print("Data premi berhasil diubah.")
    else:
        print("Nomor premi tidak valid.")

def hapus_data_premi():
    lihat_premi()
    if not premi_data:
        return
    
    nomor = int(input("Masukkan nomor premi yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(premi_data):
        premi_data.pop(nomor)
        print("Data premi berhasil dihapus.")
    else:
        print("Nomor premi tidak valid.")

if __name__ == "__main__":
    menu()
