with open("talaba.txt", 'w') as file:
    ism = input("Talaba ismi: ").title()
    yosh = int(input("Talaba yili: "))
    ball = int(input("Talaba balli: "))
    file.write(f"ism: {ism}\n")
    file.write(f"yosh: {yosh}\n")
    file.write(f"ball: {ball}\n")