file_path = '3uzd.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    if len(lines) >= 3:
        print(lines[2])
    else:
        print("Failā nav pietiekami daudz rindu.")