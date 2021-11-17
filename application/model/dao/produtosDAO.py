from application.model.entity.produtos import Produto
import json

lista_produtos_json = []


class ProdutosDAO():
    def init(self):
        self.__lista_produtos_json = lista_produtos_json

    def dict_to_list(self, lista_prod):
        lista_produtos_json = []
        for produto_item in lista_prod:
            produto = Produto()
            produto.set_id(produto_item['id'])
            produto.set_name(produto_item['name'])
            produto.set_image(produto_item['image'])
            produto.set_oldPrice(produto_item['oldPrice'])
            produto.set_price(produto_item['price'])
            produto.set_description(produto_item['description'])
            installments = produto_item['installments']
            produto.set_count(installments['count'])
            produto.set_value(installments['value'])
            lista_produtos_json.append(produto)
        return lista_produtos_json

    def lista_produtos_json(self):
        with open('application/controller/products.json', 'r') as file:
            produto_json = json.load(file)
            lista = self.dict_to_list(produto_json)
        return lista