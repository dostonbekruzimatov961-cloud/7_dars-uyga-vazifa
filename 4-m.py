with open("talabalar.txt", 'w') as file:
    n = int(input())
    for talabalar in range(n):
        ism = input().title()
        file.write(f"Talaba: {ism}\n")