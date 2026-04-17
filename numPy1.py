#Exercício_1:
import numpy as np

a = np.arange(1, 11)
print(a)              # [1 2 3 4 5 6 7 8 9 10]
print(a.shape)        # (10,)
print(a[::-2])        # [10 8 6 4 2]
print(a[::-1])        # [10 9 8 7 6 5 4 3 2 1]
print(a.sum())        # 55
print(a.mean())       # 5.5
print(a[a > 5])       # [6 7 8 9 10]
print(a[a % 3 == 0])  # [3 6 9]

#Exercício_2:
import numpy as np

notas = np.array([7.5, 6.0, 8.5, 7.0])

#Média 
print(notas.mean())

#Maior e menor
print(notas.max(), notas.min())

#Acima da média
print(len(notas[notas > notas.mean()]))

#Arredondar
print(np.round(notas))


#Exercício_3:
import numpy as np

#Preços
precos = np.array([19.90, 35.50, 42.00, 8.90, 120.00, 55.00])

#Desconto
novos = precos * 0.85
print(novos)

#Maior que R$30
print(novos[novos > 30])

#Total
print(novos.sum())


#Exercício_4:
import numpy as np

temperaturas = np.array([22, 25, 19, 30, 28, 21])

media = temperaturas.mean()
print("Media:", media)

acima_media = temperaturas[temperaturas > media]
print("Acima da media:", acima_media)

# Converter Celsius para Fahrenheit
fahrenheit = temperaturas * 9/5 + 32
print("Em Fahrenheit:", fahrenheit)

