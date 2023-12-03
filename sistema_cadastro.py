produtos = []  
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar produto, preço e quantidade \n'
    '2. Remover produto, preço e quantidade \n'
    '3. Listar produtos cadastrados \n'
    '4. Sair \n')

print(menu)

while escolha != 4:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        produto = input('Informe o nome do produto a ser cadastrado: ')
        preco = float(input('Informe o preço do produto: '))
        quantidade = int(input('Informe a quantidade do produto: '))
        produtos.append((produto, preco, quantidade))  

    elif escolha == 2:
        if len(produtos) == 0:
            print('Não há produtos para remover do cadastro!')
        else:
            produto_removido = input('Informe o nome do produto que deseja remover: ')
            encontrou = False
            for produto in produtos:
                if produto[0] == produto_removido:
                    produtos.remove(produto)  
                    encontrou = True
                    print(f"O produto '{produto_removido}' foi removido com sucesso!")
                    break
            if not encontrou:
                print(f"Produto '{produto_removido}' não encontrado no cadastro.")

    elif escolha == 3:
        if len(produtos) == 0:
            print('Não há produtos cadastrados!')
        else:
            print('Produtos cadastrados:')
            for i, produto in enumerate(produtos):
                print(f"{i + 1}. Nome: {produto[0]}, Preço: {produto[1]}, Quantidade: {produto[2]}")
    elif escolha == 4:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção inválida')
