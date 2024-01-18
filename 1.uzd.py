#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu

file_path = '1uzd.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    saturs = file.read()
    print(saturs)
