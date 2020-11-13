from os import system
from datetime import datetime

def view_menu():
	system("cls")
	menu = """
	-CHECK-IN DAN CHECK-OUT HOTEL ONLINE-
	-TOLONG MENGIKUTI LANGKAH DENGAN BAIK-
	[1] - CHECK IN
	[2] - TIPE KAMAR
	[3] - DEPOSIT
	[4] - PAYMENT
	[5] - BILL
	[6] - CHECK OUT
	[Q] - KELUAR
		"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_id_user():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(info_pelanggan)+1
	#year, month, day = str(year), str(month), str(day)
	id_user = str("%4d%02d%02d-A%03d" % (year, month, hari, counter))
	return id_user

def searching(suite):
	if suite in info_hotel:
		print(f"""
		-DATA DITEMUKAN-
	Nama:{suite}
	Harga:{info_hotel[suite]["price"]}
	Kapasitas:{info_hotel[suite]["kapasitas"]}
			""")

def searching2(id_user):
	if id_user in daftar_transaksi:
		print(f"""
			-DATA DITEMUKAN-
		ID pelanggan: {id_user}
		Nama pelanggan: {daftar_transaksi[id_user]['nama pelanggan']}
		Kamar Yang Dipesan:{daftar_transaksi[id_user]['kamar yang dipesan']}
		Harga: {daftar_transaksi[id_user]['total bill']}
			""")
	else:
		print("-DATA TIDAK DITEMUKAN-")
	input("Tekan ENTER untuk kembali ke MENU")


def biodata_pelanggan():
	print_header("-MASUKKAN BIODATA ANDA-")
	nama = input("Nama\t: ")
	telp = input("No.Telp\t: ")
	nomor_ktp = len(input("No. KTP\t:  "))
	total_kamar = input("Ingin Berapa Kamar : ")

	customer_ans = input("Tekan Y untuk menyimpan(Y/N): ")

	if verify_ans(customer_ans):
		id_user = create_id_user()
		print("Menyimpan Data...")
		info_pelanggan[id_user] = {
		"no.telp" : telp,
		"no.ktp" : nomor_ktp
		}
		print("Data Tersimpan")
	else:
		print("Data batal disimpan")
	input("Tekan ENTER untuk kembali ke MENU")


def room_type():
	print_header("-CARI KAMAR-")
	print(info_hotel)
	tipe = input("Kamar Yang Dicari : ")
	result = searching(tipe)
	input("Tekan ENTER untuk kembali ke MENU")


def deposit_payment():
	print_header("-DEPOSIT-")
	print("Deposit sebesar 500.000")
	user_ans = input("Tekan Y jika ingin membayar Deposit : ")
	print("Terima Kasih")
	input("Tekan ENTER untuk kembali ke MENU")


def checking_out():
	print_header("-CHECKIN-OUT-")
	input("Tekan Y untuk keluar dari situs : ")
	print("Terima kasih telah berkunjung ke situs ini.")
	input("Tekan ENTER untuk kembali ke MENU")


def payment_method():
	print_header("-PEMBAYARAN-")
	id_user = create_id_user()
	nama_pelanggan = input("Nama anda: ")
	banyak_kamar = int(input("Berapa Kamar yang anda pesan : "))
	kamar = input("Tipe Kamar anda : ")
	tipe_kamar = searching(kamar)
	harga = info_hotel[kamar]['price']*banyak_kamar
	print(f"Harga = {banyak_kamar}x{info_hotel[kamar]['price']} : {harga}")
	user_ans = input("Tekan Y untuk membayar : ")

	customer_ans = input("Tekan Y untuk menyimpan(Y/N): ")

	if verify_ans(customer_ans):
		print("Menyimpan Data...")
		daftar_transaksi[id_user] = {
		"nama pelanggan" : nama_pelanggan,
		"kamar yang dipesan" : kamar,
		"banyak kamar" : banyak_kamar,
		"total bill" : harga
		}
		print("Data Tersimpan")
	print("Terima Kasih karena telah melakukan Pembayaran")
	input("Tekan ENTER untuk kembali ke MENU")





def bill_total():
	print_header("-Total Bill-")
	name = input(" ")
	bill = searching2(name)
	

def check_input(char):
	char = char.upper()
	if char == "Q":
		return True
	elif char == "1":
		biodata_pelanggan()
	elif char == "2":
		room_type()
	elif char == "3":
		deposit_payment()
	elif char == "4":
		payment_method()
	elif char == "5":
		bill_total()
	elif char == "6":
		checking_out()


info_pelanggan = {
	"Ibu Wati" : {
	"nama" : "Ibu Wati",
	"no.telp" : "08912389120",
	"no.ktp" : "001293810"
	},
	"Pak Deni" : {
	"nama" : "Pak Deni",
	"no.telp" : "081287918237",
	"no.ktp" : "001892892"
	}
}
stop = False


info_hotel = {
	"King suite" : {
		"price" : 1_500_000,
		"kapasitas" : 4
	},
	"Queen suite" : {
		"price" : 1_200_000,
		"kapasitas" : 3
	},
	"Normal suite" : {
		"price" : 900_000,
		"kapasitas" : 2
	}
}

daftar_transaksi = {
	"20201019-A001" : {
	"nama pelanggan" : "Ibu Nuri", 
	"kamar yang dipesan" : "King suite",
	"banyak kamar" : 3,
	"total bill" : 4_500_000
	},
	"20201019-A002" : {
	"nama pelanggan" : "Ibu Sulastri",
	"kamar yang dipesan" : "Normal suite",
	"banyak kamar" : 2,
	"total bill" : 1_800_000
	}
}



while not stop:
	view_menu()
	customer_input = input("Pilihan : ")
	stop = check_input(customer_input)