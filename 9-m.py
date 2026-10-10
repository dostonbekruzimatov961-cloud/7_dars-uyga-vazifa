with open("xodimlar.txt", 'w') as file:
    n = int(input())
    for xodimlar in range(n):
        xodim = input().title()
        file.write(f"Xodim: {xodim}\n")