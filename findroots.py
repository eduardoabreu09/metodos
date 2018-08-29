"""
Função que retorna um intervalo [x1,x2] entre os pontos
a e b contendo uma raiz da função f. Caso não seja
encontrada nenhuma mudança de sinal, retorna None,None.
A função recebe como entrada:
f: a expressão matemática (string) que está sendo analisada;
a: extremo esquerdo do intervalo;
b: extremo direito do intervalo;
dx: Incremento usado na busca por raízes.

César Lincoln Cavalcante Mattos - 2018
"""
def findroots(f, a, b, dx):
    x1 = a
    f1 = f(a)
    x2 = a + dx
    f2 = f(x2)

    while f1*f2 >= 0:
        if x1 >= b:
            return None,None
        x1 = x2
        f1 = f2
        x2 = x1 + dx
        f2 = f(x2)
    else:
        return x1,x2
