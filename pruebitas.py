lista = ['animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 
          'sport', 'travel']

lista_diccionario = []
num = 1
for i in lista:
    lista_diccionario.append({'clave':num, 'valor':i})
    num += 1

print(lista_diccionario)

for diccionario in lista_diccionario:
    print(f'{diccionario['clave']} - {diccionario['valor']}')

seleccion = int(input('Seleccione un numero para categoria: '))

for diccionario in lista_diccionario:
    if diccionario['clave'] == seleccion:
        print(f'tu seleccion fue {diccionario['valor']}')
