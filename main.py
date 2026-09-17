import requests as consulta 

# https://api.chucknorris.io/jokes/categories
categorias = consulta.get('https://api.chucknorris.io/jokes/categories')
print('categorias: ', categorias.json())
lista_categoria = categorias.json()
print('ultimo dato de lista categoria:', lista_categoria[len(lista_categoria) - 1])
response = consulta.get('https://api.chucknorris.io/jokes/random?category=animal')

print('codigo http de respuesta: ',response.status_code)
print('cabecera: ', response.headers['content-type'])
print('encoding: ',response.encoding)
print('respuesta en string: ', response.text)
print('respuesta en json: ', response.json())