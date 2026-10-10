with open("mahsulotlar.txt", 'w') as file:
    n = int(input())
    for mahsulotlar in range(n):
        mahsulot = input().title()
        file.write(f"Mahsulot: {mahsulot}\n")