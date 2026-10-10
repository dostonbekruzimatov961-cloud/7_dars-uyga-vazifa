with open("mahsulotlar.txt", 'a') as file:
    mahsulot = input("Mahsulotni kiriting: ").title()
    file.write(f"Mahsulot: {mahsulot}\n")