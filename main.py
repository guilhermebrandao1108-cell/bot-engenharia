# Importar a classe principal do SeleniumBase
from seleniumbase import SB

# Iniciar o robô
with SB() as sb:
    # Guarda o endereço
    url = "https://www.saucedemo.com/"
    # Abre o site
    sb.open(url)
    # 1. Acesso ao Site 
    #prenenche o nome do usuário
    sb.type("#user-name", "standard_user")
    #digita a senha
    sb.type("#password", "secret_sauce")
    #clica no botão de login
    sb.click("#login-button")

    
    # 2.Coleta de Dados 
    #cria a lista com os nomes e preços dos produtos
    nomes = sb.find_elements(".inventory_item_name")
    precos = sb.find_elements(".inventory_item_price")
    descricao = sb.find_elements(".inventory_item_desc")
    
    # Exibe a quantidade de produtos encontrados
    print(f"{len(nomes)}")

    #cria uma lista fazia para guardar o catálogo
    catalogo = []

    # O range cria um contador: 0, 1, 2, 3, 4, 5...
    for i in range(len(nomes)):
        # Pega o texto do nome número 'i'
        texto_nome = nomes[i].text
        # Pega o texto do preço número 'i'
        texto_preco = precos[i].text
        # Pega o textoda descrição número 'i
        texto_descricao = descricao[i].text
        # prepara o dicionário do produto atual
        produto_atual = {"nome": texto_nome, "valor": texto_preco, "descricao": texto_descricao}
        # Adiciona esse dicionário na lista principal
        catalogo.append(produto_atual)
    

    # Exibe o catálogo completo
    print("Dados salvos na memória:")
    print(catalogo)    
  

    #3. Automação de Compra

    #Adicionar Mochila ao carrinho
    sb.click("#add-to-cart-sauce-labs-backpack")
    # Ir para o carrinho de comptras
    sb.click("shopping_cart_container")
    # Iniciar o processo de checkout
    sb.click("checkout")
    
    # Para conseguir ver o que apareceu  na tela, vamos esperar 8 segundos
    sb.sleep(8)

    