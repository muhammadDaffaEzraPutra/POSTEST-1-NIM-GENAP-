## Konversi berat  (pounds (lb), ounce (ons), gram (g) )
#Nama : Muhammad Daffa Ezra Putra
#Nim : 2309116052
#Sistem informasi kelas B




#login
x : input("masukkan nama kalian : ")
y : input("masukkan NIM : ")
z : input("masukkan kelas : ")

#opsi operasi
print("\nPilih operasi:")       
print("1. lbs")
print("2. ons")
print("3. g")

#input operasi
pilihan = input("Pilih Operasi (1/2/3) ")


#input angka memakai koma
kg = float(input("Masukan Berat dalam KG : "))

#jika input sesuai opsi maka hasil yang keluar sesuai opsi
if pilihan == "1"  :
    kg *= float(2.204623) 
    print("Hasil perkalian : ", kg, "Lbs") 
elif pilihan == "2":
    kg *= float(35.274) 
    print("Hasil perkalian : ", kg, "ons") 
elif pilihan == "3"  :
    kg*= float(1000) 
    print("Hasil perkalian : ", kg, "g")
