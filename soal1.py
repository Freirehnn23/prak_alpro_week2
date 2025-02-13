berat = float(input('Masukan BMI yang diinginkan: '))
tinggi = int(input("Masukan tinggi badan anda saat ini dalam cm: "))
konvert_tinggi = tinggi / 100
bmi = berat * (konvert_tinggi ** 2)

print(f"berat badan yang diperlukan untuk mencapai BMI {berat} adalah: {bmi:.2f}") 

