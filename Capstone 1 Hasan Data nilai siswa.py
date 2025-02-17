
from tabulate import tabulate
from colorama import Fore, Back, Style, init
import sys
import pwinput
init(autoreset=True)

## Data nilai siswa
nilai_uts_ips = [
    {"id_siswa": "20250001", "Nama": "Andi Pratama", "L/P": "L", "Ekonomi": 65, "Sosiologi": 70, "Geografi": 75, "Bahasa Indonesia": 90, "Bahasa Inggris": 80, "Matematika": 88},
    {"id_siswa": "20250002", "Nama": "Budi Santoso", "L/P": "L", "Ekonomi": 60, "Sosiologi": 65, "Geografi": 72, "Bahasa Indonesia": 80, "Bahasa Inggris": 75, "Matematika": 82},
    {"id_siswa": "20250003", "Nama": "Clara Wulandari", "L/P": "P", "Ekonomi": 88, "Sosiologi": 65, "Geografi": 90, "Bahasa Indonesia": 85, "Bahasa Inggris": 93, "Matematika": 92},
    {"id_siswa": "20250004", "Nama": "Dina Melani", "L/P": "P", "Ekonomi": 70, "Sosiologi": 60, "Geografi": 60, "Bahasa Indonesia": 83, "Bahasa Inggris": 75, "Matematika": 88},
    {"id_siswa": "20250005", "Nama": "Eko Susanto", "L/P": "L", "Ekonomi": 76, "Sosiologi": 55, "Geografi": 68, "Bahasa Indonesia": 81, "Bahasa Inggris": 67, "Matematika": 89},
    {"id_siswa": "20250006", "Nama": "Fadil Akbar", "L/P": "L", "Ekonomi": 82, "Sosiologi": 60, "Geografi": 70, "Bahasa Indonesia": 55, "Bahasa Inggris": 88, "Matematika": 84},
    {"id_siswa": "20250007", "Nama": "Gita Permatasari", "L/P": "P", "Ekonomi": 65, "Sosiologi": 70, "Geografi": 60, "Bahasa Indonesia": 79, "Bahasa Inggris": 55, "Matematika": 84},
    {"id_siswa": "20250008", "Nama": "Hadi Prabowo", "L/P": "L", "Ekonomi": 50, "Sosiologi": 63, "Geografi": 72, "Bahasa Indonesia": 60, "Bahasa Inggris": 92, "Matematika": 91},
    {"id_siswa": "20250009", "Nama": "Ika Febriani", "L/P": "P", "Ekonomi": 65, "Sosiologi": 75, "Geografi": 55, "Bahasa Indonesia": 87, "Bahasa Inggris": 60, "Matematika": 81},
    {"id_siswa": "20250010", "Nama": "Joko Sutrisno", "L/P": "L", "Ekonomi": 72, "Sosiologi": 65, "Geografi": 88, "Bahasa Indonesia": 92, "Bahasa Inggris": 79, "Matematika": 55},
    {"id_siswa": "20250011", "Nama": "Karina Rahayu", "L/P": "P", "Ekonomi": 78, "Sosiologi": 62, "Geografi": 88, "Bahasa Indonesia": 60, "Bahasa Inggris": 77, "Matematika": 90},
    {"id_siswa": "20250012", "Nama": "Lita Sari", "L/P": "P", "Ekonomi": 55, "Sosiologi": 60, "Geografi": 80, "Bahasa Indonesia": 88, "Bahasa Inggris": 81, "Matematika": 83},
    {"id_siswa": "20250013", "Nama": "Muhammad Faris", "L/P": "L", "Ekonomi": 95, "Sosiologi": 58, "Geografi": 87, "Bahasa Indonesia": 92, "Bahasa Inggris": 85, "Matematika": 90},
    {"id_siswa": "20250014", "Nama": "Nadia Wijaya", "L/P": "P", "Ekonomi": 50, "Sosiologi": 67, "Geografi": 75, "Bahasa Indonesia": 79, "Bahasa Inggris": 78, "Matematika": 76},
    {"id_siswa": "20250015", "Nama": "Oscar Harahap", "L/P": "L", "Ekonomi": 60, "Sosiologi": 50, "Geografi": 60, "Bahasa Indonesia": 84, "Bahasa Inggris": 65, "Matematika": 80},
    {"id_siswa": "20250016", "Nama": "Putri Prameswari", "L/P": "P", "Ekonomi": 65, "Sosiologi": 76, "Geografi": 79, "Bahasa Indonesia": 71, "Bahasa Inggris": 82, "Matematika": 85},
    {"id_siswa": "20250017", "Nama": "Qoriq Rahmawati", "L/P": "P", "Ekonomi": 50, "Sosiologi": 62, "Geografi": 60, "Bahasa Indonesia": 87, "Bahasa Inggris": 75, "Matematika": 90},
    {"id_siswa": "20250018", "Nama": "Rudi Saputra", "L/P": "L", "Ekonomi": 65, "Sosiologi": 80, "Geografi": 70, "Bahasa Indonesia": 82, "Bahasa Inggris": 89, "Matematika": 74},
    {"id_siswa": "20250019", "Nama": "Siti Aminah", "L/P": "P", "Ekonomi": 74, "Sosiologi": 55, "Geografi": 79, "Bahasa Indonesia": 80, "Bahasa Inggris": 92, "Matematika": 86},
    {"id_siswa": "20250020", "Nama": "Toni Kurniawan", "L/P": "L", "Ekonomi": 83, "Sosiologi": 58, "Geografi": 72, "Bahasa Indonesia": 81, "Bahasa Inggris": 79, "Matematika": 88}
]

nilai_uas_ips = [
    {"id_siswa": "20250001", "Nama": "Andi Pratama", "L/P": "L", "Ekonomi": 70, "Sosiologi": 75, "Geografi": 80, "Bahasa Indonesia": 85, "Bahasa Inggris": 90, "Matematika": 92},
    {"id_siswa": "20250002", "Nama": "Budi Santoso", "L/P": "L", "Ekonomi": 62, "Sosiologi": 67, "Geografi": 75, "Bahasa Indonesia": 82, "Bahasa Inggris": 78, "Matematika": 80},
    {"id_siswa": "20250003", "Nama": "Clara Wulandari", "L/P": "P", "Ekonomi": 90, "Sosiologi": 68, "Geografi": 93, "Bahasa Indonesia": 87, "Bahasa Inggris": 95, "Matematika": 94},
    {"id_siswa": "20250004", "Nama": "Dina Melani", "L/P": "P", "Ekonomi": 75, "Sosiologi": 65, "Geografi": 65, "Bahasa Indonesia": 85, "Bahasa Inggris": 80, "Matematika": 90},
    {"id_siswa": "20250005", "Nama": "Eko Susanto", "L/P": "L", "Ekonomi": 80, "Sosiologi": 58, "Geografi": 70, "Bahasa Indonesia": 83, "Bahasa Inggris": 72, "Matematika": 91},
    {"id_siswa": "20250006", "Nama": "Fadil Akbar", "L/P": "L", "Ekonomi": 85, "Sosiologi": 65, "Geografi": 75, "Bahasa Indonesia": 60, "Bahasa Inggris": 90, "Matematika": 88},
    {"id_siswa": "20250007", "Nama": "Gita Permatasari", "L/P": "P", "Ekonomi": 70, "Sosiologi": 75, "Geografi": 65, "Bahasa Indonesia": 82, "Bahasa Inggris": 60, "Matematika": 85},
    {"id_siswa": "20250008", "Nama": "Hadi Prabowo", "L/P": "L", "Ekonomi": 55, "Sosiologi": 70, "Geografi": 75, "Bahasa Indonesia": 65, "Bahasa Inggris": 95, "Matematika": 93},
    {"id_siswa": "20250009", "Nama": "Ika Febriani", "L/P": "P", "Ekonomi": 70, "Sosiologi": 80, "Geografi": 60, "Bahasa Indonesia": 92, "Bahasa Inggris": 68, "Matematika": 83},
    {"id_siswa": "20250010", "Nama": "Joko Sutrisno", "L/P": "L", "Ekonomi": 75, "Sosiologi": 70, "Geografi": 90, "Bahasa Indonesia": 95, "Bahasa Inggris": 82, "Matematika": 60},
    {"id_siswa": "20250011", "Nama": "Karina Rahayu", "L/P": "P", "Ekonomi": 80, "Sosiologi": 70, "Geografi": 90, "Bahasa Indonesia": 70, "Bahasa Inggris": 80, "Matematika": 95},
    {"id_siswa": "20250012", "Nama": "Lita Sari", "L/P": "P", "Ekonomi": 60, "Sosiologi": 65, "Geografi": 85, "Bahasa Indonesia": 93, "Bahasa Inggris": 83, "Matematika": 88},
    {"id_siswa": "20250013", "Nama": "Muhammad Faris", "L/P": "L", "Ekonomi": 98, "Sosiologi": 65, "Geografi": 90, "Bahasa Indonesia": 95, "Bahasa Inggris": 90, "Matematika": 92},
    {"id_siswa": "20250014", "Nama": "Nadia Wijaya", "L/P": "P", "Ekonomi": 55, "Sosiologi": 70, "Geografi": 80, "Bahasa Indonesia": 80, "Bahasa Inggris": 82, "Matematika": 78},
    {"id_siswa": "20250015", "Nama": "Oscar Harahap", "L/P": "L", "Ekonomi": 70, "Sosiologi": 60, "Geografi": 75, "Bahasa Indonesia": 85, "Bahasa Inggris": 72, "Matematika": 85},
    {"id_siswa": "20250016", "Nama": "Putri Prameswari", "L/P": "P", "Ekonomi": 75, "Sosiologi": 80, "Geografi": 80, "Bahasa Indonesia": 72, "Bahasa Inggris": 90, "Matematika": 88},
    {"id_siswa": "20250017", "Nama": "Qoriq Rahmawati", "L/P": "P", "Ekonomi": 55, "Sosiologi": 70, "Geografi": 70, "Bahasa Indonesia": 90, "Bahasa Inggris": 80, "Matematika": 92},
    {"id_siswa": "20250018", "Nama": "Rudi Saputra", "L/P": "L", "Ekonomi": 75, "Sosiologi": 85, "Geografi": 80, "Bahasa Indonesia": 85, "Bahasa Inggris": 92, "Matematika": 78},
    {"id_siswa": "20250019", "Nama": "Siti Aminah", "L/P": "P", "Ekonomi": 78, "Sosiologi": 60, "Geografi": 85, "Bahasa Indonesia": 85, "Bahasa Inggris": 95, "Matematika": 89},
    {"id_siswa": "20250020", "Nama": "Toni Kurniawan", "L/P": "L", "Ekonomi": 85, "Sosiologi": 60, "Geografi": 75, "Bahasa Indonesia": 80, "Bahasa Inggris": 80, "Matematika": 90}
]

nilai_uts_ipa = [
    {"id_siswa": "20250101", "Nama": "Ahmad Rifai", "L/P": "L", "Fisika": 80, "Kimia": 75, "Biologi": 85, "Bahasa Indonesia": 78, "Bahasa Inggris": 82, "Matematika": 88},
    {"id_siswa": "20250102", "Nama": "Bella Purnama", "L/P": "P", "Fisika": 75, "Kimia": 70, "Biologi": 80, "Bahasa Indonesia": 85, "Bahasa Inggris": 78, "Matematika": 84},
    {"id_siswa": "20250103", "Nama": "Cinta Dwi", "L/P": "P", "Fisika": 70, "Kimia": 85, "Biologi": 90, "Bahasa Indonesia": 80, "Bahasa Inggris": 76, "Matematika": 77},
    {"id_siswa": "20250104", "Nama": "Dimas Hendra", "L/P": "L", "Fisika": 85, "Kimia": 80, "Biologi": 75, "Bahasa Indonesia": 90, "Bahasa Inggris": 84, "Matematika": 79},
    {"id_siswa": "20250105", "Nama": "Elsa Damayanti", "L/P": "P", "Fisika": 90, "Kimia": 85, "Biologi": 88, "Bahasa Indonesia": 85, "Bahasa Inggris": 87, "Matematika": 91},
    {"id_siswa": "20250106", "Nama": "Farhan Ilham", "L/P": "L", "Fisika": 78, "Kimia": 72, "Biologi": 80, "Bahasa Indonesia": 70, "Bahasa Inggris": 79, "Matematika": 82},
    {"id_siswa": "20250107", "Nama": "Gisela Maharani", "L/P": "P", "Fisika": 83, "Kimia": 77, "Biologi": 82, "Bahasa Indonesia": 80, "Bahasa Inggris": 79, "Matematika": 85},
    {"id_siswa": "20250108", "Nama": "Hans Satria", "L/P": "L", "Fisika": 76, "Kimia": 80, "Biologi": 84, "Bahasa Indonesia": 78, "Bahasa Inggris": 83, "Matematika": 88},
    {"id_siswa": "20250109", "Nama": "Indah Sekar", "L/P": "P", "Fisika": 90, "Kimia": 87, "Biologi": 92, "Bahasa Indonesia": 81, "Bahasa Inggris": 88, "Matematika": 91},
    {"id_siswa": "20250110", "Nama": "Jovan Prasetya", "L/P": "L", "Fisika": 85, "Kimia": 83, "Biologi": 86, "Bahasa Indonesia": 87, "Bahasa Inggris": 85, "Matematika": 90},
    {"id_siswa": "20250111", "Nama": "Karina Asmara", "L/P": "P", "Fisika": 79, "Kimia": 78, "Biologi": 80, "Bahasa Indonesia": 82, "Bahasa Inggris": 77, "Matematika": 84},
    {"id_siswa": "20250112", "Nama": "Luthfi Ramadan", "L/P": "L", "Fisika": 88, "Kimia": 92, "Biologi": 85, "Bahasa Indonesia": 79, "Bahasa Inggris": 80, "Matematika": 82},
    {"id_siswa": "20250113", "Nama": "Mega Syafira", "L/P": "P", "Fisika": 76, "Kimia": 81, "Biologi": 90, "Bahasa Indonesia": 84, "Bahasa Inggris": 83, "Matematika": 80},
    {"id_siswa": "20250114", "Nama": "Naufal Andika", "L/P": "L", "Fisika": 89, "Kimia": 85, "Biologi": 78, "Bahasa Indonesia": 90, "Bahasa Inggris": 87, "Matematika": 83},
    {"id_siswa": "20250115", "Nama": "Oktavia Dewi", "L/P": "P", "Fisika": 85, "Kimia": 87, "Biologi": 91, "Bahasa Indonesia": 82, "Bahasa Inggris": 88, "Matematika": 80},
    {"id_siswa": "20250116", "Nama": "Putra Prabowo", "L/P": "L", "Fisika": 72, "Kimia": 78, "Biologi": 80, "Bahasa Indonesia": 83, "Bahasa Inggris": 75, "Matematika": 77},
    {"id_siswa": "20250117", "Nama": "Riana Kurnia", "L/P": "P", "Fisika": 80, "Kimia": 82, "Biologi": 85, "Bahasa Indonesia": 76, "Bahasa Inggris": 78, "Matematika": 84},
    {"id_siswa": "20250118", "Nama": "Satria Candra", "L/P": "L", "Fisika": 83, "Kimia": 75, "Biologi": 80, "Bahasa Indonesia": 85, "Bahasa Inggris": 84, "Matematika": 86},
    {"id_siswa": "20250119", "Nama": "Tia Melia", "L/P": "P", "Fisika": 75, "Kimia": 79, "Biologi": 82, "Bahasa Indonesia": 84, "Bahasa Inggris": 80, "Matematika": 89},
    {"id_siswa": "20250120", "Nama": "Ujang Fadilah", "L/P": "L", "Fisika": 79, "Kimia": 83, "Biologi": 88, "Bahasa Indonesia": 82, "Bahasa Inggris": 76, "Matematika": 90}
]

nilai_uas_ipa = [
    {"id_siswa": "20250101", "Nama": "Ahmad Rifai", "L/P": "L", "Fisika": 82, "Kimia": 80, "Biologi": 86, "Bahasa Indonesia": 84, "Bahasa Inggris": 85, "Matematika": 87},
    {"id_siswa": "20250102", "Nama": "Bella Purnama", "L/P": "P", "Fisika": 79, "Kimia": 75, "Biologi": 83, "Bahasa Indonesia": 88, "Bahasa Inggris": 81, "Matematika": 85},
    {"id_siswa": "20250103", "Nama": "Cinta Dwi", "L/P": "P", "Fisika": 76, "Kimia": 87, "Biologi": 92, "Bahasa Indonesia": 83, "Bahasa Inggris": 78, "Matematika": 81},
    {"id_siswa": "20250104", "Nama": "Dimas Hendra", "L/P": "L", "Fisika": 88, "Kimia": 82, "Biologi": 77, "Bahasa Indonesia": 90, "Bahasa Inggris": 85, "Matematika": 80},
    {"id_siswa": "20250105", "Nama": "Elsa Damayanti", "L/P": "P", "Fisika": 93, "Kimia": 89, "Biologi": 91, "Bahasa Indonesia": 87, "Bahasa Inggris": 90, "Matematika": 93},
    {"id_siswa": "20250106", "Nama": "Farhan Ilham", "L/P": "L", "Fisika": 79, "Kimia": 74, "Biologi": 83, "Bahasa Indonesia": 72, "Bahasa Inggris": 80, "Matematika": 84},
    {"id_siswa": "20250107", "Nama": "Gisela Maharani", "L/P": "P", "Fisika": 85, "Kimia": 79, "Biologi": 85, "Bahasa Indonesia": 82, "Bahasa Inggris": 80, "Matematika": 89},
    {"id_siswa": "20250108", "Nama": "Hans Satria", "L/P": "L", "Fisika": 80, "Kimia": 82, "Biologi": 87, "Bahasa Indonesia": 80, "Bahasa Inggris": 85, "Matematika": 89},
    {"id_siswa": "20250109", "Nama": "Indah Sekar", "L/P": "P", "Fisika": 92, "Kimia": 89, "Biologi": 93, "Bahasa Indonesia": 84, "Bahasa Inggris": 89, "Matematika": 94},
    {"id_siswa": "20250110", "Nama": "Jovan Prasetya", "L/P": "L", "Fisika": 88, "Kimia": 85, "Biologi": 87, "Bahasa Indonesia": 90, "Bahasa Inggris": 88, "Matematika": 92},
    {"id_siswa": "20250111", "Nama": "Karina Asmara", "L/P": "P", "Fisika": 80, "Kimia": 79, "Biologi": 82, "Bahasa Indonesia": 86, "Bahasa Inggris": 80, "Matematika": 85},
    {"id_siswa": "20250112", "Nama": "Luthfi Ramadan", "L/P": "L", "Fisika": 89, "Kimia": 91, "Biologi": 84, "Bahasa Indonesia": 81, "Bahasa Inggris": 82, "Matematika": 84},
    {"id_siswa": "20250113", "Nama": "Mega Syafira", "L/P": "P", "Fisika": 78, "Kimia": 80, "Biologi": 90, "Bahasa Indonesia": 84, "Bahasa Inggris": 82, "Matematika": 81},
    {"id_siswa": "20250114", "Nama": "Naufal Andika", "L/P": "L", "Fisika": 91, "Kimia": 88, "Biologi": 82, "Bahasa Indonesia": 91, "Bahasa Inggris": 88, "Matematika": 83},
    {"id_siswa": "20250115", "Nama": "Oktavia Dewi", "L/P": "P", "Fisika": 86, "Kimia": 89, "Biologi": 92, "Bahasa Indonesia": 85, "Bahasa Inggris": 90, "Matematika": 83},
    {"id_siswa": "20250116", "Nama": "Putra Prabowo", "L/P": "L", "Fisika": 74, "Kimia": 79, "Biologi": 82, "Bahasa Indonesia": 85, "Bahasa Inggris": 77, "Matematika": 80},
    {"id_siswa": "20250117", "Nama": "Riana Kurnia", "L/P": "P", "Fisika": 81, "Kimia": 83, "Biologi": 86, "Bahasa Indonesia": 80, "Bahasa Inggris": 79, "Matematika": 85},
    {"id_siswa": "20250118", "Nama": "Satria Candra", "L/P": "L", "Fisika": 84, "Kimia": 76, "Biologi": 81, "Bahasa Indonesia": 86, "Bahasa Inggris": 85, "Matematika": 87},
    {"id_siswa": "20250119", "Nama": "Tia Melia", "L/P": "P", "Fisika": 80, "Kimia": 83, "Biologi": 86, "Bahasa Indonesia": 85, "Bahasa Inggris": 81, "Matematika": 90},
    {"id_siswa": "20250120", "Nama": "Ujang Fadilah", "L/P": "L", "Fisika": 83, "Kimia": 86, "Biologi": 89, "Bahasa Indonesia": 84, "Bahasa Inggris": 79, "Matematika": 91}
]

user = {"adminharapan" : "q1w2e3"}
def login():
    while True:
        try:
            username = input("Masukkan username: ")
            password = pwinput.pwinput("Masukkan password: ")
            if username in user and user[username] == password:
                print(f"{Fore.GREEN}Login Berhasil")
                break
            else:
                raise ValueError(f"{Fore.RED}ID atau password anad salah")
        except ValueError as login_gagal:
            print(f"{Fore.RED}Login gagal{login_gagal}")
            try_again = input("apakah anda ingin mencoba lagi?\nKetik 'ya' untuk mencoba\nKetik apapun untuk keluar").lower()
            if try_again != "ya":
                sys.exit()

            
def nilai_akhir(nilai_uts, nilai_uas): #Fungsi untuk menghiyung nilai akhir
    nilai_final = {} #dict kosong untuk menampung nilai akhir
    for key in nilai_uts:
        if key not in ["Nama","id_siswa","L/P"]: #lewati id siswa dan nama
            nilai_final[key] = nilai_uts[key]*0.4 + nilai_uas[key]*0.6 #isi dict kosong
    return nilai_final
        
nilai_gabungan_ips = []
nilai_gabungan_ipa = []
recycle_bin = []

# Membuat data nilai gabungan uts dan uas ips
for data_uts, data_uas in zip(nilai_uts_ips, nilai_uas_ips):
    nilai_final_siswa = nilai_akhir(data_uts,data_uas)

    row = {"id_siswa": data_uts["id_siswa"], "Nama": data_uts["Nama"], "L/P": data_uts["L/P"]}
    # Ambil mata pelajaran
    for mapel in data_uts.keys():
        if mapel not in ["id_siswa", "Nama", "L/P"]:
            row[f"{mapel}"] = (f"{data_uts[mapel]},{data_uas[mapel]},{round(nilai_final_siswa[mapel])}")

    nilai_gabungan_ips.append(row)

# Membuat data nilai gabungan uts dan uas ipa
for data_uts, data_uas in zip(nilai_uts_ipa, nilai_uas_ipa):
    nilai_final_siswa = nilai_akhir(data_uts,data_uas)

    row = {"id_siswa": data_uts["id_siswa"], "Nama": data_uts["Nama"], "L/P":data_uts["L/P"]}
    # Ambil mata pelajaran
    for mapel in data_uts.keys():
        if mapel not in ["id_siswa", "Nama", "L/P"]:
            row[f"{mapel}"] = (f"{data_uts[mapel]},{data_uas[mapel]},{round(nilai_final_siswa[mapel])}")

    nilai_gabungan_ipa.append(row)
    
#Fungsi untuk memisahkan kelas yang terhubung dengan nilai gabungan
def jenis_kelas(ipa_or_ips): 
            if ipa_or_ips == "ips":
                jenis_kelas = nilai_gabungan_ips
                return jenis_kelas
            else:
                jenis_kelas = nilai_gabungan_ipa
                return  jenis_kelas
            
def menampilkan_recycle_bin():  # Menampilkan data yang dihapus
    if recycle_bin == []:
        print(f"{Fore.LIGHTGREEN_EX}****** Recycle bin kosong ******")
    else:
        for data in recycle_bin: 
                for keys,values in data.items():
                    print(keys, values)
                print("\n")

def menampilkan_daftar_nilai():
    print("Data nilai SMA Harapan Bangsa")
    while True:
        try:
            daftar_nilai_ips_or_ipa = input("Pilih  data nilai kelas\nKetik 'ipa' atau 'ips' :").lower()
            if daftar_nilai_ips_or_ipa != "ips" and daftar_nilai_ips_or_ipa != "ipa":
                raise ValueError("Kelas harus ipa atau ips")
        except ValueError as error:
            print(f"{Fore.RED}Terjadi kesalahan {error}")
        else:
            print(f"Berikut daftar nilai (UTS|UAS|Akhir) kelas {daftar_nilai_ips_or_ipa}")
            print(tabulate(jenis_kelas(daftar_nilai_ips_or_ipa), headers = "keys", tablefmt = "grid" , showindex = False))
        lihat_daftar_nilai_lagi = input("Apakah anda ingin melihat daftar nilai lainnya?\nketik 'ya' untuk melihat kembali :").lower()
        if lihat_daftar_nilai_lagi != "ya":
            break
            
def menambah_data_nilai():
    submenu_tambah = input('''
    Menu Tambah Data nilai
                        
    1. Tambah data nilai siswa 
    2. Kembali ke main menu 
                        
    Ketik '1' untuk menambah data
    Ketik sembarang untuk kembali ke main menu: ''')
    id_siswa_ips_terakhir_tambah_satu = 21 #ID siswa baru dimulai dari 20 + 1
    id_siswa_ipa_terakhir_tambah_satu = 21

    while True:
        if submenu_tambah != "1":
            break
        try:
            print(f"{Fore.BLUE}Menambah data nilai siswa\nMohon isi data siswa")
            nama_siswa_baru = input("Nama siswa: ").title().strip()
            if not all(k.isalpha() or k.isspace() for k in nama_siswa_baru) or not nama_siswa_baru: #Mencegah user memasukkan angka atau mengosongkan nama
                raise ValueError("Nama tidak boleh kosong atau berupa angka")
            jenis_kelamin_siswa_baru = input("Jenis kelamin siswa\nKetik 'L' untuk laki - laki atau 'P' untuk perempuan: ").upper()
            if not (jenis_kelamin_siswa_baru == "P" or  jenis_kelamin_siswa_baru == "L"):
                raise ValueError("Jenis kelamin harus diisi dengan benar\n'L' untuk laki - laki, 'P' untuk perempuan")
            tahun_masuk_siswa = input("Tahun masuk siswa: ")
            if not tahun_masuk_siswa.isdigit():
                raise ValueError("Tahun masuk harus berupa angka")
            kelas_siswa_baru = input("Kelas siswa\nKetik 'ipa' atau 'ips': ").lower()
            if kelas_siswa_baru != "ips" and kelas_siswa_baru != "ipa":
                raise ValueError("Kelas harus ips atau ipa")
            if kelas_siswa_baru == "ips":
                kode_kelas = "00"
            else:
                kode_kelas = "01"
            
            # Memisahkan penambahan id baru antar kelas
            if kelas_siswa_baru == "ips": 
                id_siswa_baru = tahun_masuk_siswa + kode_kelas + str(id_siswa_ips_terakhir_tambah_satu)
            else:
                id_siswa_baru = tahun_masuk_siswa + kode_kelas + str(id_siswa_ipa_terakhir_tambah_satu)
            print(f"{Fore.GREEN}id {nama_siswa_baru} adalah {id_siswa_baru}")  
            if kelas_siswa_baru == "ips":
                while True:
                    try:
                        nilai_ekonomi_uts = int(input("Masukkan nilai UTS ekonomi siswa: "))
                        nilai_ekonomi_uas = int(input("Masukkan nilai UAS ekonomi siswa: "))
                        nilai_sosiologi_uts = int(input("Masukkan nilai UTS sosiologi siswa: "))
                        nilai_sosiologi_uas = int(input("Masukkan nilai UAS sosiologi siswa: "))
                        nilai_geografi_uts = int(input("Masukkan nilai UTS geografi siswa: "))
                        nilai_geografi_uas = int(input("Masukkan nilai UAS geografi siswa: "))
                        nilai_bahasa_indonesia_uts = int(input("Masukkan nilai UTS bahasa indonesia siswa: "))
                        nilai_bahasa_indonesia_uas = int(input("Masukkan nilai UAS bahasa indonesia siswa: "))
                        nilai_bahasa_inggris_uts= int(input("Masukkan nilai UTS bahasa inggris siswa: "))
                        nilai_bahasa_inggris_uas = int(input("Masukkan nilai UAS bahasa inggris siswa: "))
                        nilai_matematika_uts= int(input("Masukkan nilai UTS matematika siswa: "))
                        nilai_matematika_uas = int(input("Masukkan nilai UAS matematika siswa: "))
                    except ValueError:
                        print(f"{Fore.RED}Nilai harus berupa bilangan bulat")
                         
                    else:
                        simpan_data = input("Apakah anda yakin ingin menyimpan data ini\nKetik 'ya' untuk menyimpan: ")
                        if simpan_data != "ya":
                            print(f"{Fore.YELLOW}Data siswa tidak tersimpan")
                            break
                        nilai_uts_ips.append({
                                            "id_siswa": id_siswa_baru,
                                            "Nama": nama_siswa_baru,
                                            "L/P": jenis_kelamin_siswa_baru,
                                            "Ekonomi": nilai_ekonomi_uts,
                                            "Sosiologi": nilai_sosiologi_uts,
                                            "Geografi": nilai_geografi_uts,
                                            "Bahasa Indonesia": nilai_bahasa_indonesia_uts,
                                            "Bahasa Inggris": nilai_bahasa_inggris_uts,
                                            "Matematika": nilai_matematika_uts
                        })
                        nilai_uas_ips.append({
                                            "id_siswa": id_siswa_baru,
                                            "Nama": nama_siswa_baru,
                                            "L/P": jenis_kelamin_siswa_baru,
                                            "Ekonomi": nilai_ekonomi_uas,
                                            "Sosiologi": nilai_sosiologi_uas,
                                            "Geografi": nilai_geografi_uas,
                                            "Bahasa Indonesia": nilai_bahasa_indonesia_uts,
                                            "Bahasa Inggris": nilai_bahasa_inggris_uas,
                                            "Matematika": nilai_matematika_uas
                        })
                        for data_uts, data_uas in zip(nilai_uts_ips, nilai_uas_ips):
                            nilai_final_siswa = nilai_akhir(data_uts,data_uas)
                            row = {"id_siswa": data_uts["id_siswa"], "Nama": data_uts["Nama"], "L/P": data_uts["L/P"]}

                        # Mengupdate data nilai ips dengan data yang baru ditambah
                        for mapel in data_uts.keys():
                            if mapel not in ["id_siswa", "Nama", "L/P"]:
                                row[f"{mapel}"] = (f"{data_uts[mapel]},{data_uas[mapel]},{round(nilai_final_siswa[mapel])}")

                        nilai_gabungan_ips.append(row)
                        print(f"{Fore.GREEN}\nData nilai siswa berhasil disimpan\n")
                        print(f"Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_siswa_baru}")
                        print(tabulate(nilai_gabungan_ips, headers = "keys", tablefmt = "grid" , showindex = False))
                        break
            else:
                while True:
                    try:
                        nilai_fisika_uts = int(input("Masukkan nilai UTS fisika siswa: "))
                        nilai_fisika_uas = int(input("Masukkan nilai UAS fisika siswa: "))
                        nilai_kimia_uts = int(input("Masukkan nilai UTS kimia siswa: "))
                        nilai_kimia_uas = int(input("Masukkan nilai UAS kimia siswa: ")) 
                        nilai_biologi_uts = int(input("Masukkan nilai UTS biologi siswa: "))
                        nilai_biologi_uas = int(input("Masukkan nilai UAS biologi siswa: "))
                        nilai_bahasa_indonesia_uts= int(input("Masukkan nilai UTS bahasa indonesia siswa: "))
                        nilai_bahasa_indonesia_uas= int(input("Masukkan nilai UAS bahasa indonesia siswa: "))
                        nilai_bahasa_inggris_uts = int(input("Masukkan nilai UTS bahasa inggris siswa: "))
                        nilai_bahasa_inggris_uas = int(input("Masukkan nilai UAS bahasa inggris siswa: "))
                        nilai_matematika_uts= int(input("Masukkan nilai UTS matematika siswa: "))
                        nilai_matematika_uas= int(input("Masukkan nilai UAS matematika siswa: "))
                    except ValueError:
                        print(f"{Fore.RED}Nilai hanya bisa berupa bilangan bulat")    
                    else:
                        simpan_data = input("Apakah anda yakin ingin menyimpan data ini\nKetik 'ya' untuk menyimpan: ")
                        if simpan_data != "ya":
                            print(f"{Fore.YELLOW}Data siswa tidak tersimpan")
                            break
                        
                        nilai_uts_ipa.append({
                                            "id_siswa": id_siswa_baru,
                                            "Nama": nama_siswa_baru,
                                            "L/P": jenis_kelamin_siswa_baru,
                                            "Fisika": nilai_fisika_uts,
                                            "Kimia": nilai_kimia_uts,
                                            "Biologi": nilai_biologi_uts,
                                            "Bahasa Indonesia": nilai_bahasa_indonesia_uts,
                                            "Bahasa Inggris": nilai_bahasa_inggris_uts,
                                            "Matematika": nilai_matematika_uts
                        })
                        nilai_uas_ipa.append({
                                            "id_siswa": id_siswa_baru,
                                            "Nama": nama_siswa_baru,
                                            "L/P": jenis_kelamin_siswa_baru,
                                            "Fisika": nilai_fisika_uas,
                                            "Kimia": nilai_kimia_uas,
                                            "Biologi": nilai_biologi_uas,
                                            "Bahasa Indonesia": nilai_bahasa_indonesia_uas,
                                            "Bahasa Inggris": nilai_bahasa_inggris_uas,
                                            "Matematika": nilai_matematika_uas
                        })
                        for data_uts, data_uas in zip(nilai_uts_ipa, nilai_uas_ipa):
                            nilai_final_siswa = nilai_akhir(data_uts,data_uas)
                            row = {"id_siswa": data_uts["id_siswa"], "Nama": data_uts["Nama"], "L/P":data_uts["L/P"]}

                        # Mengupdate data nilai ipa dengan data yang baru ditambah
                        for mapel in data_uts.keys():
                            if mapel not in ["id_siswa", "Nama", "L/P"]:
                                row[f"{mapel}"] = (f"{data_uts[mapel]},{data_uas[mapel]},{round(nilai_final_siswa[mapel])}")

                        nilai_gabungan_ipa.append(row)
                        print(f"{Fore.GREEN}\nData nilai siswa berhasil disimpan\n")
                        print(f"Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_siswa_baru}")
                        print(tabulate(nilai_gabungan_ipa, headers = "keys", tablefmt = "grid" , showindex = False))

                        # Digit terakhir ID siswa + 1 tergantung kelasnya
                        if kelas_siswa_baru == "ips":
                            id_siswa_ips_terakhir_tambah_satu += 1
                        else:
                            id_siswa_ipa_terakhir_tambah_satu += 1
                        break
            tambah_siswa_lagi = input("Apakah anda ingin menambah data nilai siswa lagi?\nKetik 'ya' untuk menambah data :")
            if tambah_siswa_lagi != "ya":
                break
            
        except ValueError as error:
            print (f"{Fore.RED}terjadi kesalahan {error}")

def menghapus_data_nilai():
    
    while True:
        submenu_hapus = input('''
    Menu Hapus Data nilai
                        
    1. Hapus data nilai siswa
    2. Lihat recycle bin 
    3. Kembali ke main menu 
                        
    Ketik '1' untuk menghapus data
    Ketik '2' untuk melihat recycle bin
    Ketik sembarang untuk kembali ke main menu: ''')

        while True:   
            if submenu_hapus == "2":
                menampilkan_recycle_bin()
                break
            elif not (submenu_hapus == "1" or submenu_hapus == "2"):
                return
            try:
                kelas_data_nilai_di_hapus = input("Data kelas apa yang ingin anda hapus?\nKetik 'ips' atau 'ipa'")
                if kelas_data_nilai_di_hapus != "ips" and kelas_data_nilai_di_hapus != "ipa":
                    raise ValueError("kelas harus berupa 'ips' atau 'ipa'")
                
                if kelas_data_nilai_di_hapus == "ips":
                    print(f"=====Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_data_nilai_di_hapus}=====")
                    print(tabulate(jenis_kelas(kelas_data_nilai_di_hapus), headers = "keys", tablefmt = "grid" , showindex = False))

                else:
                    print(f"=====Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_data_nilai_di_hapus}=====")
                    print(tabulate(jenis_kelas(kelas_data_nilai_di_hapus), headers = "keys", tablefmt = "grid" , showindex = False))

                id_yg_ingin_dihapus = input("Masukkan id yg ingin dihapus")
                id_ditemukan = False #Flag untuk memeriksa keberadaan id
                for i in range(len(jenis_kelas(kelas_data_nilai_di_hapus))):
                        if id_yg_ingin_dihapus == jenis_kelas(kelas_data_nilai_di_hapus)[i]["id_siswa"]:
                            yakin_hapus = input(f'''{Fore.YELLOW}
                            Apakah anda yakin akan menghapus data nilai {jenis_kelas(kelas_data_nilai_di_hapus)[i]['Nama']}
                            Mohon perhatikan kembali data yang akan anda hapus
                            Ketik 'ya' untuk menghapus''').lower()
                            if yakin_hapus == "ya":
                                print(f"{Fore.GREEN}Data berhasil dihapus")
                                recycle_bin.append(jenis_kelas(kelas_data_nilai_di_hapus)[i])
                                del jenis_kelas(kelas_data_nilai_di_hapus)[i]
                                id_ditemukan = True #Status flag bila id ditemukan
                                break
                            else:
                                print(f"{Fore.YELLOW}ID gagal dihapus")
                                id_ditemukan = True
                                break
                                
                if not id_ditemukan:
                    raise ValueError("ID tidak ditemukan")
                    
                print(f"=====Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_data_nilai_di_hapus}=====")
                print(tabulate(jenis_kelas(kelas_data_nilai_di_hapus), headers = "keys", tablefmt = "grid" , showindex = False))
                hapus_lagi = input("adakah data nilai id lain yang ingin dihapus? ketik 'ya' untuk menghapus lagi :")
                if hapus_lagi != "ya":
                    break
            except ValueError as error:
                print(f"Terjadi kesalahan {error} ")

    
def mengubah_data():
    submenu_update = input('''
    Menu Ubah Data Nilai
                        
    1. Ubah data nilai siswa 
    2. Kembali ke main menu 
                        
    Ketik '1' untuk mengubah data
    Ketik sembarang untuk kembali ke main menu: ''')
    
    while True:
        if submenu_update != "1":
            break
        try:
            kelas_data_nilai_diubah = input("Masukkan kelas siswa\nKetik 'ipa' atau 'ips'").lower()
            if kelas_data_nilai_diubah != "ips" and kelas_data_nilai_diubah != "ipa":
                raise ValueError("Kelas harus 'ipa' atau 'ips'")
        
            
            print(f"=====Berikut daftar nilai (UTS|UAS|Akhir) kelas {kelas_data_nilai_diubah}=====\n")
            print(tabulate(jenis_kelas(kelas_data_nilai_diubah), headers = "keys", tablefmt = "grid" , showindex = False))
            id_siswa_diubah = input("Masukkan ID siswa")

            data_siswa_diubah = None
            for data_siswa in jenis_kelas(kelas_data_nilai_diubah):
                if data_siswa["id_siswa"] == id_siswa_diubah:
                    data_siswa_diubah = data_siswa

            if data_siswa_diubah:
                while True:

                    print(f"Berikut adalah data nilai {data_siswa_diubah["Nama"]}\n")
                    print(f"{'Mapel':<20} {'UTS|UAS|Akhir':<20}")
                    
                    for mapel,nilai in data_siswa_diubah.items():
                        if mapel not in ["id_siswa", "Nama", "L/P"]:
                            print(f"{mapel:<23}{nilai:<15}")
                    try:
                        nilai_mapel_diubah = input("Ketik mata pelajaran yang nilainya ingin diubah: ").title().strip()
                        if nilai_mapel_diubah not in data_siswa_diubah:
                            raise ValueError("Mapel tidak ditemukan atau ada kesalahan dalam penulisan mata pelajaran")
                    except ValueError as e:
                        print(f"{Fore.RED}Terjadi kesalahan {e}")        
                    else:
                        nilai_uts_baru = int(input(f"Masukkan nilai uts {nilai_mapel_diubah} siswa: "))
                        nilai_uas_baru = int(input(f"Masukkan nilai uas {nilai_mapel_diubah} siswa: "))
                        simpan_update_data = input("Apakah anda yakin ingin menyimpan perubahan data?\nKetik 'ya' untuk menyimpan: ")
                        if simpan_update_data != "ya":
                            print(f"{Fore.YELLOW}Perubahan gagal disimpan")
                            break           

                        for data_uts, data_uas in zip(nilai_uts_ips if kelas_data_nilai_diubah == "ips" else nilai_uts_ipa, 
                                                    nilai_uas_ips if kelas_data_nilai_diubah == "ips" else nilai_uas_ipa):
                            if data_uts["id_siswa"] == id_siswa_diubah:
                                data_uts[nilai_mapel_diubah] = nilai_uts_baru
                                data_uas[nilai_mapel_diubah] = nilai_uas_baru
                                break
                        # Ambil mata pelajaran
                        for data_siswa in jenis_kelas(kelas_data_nilai_diubah):
                            if data_siswa["id_siswa"] == id_siswa_diubah:
                                nilai_final_siswa = nilai_akhir(data_uts, data_uas)
                                data_siswa[nilai_mapel_diubah] = f"{nilai_uts_baru},{nilai_uas_baru},{round(nilai_final_siswa[nilai_mapel_diubah])}"
                                break

                        print(f"{Fore.GREEN}Perubahan data berhasil disimpan")
                        print(tabulate(jenis_kelas(kelas_data_nilai_diubah), headers = "keys", tablefmt = "grid" , showindex = False))
                        break
                ubah_lagi = input("Apakah masih ada data yang ingin diubah\nKetik 'ya' untuk mengubah: ").lower()
                if ubah_lagi != "ya":
                    break
            else:
                raise ValueError(f"{Fore.RED}ID tidak ditemukan")                      
        except ValueError as error:
                print(f"{Fore.RED}Terjadi kesalahan\n{error}")
                masih_ingin_ubah = input("Apakah masih ada data yang ingin anda ubah?\nKetik 'ya' untuk mengubah").lower()
                if masih_ingin_ubah != "ya":
                    break

login()
while True:
    main_menu = input('''
        ==== SELAMAT DATANG DI E-EDU ====
            
        Berikut adalah menu yang tersedia :             
        1. Lihat daftar nilai
        2. Tambah data nilai
        3. Hapus data nilai
        4. Ubah nilai
        5. Keluar program
                         
        Masukkan angka sesuai menu yg anda inginkan :''')
    
    if main_menu == "1":
        menampilkan_daftar_nilai()
    elif main_menu == "2":
        menambah_data_nilai()
    elif main_menu == "3":
        menghapus_data_nilai()
    elif main_menu == "4":
        mengubah_data()
    elif main_menu == "5":
        break
    else:
        print(f"{Fore.RED}Input salah")

           


        
        

    

    

