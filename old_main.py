import requests as consulta 

# https://api.chucknorris.io/jokes/categories
categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
# print('categorias: ', categorias.json())
lista_categoria = categorias.json()
# mostrat cada categoria con un numero 
lista_categoria_dict = []
num = 0 
for i in lista_categoria:
    num += 1
    lista_categoria_dict.append({'clave':num, 'valor': i})

for diccionario in lista_categoria_dict:
    print(f'{diccionario['clave']} - {diccionario['valor']}')


seleccion = int(input('Seleccione un numero para categoria: '))
categoria_seleccionada = None
for diccionario in lista_categoria_dict:
    if diccionario['clave'] == seleccion:
        categoria_seleccionada = diccionario['valor']
        # print(f'tu seleccion fue {diccionario['valor']}')


#print('ultimo dato de lista categoria:', lista_categoria[len(lista_categoria) - 1])
#response = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

#print('codigo http de respuesta: ',response.status_code)
#print('cabecera: ', response.headers['content-type'])
#print('encoding: ',response.encoding)
#print('respuesta en string: ', response.text)
#print('respuesta en json: ', response.json())