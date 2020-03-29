try:
    with open('texte.txt', 'r') as file:
        file = file.read()
        print(file)
except FileNotFoundError:
    print('File dose not exist')