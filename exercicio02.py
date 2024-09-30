print("Nesse jogo cada pergunta correta vale 2 pontos. Cada pergunta tem 4 opções e respostas, bom jogo.\n")
 
# Inicializando a pontuação
pontos = 0
 
print("Qual é o maior planeta do sistema solar?")
print("A) Terra\nB) Marte\nC) Júpiter\nD) Vênus")
resposta1 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta1 == "C" or resposta1 == "c":
    pontos += 2
    print("Parabéns, você acertou a primeira pergunta. Você somou 2 pontos.")
else:
    print("Sinto muito, você errou a pergunta.")
 
print("\n")
 
print("Qual animal é conhecido por mudar de cor?")
print("A) Elefante\nB) Camaleão\nC) Canguru\nD) Pinguim")
resposta2 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta2 == "B" or resposta2 == "b":
    pontos += 2
    print("Parabéns, você acertou a segunda pergunta. Você somou 2 pontos.")
else:
    print("Sinto muito, você errou a pergunta.")
 
print("\n")
 
print("Qual é a capital da França?")
print("A) Roma\nB) Paris\nC) Londres\nD) Madrid")
resposta3 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta3 == "B" or resposta3 == "b":
    pontos += 2
    print("Parabéns, você acertou a terceira pergunta. Você somou 2 pontos.")
else:
    print("Sinto muito, você errou a pergunta.")
 
print("\n")
 
print("Qual elemento químico tem o símbolo O?")
print("A) Ouro\nB) Oxigênio\nC) Hidrogênio\nD) Carbono")
resposta4 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta4 == "B" or resposta4 == "b":
    pontos += 2
    print("Parabéns, você acertou a quarta pergunta. Você somou 2 pontos.")
else:
    print("Sinto muito, você errou a pergunta.")
 
print("\n")
 
print("Em que continente fica o Egito?")
print("A) Ásia\nB) Europa\nC) América\nD) África")
resposta5 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta5 == "D" or resposta5 == "d":
    pontos += 2
    print("Parabéns, você acertou a quinta pergunta. Você somou 2 pontos.")
else:
    print("Sinto muito, você errou a pergunta.")
 
print("\n")
 
print("Pergunta bônus. É tudo ou nada \n")
 
 
print("Quantas letras existem no alfabeto Brasileiro?")
print("A) 19\nB) 26\nC) 25\nD) 27")
resposta6 = input("Qual opção é a correta? : ")
print("\n")
 
if resposta6 == "B" or resposta6 == "b":
    pontos += 3
    print("Parabéns, você acertou a pergunta bônus. Você somou 3 pontos.")
elif resposta6 != "B" or resposta6 != "b":
    pontos -= 3
    print("Você errou a pergunta bônus, você perdeu três pontos")
print("\n")
 
 
 
 
# Exibindo a pontuação final
print(f"Sua pontuação final é: {pontos} pontos.")