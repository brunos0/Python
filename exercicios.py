"""
Programa de teste para Python
"""
#testar em casa
#lista = input("Digite 4 notas, separadas por virgulas")
# nome = 'Bruno'
# sobrenome = 'Horvat'
# #print("o nome é", nome, "e o sobrenome e",sobrenome)
# #print("o nome é {} e o sobrenome e {}" .format(nome, sobrenome))
# #print(f"O nome é {nome} e o sobrenome e {sobrenome} ")
# # print(" teste { } ")5
# #val1 = '1'
# #val2 = '2'
# #print( eval(val1) + eval(val2) )  # macro execução]
lista = ['Corinthians', [1, 2, 3, 4, 5] ,'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']
# #print 3, 13, vasco
# print(lista[1][2],lista[4][3],lista[6])
# print(lista[1][-2])
# print(lista.index("Palmeiras"))
# print(lista.index("Corinthians"))
print(lista[0:40])
print(lista[lista.index("Corinthians"):lista.index("Palmeiras")+1])

# lista.append('Bragantino')      # vai pro final
# lista.insert(0,'Santos')        # vai pro começo

print(lista)

try:
    lista.remove('Vasce') # retira o Vasco:
except Exception:  
    print("erro ao remover Vasce")
#except ValueError:  
#    print("erro ao remover Vasce")

print(lista)

