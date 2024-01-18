file_name = input("Ievadi faila nosaukumu: ")
file_extension = input("Ievadi faila formātu (piemēram, txt, csv utt.): ")
file_path = f'{file_name}.{file_extension}'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        saturs = file.read()
        print(saturs)
except FileNotFoundError:
    print(f"Faila {file_path} nav atrasts.")
except Exception as e:
    print(f"Kļūda lasot failu: {e}")