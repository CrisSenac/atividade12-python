nome = input('Digite o nome: ')
idade = int(input('Qual a sua idade? '))

dorIntensa = input("Sente dor intensa? (SIM/NÃO) ").strip().upper()
dificuldadeRespiratoria = input("Tem dificuldade respiratória? (SIM/NÃO) ").strip().upper()
fraturaVisivel = input("Tem alguma fratura visível? (SIM/NÃO) ").strip().upper()
sangramento = input("Está com sangramento? (SIM/NÃO) ").strip().upper()
febreAlta = input("Teve febre alta persistente? (SIM/NÃO) ").strip().upper()

if dorIntensa == "SIM" or dificuldadeRespiratoria == "SIM" or idade <= 12 or idade >= 65:
    classificacao = "Emergência"
elif fraturaVisivel == "SIM" or sangramento == "SIM" or idade <= 12 or idade >= 65:
    classificacao = "Grave"
elif febreAlta == "SIM":
    classificacao = "Preferencial"
else:
    classificacao = "Sem urgência"


print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Classificação: {classificacao}")