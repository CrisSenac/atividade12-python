x = int(input("Informe um valor para o eixo x do seu plano: "))
y = int(input("Informe um valor para o eixo y do seu plano "))
 
if x > 0 and y > 0:
    quadrante = "Primeiro quadrante"
elif x > 0 and y < 0:
    quadrante = "Segundo quadrante"
elif x < 0 and y < 0 :
    quadrante = "Terceiro quadrante"
elif x < 0 and y > 0:
    quadrante = "Quarto quadrante"
else:
    quadrante = "Pontos de origens ou no eixo"
 
distancia_ao_quadrado = (x**2 + y**2)
print(f"O ponto está no: {quadrante}")
print(f"A distância até a origem é: {distancia_ao_quadrado}")