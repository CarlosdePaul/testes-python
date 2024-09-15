#nome="Carlos"
#idade=18
#cidade="Várzea Grande"
#estado="Mato grosso"
#print(nome,idade,estado,cidade)

#nome=input("Qual seu nome?")
#altura=input("Qual sua altura?")
#print(nome,altura)

#nome=input("Digite seu nome:")
#print("Olá Carlos seja bem vindo")

#dia=input("Digite o dia do seu aniversário:")
#mês=input("Digite o mês do seu aniversário:")
#ano=input("DIgite o ano do seu aniversário:")
#print("Você nasceu no dia 01 de abril de 2006?")

#primeiroNumero=input("primeiro número:")
#segundoNumero=input("segundo número:")
#print(primeiroNumero+segundoNumero)

#exercícios Fahim 5
#valor=23
#resto=valor//3
#print("O resto é:",resto)

#Exercícios Fahim 6
#função divmod() serve para obter o quociente e resto da divisão 
#valor=31
#quociente=valor//3
#print("O quociente de 31/3 é:",quociente)

#Exercícios fahim 7
#valora=input("Digite primeiro valor:")
#valorb=input("Digite segundo valor:")
#valorestrocados=valora.replace("Digite segundo valor:")
#print(valorestrocados)

   #Exercícios Fahim 8
#horastrabalhadas=input("Digite a quantidade de horas trabalhadas:")
#hora=input("entre com o valor da hora: ")
#salario=horastrabalhadas * hora
#print("O salário bruto é:",salario)

#exercício de sala errado
#nota1=7
#nota2=6
#nota3=4
#nota4=5
#boletim_final=nota1+nota2+nota3+nota4/5
#print("Média:",nota1+nota2+nota3+nota4/5)
 #if (boletim_final>7):
 #print("Passou direto")
 #else 
 #if(boletim_final<4)
# print("Reprovado")
 #else
 #if(boletim_final>=4),(boletim_final ,7)
#print("Prova")

  #exercício de sala corrigido
#nota1 = 7
#nota2 = 6
#nota3 = 4
#nota4 = 5

#boletim_final = (nota1 + nota2 + nota3 + nota4) / 4
#print("Média:", boletim_final)

#if boletim_final > 7:
    #print("Passou direto")
#elif boletim_final < 4:
    #print("Reprovado")
#elif 4 <= boletim_final <= 7:
    #print("Prova final")
 
 #Exercício lista 2

#tempo=float(input("Digite o tempo da viagem:"))
#velocidade=float(input("Digite a velocidade média:"))
#distancia=tempo*velocidade
#print("A distancia é:",distancia)

#litros_usados=distancia/12
#print("A quantidade de litros usados foi:",litros_usados)


#raio=float(input("Digite o raio:"))
#altura=float(input("Digite a altura:"))
#volume_lata_oleo=314159*raio**2*altura
#print("O volume da lata de óleo é:",volume_lata_oleo)
# precisa converter essas strings em números (inteiros ou floats) antes de realizar operações matemáticas.

#nome=input("Digite seu nome:")
#print("Seja bem vindo,",nome)
#numero1=int(input("Digite um número:"))          #A soma não da certo pois o código entende que os números são strings(texto)
#numero2=int(input("Digite um segundo número:")) #para somar direito precisa colocar "int" de número inteiro antes do input pra funcionar
#soma=numero1+numero2
#print("A soma entre 6 e 2 é:",soma)

#n1=int(input("DIgite primeiro valor:"))
#n2=int(input("Digite segundo valor:"))
#multiplicação=n1%n2
#print(multiplicação)

#n= int(input("Digite número:"))
#antecessor=n-1
#sucessor=n+1
#print(f"seu antecessor é {n-1} e seu sucessor {n+1}")

#n=int (input("Digite um número:"))
#print(f"O dobro de {n} é {n*2} \no triplo é {n*3} \ne raiz quadrada é {n**(1/2)}")

#ntaluno=float(input("Primeira nota:"))
#ntaluno_dois=float(input("segunda nota"))
#print(f"A média do aluno foi {(ntaluno + ntaluno_dois )/5} ")  #números em parenteses serão resolvidos primeiros

#metro=float(input("Digite um metro:"))
#print(f"{metro} convertido em km é {metro*0.001}\nconvertido em hectômetros é {metro*0.01}\nconvertido em decamêtro {metro*0.1}\nconvertido em decímetros {metro*metro*10}\nconvertido em centímetros {metro*100}\nconvertido em milímetros {metro*1000}")
#medida= float(input("Digite uma distância em metros:"))
#cm= medida * 100
#mm= medida * 1000
#dm= medida * 0.1
#print(f"a {medida} convertida em cm é {cm} \n , em mm é {mm} e em decâmetro {dm}")

       #atividades Fahim 3
#1-
#n1=int(input("Digite primeiro valor"))
#n2=int(input("Digite segundo valor:"))
#n3=int(input("DIgite terceiro valor:"))
#if n1>n2 and n1>n3:
    # maior=n1
#elif n2>n3:
     #maior=n2
#else:
    # maior=n3

#if n1<n2 and n1<n3:
     #menor=n1
#elif n2<n3:
    # menor=n2
#else:
     #menor=n3
#print("O maior será",maior)
#print("O menor será",menor)

#2
#valor1=int(input("Primeiro valor:"))
#valor2=int(input("Segundo valor:"))
 #if valor1/valor2:
  #resto=

#4
#valor=int(input("Digite um valor:"))
#valor2=int(input("Digite segundo valor:"))
#print(f"Os valores digitados são {valor} e {valor2}")
#valor=int(input("Digite valor:"))
#resto=valor%3
#print("o resto é:",resto)

#valora=int(input("DIgite valor 1:"))
#valorb=int(input("Digite valor 2:"))
#auxilio=valora
#valora=valorb
#valorb=auxilio
#print("Os valores trocados",valora,valorb)

#horas_trabalhadas=float(input("Quantidade de horas trabalhadas:"))
#valor_hora=float(input("Valor trabalho:"))
#salario_bruto=horas_trabalhadas*valor_hora
#print("O salário bruto será:",salario_bruto)

#tm=float(input("DIgite o tempo da viagem:"))
#velocidade=int(input("DIgite a velocidade:"))
#distancia=tm*velocidade
#litros_usados=distancia/12
#print("A quantidade de litros usados foi:",litros_usados)

#nota1=float(input("primeira nota:"))
#nota2=float(input("Segunda nota:"))
#nota3=float(input("terceira nota:"))
#nota4=float(input("quarta nota:"))
#print(f"A média do aluno é {(nota1+nota2+nota3+nota4)/4}")
#media=float(input("DIgite a nota:"))
#if media>=7:
    #print("Aprovado")
#else:
  #if media <4:
     #print("reprovado")
#numero=int(input("Digite um número para ver sua tabuada:"))
#print(f"{numero}/{1:2}={numero/1}")
#print(f"{numero}/{2:2}={numero/2}")
#print(f"{numero}/{3:2}={numero/3}")
#print(f"{numero}/{4:2}={numero/4}")
#print(f"{numero}/{5:2}={numero/5}")
#print(f"{numero}/{6:2}={numero/6}")
#print(f"{numero}/{7:2}={numero/7}")
#print(f"{numero}/{8:2}={numero/8}")
#print(f"{numero}/{9:2}={numero/9}")
#print(f"{numero}/{10:2}={numero/10}")

#valor_prestação=float(input("Digite o valor da prestação:"))
#valor_taxa=float(input("Digite o valor da taxa:"))
#tempo=float(input("Digite o tempo:"))
#valor_a_ser_pago=valor_prestação+(valor_prestação*(valor_taxa/100)*tempo)
#print("O valor a ser pago é:",valor_a_ser_pago)

#reais=float(input("Quanto dinheiro você tem na carteira? R$"))
#dolar=reais / 5.66
#print(f"Com R${reais:2f} você pode comprar U${dolar:2f}")

#largura=float(input("Largura da parede:"))
#altura=float(input("Altura da parede:"))
#print(f"Sua parede tem dimensão de {largura}x{altura} e sua área é de {largura*altura}m²")
#print(f"A quamtidade de tinta usada será de {(largura*altura)/2}l")

#preço=float(input("Qual o preço do produtro?"))
#print(f"O produto que custava R${preço:2f} com o desconto de 5% agora passa a custar R${preço-(preço*5/100):2f}")

#salario=float(input("Salário do funcionário R$:"))
#print(f"O salário do funcionário com aumento de 15% é R${salario+(salario*15/100):2f}")
#graus=int(input("Quantos graus tem?C "))
#print("Está fazendo ",graus)
#fahrenheit=(graus * 9/5) +32
#print(f"A quantidade {graus}C convertido em Fahrenheit é {fahrenheit}F")

#dias=int (input("Quantidade de dias usando carro:"))
#km=float(input("Quilômetros rodados:"))
#km_preço=km * 0.15
#dias_usados=dias*60
#print(f"O total a pagar é {km_preço+dias_usados}")

