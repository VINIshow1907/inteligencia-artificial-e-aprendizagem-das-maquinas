class Produto:
    def __init__(self, idproduto, nome, marca, descricao, preco, quantidade_estoque):
        self.idproduto = idproduto
        self.nome = nome
        self.marca = marca
        self.descricao = descricao
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque

    def imprimir(self):
        print("\n--- Dados do Produto ---")
        print("ID do Produto:", self.idproduto)
        print("Nome:", self.nome)
        print("Marca:", self.marca)
        print("Descrição:", self.descricao)
        print("Preço:", self.preco)
        print("Quantidade em Estoque:", self.quantidade_estoque)

# Entrada de dados pelo usuário
idproduto = int(input("Digite o ID do produto: "))
nome = input("Digite o nome do produto: ")
marca = input("Digite a marca do produto: ")
descricao = input("Digite a descrição do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade_estoque = int(input("Digite a quantidade em estoque: "))

# Criação do objeto e chamada do método
p1 = Produto(idproduto, nome, marca, descricao, preco, quantidade_estoque)
p1.imprimir()