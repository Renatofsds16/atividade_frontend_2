from atividade_frontend_2.pessoa import Pessoa
lista = []
altura  = []
total_feminino = 0
media_altura_masculino = 0
total_feminino = 0
contador = 0
total = 0
for p in range(3):
    altura_pessoa = float(input("Digite a altura: "))
    genero = str(input("Digite o genero: "))
    pessoa = Pessoa(altura_pessoa, genero)
    lista.append(pessoa)

for pessoa in lista:
    altura.append(pessoa.altura)
    if pessoa.genero[0].upper() == "F":
        total_feminino += 1
    if pessoa.genero[0].upper() == "M":
        total += pessoa.altura
        contador += 1

media_altura_masculino = total / contador

print(f'maior altura: {max(altura)}')
print(f'memor altura: {min(altura)}')
print(f'media de altura do genero masculino: {media_altura_masculino}')
print(f'numero de pessoas do sexo Feminino: {total_feminino}')
