def le_arquivo(nome):
    with open(nome) as file:
        data = file.read()
        file.close()
        return data

