with open('logo.png','rb') as file:
    with open('copy2.png','wb') as file2:
        file2.write(file.read())