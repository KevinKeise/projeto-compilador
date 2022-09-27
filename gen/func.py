def le_arquivo(nome):
    with open(nome) as file:
        data = file.read()
        file.close()
        return data


def escreve_arquivo(str):
    with open("finalgrammar.j","w") as file:
        file.write(str)

