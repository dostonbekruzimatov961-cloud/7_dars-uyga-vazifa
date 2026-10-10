with open("talabalar.txt", 'a') as file:
    ism = input("Ismni kiriting: ").title()
    file.write(f"Talaba: {ism}\n")