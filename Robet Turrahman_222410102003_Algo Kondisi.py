angka = int(input("Angka: "))

if(angka %2==0) and (angka<10):
    print(angka,"adalah angka genap dan termasuk dalam nilai kecil")
elif(angka %2!=0) and (angka<10):
    print(angka,"adalah angka ganjil dan termasuk dalam nilai kecil")

elif(angka %2==0) and (angka>=10 and angka <=50):
    print(angka,"adalah angka genap dan termasuk dalam nilai sedang")
elif(angka %2!=0) and (angka>=10 and angka <=50):
    print(angka,"adalah angka ganjil dan termasuk dalam nilai sedang")

elif(angka %2==0) and (angka>50):
    print(angka,"adalah angka genap dan termasuk dalam nilai besar")
elif(angka %2!=0) and (angka>50):
    print(angka,"adalah angka ganjil dan termasuk dalam nilai besar")
    