print('Eae pessoa')

jogar = input('Você quer jogar um jogo valendo 1 Milhão de Reais? ')

if jogar.lower() != 'sim':
    print('Vai la então quebrado')
    quit()

print('Bora jogar então')
score = 0
input('Precione Enter para começar')

resposta = input('Qual é o triângulo que tem todos os lados diferentes? \n \n Letra a: Equilátero        Letra b: Isóceles \n Letra c: Escaleno          Letra d: Trapézio \n \n')
if resposta.lower() == 'c':
    print('Ai sim! Acertou :)')
    score += 300000
else:
    print('Essa dai nem eu lembrava :(, plausível')

input('Enter para a próxima pergunta ')

resposta = input('Seguindo a sequência do baralho, qual carta vem depois do dez? \n \n Letra a: Ás         Letra b: Valete \n Letra c: Rei         Letra d: Nove \n \n')
if resposta.lower() == 'a':
    print('Boa! Acertou a mais fácil :)')
    score += 100000
else:
    print('Conseguiu errar a mais fácil :(')

input('Aperta Enter de novo ai ')

resposta = input('Quantas letras tem a escrita da bandeira nacional brasileira? \n \n Letra a: 14         Letra b: 13 \n Letra c: 15        Letra d: 16 \n \n')
if resposta.lower() == 'd':
    print('Parábens, conseguiu essa)')
    score += 250000
else:
    print('vish, foi quase po :(')

input('Agora a mais difícil em, a pergunta valendo 1 milhão de reais. Só mais um Enter ')

resposta = input('Quantos noves se tem de 0 a 100? \n \n Letra a: 21         Letra b: 20 \n Letra c: 18        Letra d: 19 \n \n')
if resposta.lower() == 'b':
    print('É isso meu felizardo, zerou o joguinho :)')
    score += 350000 
else:
    print('Errou a última, tadinho de você :(')

print('Parabéns você ganhou R$' + str(score) + ' no pix')




