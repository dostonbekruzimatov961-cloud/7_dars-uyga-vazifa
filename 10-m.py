with open("xodimlar.txt", 'a') as file:
    xodim = input().title()
    file.write(f"Xodim: {xodim}\n")