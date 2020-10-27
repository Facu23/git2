def maximo(a: int, b: int) -> int:
    mayor = a
    if a < b:
        mayor = b
    else:
        pass
    return mayor

def maximo_de_3(a: int, b: int, c: int) -> int:
    candidato = maximo(a,b)
    return maximo(candidato,c)

def largo_lista(lista: list) -> int:
    largo = 0
    for i in lista:
        largo += 1
    return largo

def vocal_o_consonante(c: str) -> str:
    vocales = ['a', 'e', 'i', 'o', 'u']
    tipo = 'consonante'
    if c in vocales:
        tipo = 'vocal'
    else:
        pass
    return f'{c} es una {tipo}.'

def sumatoria(lista: [int]) -> int:
    suma = 0
    for i in lista:
        suma += i
    return suma


def producto(lista: [int]) -> int:
    prod = 1
    for i in lista:
        prod *= i
    return prod

def elem_comun(lista1, lista2) -> str:
       resultado = []
       for element in lista1:
           if element in lista2:
               resultado.append(element)
       return resultado
    