with open("mahsulot.txt", 'w') as file:
    nomi = input("Mahsulot nomi: ").title()
    narx = int(input("Mahsulot narxi: "))
    miqdori = int(input("Mahsulot miqdori: "))
    file.write(f"Mahsulot nomi: {nomi}\n")
    file.write(f"Mahsulot narxi: {narx}\n")
    file.write(f"Mahsulot miqdori: {miqdori}\n")