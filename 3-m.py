with open("avtomobil.txt", 'w') as file:
    marka = input("Mashina markasini kiriting: ").title()
    yil = int(input("Mashina yilini kiriting: "))
    narx = int(input("Mashina narxini kiriting: "))
    file.write(f"Marka: {marka}\n")
    file.write(f"Yil: {yil}\n")
    file.write(f"Narx: {narx}\n")