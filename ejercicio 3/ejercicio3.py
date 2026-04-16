# funció

def obtener_primero_ultimo(lista):
    # Verifica que lalista no este vacia 
    if lista:
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return 'la lista no tiene elementos suficientes agrege mas porfavor '
    else:
        return 'Dato no valido. lista vacia agrege algo para que te funcione '

# invocar funcion
lista_1 = []
resultado = obtener_primero_ultimo(lista_1)
print(resultado)