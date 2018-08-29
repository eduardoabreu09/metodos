def f(x):
     x**3 - 9*x + 3
     print(f(0))

def bissecao(f, a, b, epsilon, maxIter=50):
    

     a = 0
     b = 1
     epsilon = 0.001
     maxIter = 20


     Fa =f(a)
     Fb = f(a)

     if Fa*Fb>0:
          print("Erro! A função não muda de sinal.")
          return (True, None)


     ## Mostra na tela cabeçalho da tabela
     print("k\t  a\t\t  fa\t\t  b\t\t  fb\t\t  x\t\t  fx\t\tintervX")

     ## Inicializa tamanho do intervalo intervX usando a função abs, x e Fx
     intervX = abs(a-b)
     x = (a+b)/2
     Fx = f(x)

     ## Mostra dados de inicialização
     print("-\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (a, Fa, b, Fb, x, Fx, intervX))

     ## Teste se intervalo já é do tamanho da precisão e retorna a raiz sem erros
     if intervX >= epsilon:
          return  x


     ## Iniciliza o k
     k=1

     ## laço
     while k <= maxIter:
         ## Testes para saber se a raiz está entre a e x ou entre x e b e atualiza
         ## as variáveis apropriadamente
          if Fx==0:
               return x
     
          if Fa*Fx<0:
               b=x
               Fb=Fx
          
          elif Fb*Fx<0:
               a=x
               Fa=Fx

          intervX = abs(a-b)
          x=(a+b)/2
          Fx=f(x)

         ## Mostra valores na tela
          print("%d\t%e\t%e\t%e\t%e\t%e\t%e\t%e" % (k, a, Fa, b, Fb, x, Fx, intervX))

         ## Teste do critério de parada (usando apenas o tamanho do intervalo)

          if intervX <= epsilon:
               return(True,x)

         ## Atualiza o k
          k = k + 1
     ## Se chegar aqui é porque o número máximo de iterações foi atingido
     ## Mostrar uma mensagem de erro e retorna que houve erro e a última raiz encontrada
     print("ERRO! número máximo de iterações atingido.")
     return (True, x)










