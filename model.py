import requests as consulta 


class ModelApi:
    def __init__(self):
        self.categoria = None
        self.jokes = None
        self.lista_categoria = []
        self.lista_categoria_dict = []

    def consulta_categoria(self):
        self.categoria = consulta.get('https://api.chucknorris.io/jokes/categories')
        self.lista_categorias = self.categoria.json()


    def consulta_jokes(self, categoria_seleccionada):
        self.jokes = consulta.get(f'https://api.chucknorris.io/jokes/random?category={categoria_seleccionada}')

    def crear_diccionario_categoria(self):
        num = 0 
        for i in self.lista_categoria:
            num += 1
            self.lista_categoria_dict.append({'clave':num, 'valor': i})