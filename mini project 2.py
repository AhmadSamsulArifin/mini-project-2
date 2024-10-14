from prettytable import PrettyTable

data_pajak = []

def tampilkan_data():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Pemajak", "Jumlah Pajak", "Jenis Kendaraan"]
    for idx, pajak in enumerate(data_pajak):
        table.add_row([idx + 1, pajak['nama'], pajak['jumlah'], pajak['jenis_kendaraan']])
    print(table)

def tambah_data(nama, jumlah, jenis_kendaraan):
    data_pajak.append({'nama': nama, 'jumlah': jumlah, 'jenis_kendaraan': jenis_kendaraan})
    print("Data pajak berhasil ditambahkan!")

def update_data(id, nama, jumlah, jenis_kendaraan):
    if 0 <= id < len(data_pajak):
        data_pajak[id]['nama'] = nama
        data_pajak[id]['jumlah'] = jumlah
        data_pajak[id]['jenis_kendaraan'] = jenis_kendaraan
        print("Data pajak berhasil diupdate!")
    else:
        print("ID tidak valid!")

def hapus_data(id):
    if 0 <= id < len(data_pajak):
        data_pajak.pop(id)
        print("Data pajak berhasil dihapus!")
    else:
        print("ID tidak valid!")

def transaksi(nama_pembayar, id_pajak):
    if 0 <= id_pajak < len(data_pajak):
        pajak = data_pajak[id_pajak]
        print(f"Transaksi berhasil! {nama_pembayar} telah membayar {pajak['jumlah']} untuk pajak {pajak['nama']} ({pajak['jenis_kendaraan']}).")
    else:
        print("ID pajak tidak valid!")

def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tambah Data Pajak")
        print("2. Tampilkan Data Pajak")
        print("3. Update Data Pajak")
        print("4. Hapus Data Pajak")
        print("5. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            nama = input("Nama Pemajak: ")
            jumlah = input("Jumlah Pajak: ")
            jenis_kendaraan = input("Jenis Kendaraan: ")
            tambah_data(nama, jumlah, jenis_kendaraan)
        elif pilihan == '2':
            tampilkan_data()
        elif pilihan == '3':
            id = int(input("ID Pajak yang ingin diupdate: ")) - 1
            nama = input("Nama Pemajak baru: ")
            jumlah = input("Jumlah Pajak baru: ")
            jenis_kendaraan = input("Jenis Kendaraan baru: ")
            update_data(id, nama, jumlah, jenis_kendaraan)
        elif pilihan == '4':
            id = int(input("ID Pajak yang ingin dihapus: ")) - 1
            hapus_data(id)
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid!")

def menu_pembayar():
    while True:
        print("\n--- Menu Pembayar ---")
        print("1. Tampilkan Data Pajak")
        print("2. Transaksi")
        print("3. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            nama_pembayar = input("Nama Pembayar: ")
            id_pajak = int(input("ID Pajak yang ingin dibayar: ")) - 1
            transaksi(nama_pembayar, id_pajak)
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid!")

def login():
    print("Selamat datang di sistem pembayaran pajak samsat kota semarang!")
    while True:
        role = input("Masukkan role (admin/pembayar/keluar): ").lower()
        if role == 'admin':
            menu_admin()
        elif role == 'pembayar':
            menu_pembayar()
        elif role == 'keluar':
            print("Terima kasih! Semoga Selamat Sampai Tujuan.")
            break
        else:
            print("Role tidak valid!")


if __name__ == "__main__":
    while True:
        login()
