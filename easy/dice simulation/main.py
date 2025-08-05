# memasukan library ke dalam kode program
import random

# meletakan jawaban user di variabel input-user
input_user = input(str("Apakah kamu akan melempar dadu? (y/n) =  "))

# membuat fungsi simulasi dadu
def simulasi_dadu(min, max):
    if input_user == 'y':
        print(f"Sudah terlempar, kamu mendapat angka {random.randint(min, max)} Selamat !!!")
    elif input_user == 'n':
        print("Sudah berakhir ternyata..")
    else:
        print("Jawab yang bener dong.. y atau n, gimana sih..")

# memanggil fungsi agar bekerja           
simulasi_dadu(1, 7)              

