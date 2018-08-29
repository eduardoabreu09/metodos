def f(x):
    x**3 - 9*x + 3

def false_pos(f, a, b, epsilon, maxIter = 50):
    """Executa o método da Posição Falsa para achar o zero de f no intervalo 
       [a,b] com precisão epsilon. O método executa no máximo maxIter
       iterações.
       Retorna uma tupla (houveErro, raiz), onde houveErro é booleano.
    """
    ## Inicializar as variáveis Fa e Fb
    Fa = f(a)
    Fb = f(b)
    x= ((a*Fb) - (b*Fa))/(Fb-Fa)
    ## Teste para saber se a função muda de sinal. Se não mudar, mostrar
    
    if Fa*Fb>0:
        print("Erro! A função não muda de sinal.")
        return (True, None)
    
    ## Inicializa o tamanho do intervalo intervX usando a função abs
    intervX = abs(a-b)
    
    ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
    if intervX <= epsilon:
        return x
        
    
    ## Testes se raiz está nos extremos dos intervalos
    
    ## Teste se a é raiz, se for, retorna o próprio a sem erros
    if Fa==0:
        return a
    
    ## Teste se b é raiz, se for, retorna o próprio b sem erros
    if Fb==0:
        return b
    
    ## Mostra na tela cabeçalho da tabela
    print("k\t  a\t\t  Fa\t\t  b\t\t  Fb\t\t  x\t\t  Fx\t\tintervX")
    
    ## Iniciliza o k, dessa vez usaremos um for
    k=1
    for k in range(1, maxIter+1):
        ## Calcula x, Fx
        x= ((a*Fb) - (b*Fa))/(Fb-Fa)
        Fx=f(x)
        
        ## Mostra valores na tela
        print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e"%(k,a, Fa, b, Fb, x, Fx, intervX))
        
        ## Teste do critério de parada módulo da função
        if Fx<= epsilon:
            return x
        
        ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
        ## as variáveis apropriadamente
        
        if Fa * Fx >0:
            a = x
            Fa = Fx
        else:
            b = x
            Fb = Fx
        
        ## Atualiza intervX e checa o outro critério de parada: tamanho do intervalo
        intervX = abs(a-b)
        if intervX <= epsilon:
            return x
       
    ## Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
    print("ERRO! número máximo de iterações atingido.")
    return (True, x)
    

