from typing import Dict
import json

Lista: list = ["sapato", 39, 10.38, True]

produto_01: Dict[str, any]

produto_01: Dict[str, any] = {
    "nome": "sapato",
    "quantidade": 36,
    "preco": 10.38,
    "disponivel": True
}

produto_02: dict = {
    "nome": "televião",
    "quantidade": 10,
    "preco": 70.38,
    "disponivel": False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)
print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)
