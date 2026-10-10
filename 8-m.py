with open("avtomobil.txt", 'a') as file:
    n = int(input())
    for avtomobillar in range(n):
        avto = input().title()
        file.write(f"Avtomobil: {avto}\n")