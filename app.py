import os

restaurantes = [
    {'nome': 'Bife sujo', 'categoria': 'prato-feito', 'ativo': True},
    {'nome': 'Saco de feijao', 'categoria': 'feijoada', 'ativo': False},
    {'nome': 'Pé de banha', 'categoria': 'pastelaria', 'ativo': True}
]

def finalizar_app():
    #docstring
    '''
    Esta função é responsavel pela finalização do aplicativo
    '''
    os.system("clear")
    os.system("cls")
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")

def mostrar_subtitulo(texto):
    #docstring
    '''
    Essa função está disposta por exibir o subtitulo
    '''
    os.system("clear")
    print(texto)
    print()

def escolher_opcoes():
    mostrar_subtitulo("Programa Expresso\n")
    print("1 - Cadastrar restaurante")
    print("2 - Listar restaurante")
    print("3 - Ativar restaurante")
    print("4 - Sair\n")

def opcao_invalida():
    #docstring
    '''
    Essa função esta disposta pra demostrar que a opção está invalida
    '''
    mostrar_subtitulo("Opção inválida\n")
    voltar_menu_principal()

def chamar_nome_do_app():
    print("'ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖 𝔼𝕩𝕡𝕣𝕖𝕤'")

def listarRestaurantes():
    mostrar_subtitulo('Listando os Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'-{nome_restaurante}--{categoria}--{ativo}')

def alternar_estado_restaurante():
    mostrar_subtitulo("Alterando o estado do restaurante")

    nome_restaurante=input("Digite o nome do restaurante que dejesas alterar")
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['ativo']=not restaurante['ativo']
            mensagem=f'O restaruante {nome_restaurante} foi ativado ocm sucesso'if restaurante['ativo'] else f'O restaurente{nome_restaurante}foi desativado'
            print(mensagem)
        
        
    if not restaurante_encontrado:
            print('O restaurante não foi encontrado')

            voltar_menu_principal()

def cadastrar_novo_restaurante():
    #docstring

    '''
    Essa função é responsavel pelo cadastro um novo restauratnte

    imput:
    -nome do restaurantes
    -Categoria
    Outputs:
    -Adicionar um novo restaurante a lista de restaurantes
    '''
    nome_do_restaurante = input("Digite o nome do novo restaurante: ")
    categoria = input(f'Digite a categoria do restaurante{nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f"Você cadastrou o restaurante: {nome_do_restaurante}")


def main():
    #docstritng
    while True:
        try:
            escolher_opcoes()
            #dogstring
            opcaodigitada = int(input("Digite a opção desejada: "))
            if opcaodigitada == 1:
                print("Você escolheu cadastrar restaurante\n")
                cadastrar_novo_restaurante()
                main()
            elif opcaodigitada == 2:
                #dogstring
                '''
                Esta função demostra a lista de restaurantes arquivados
                '''
                listarRestaurantes()
                voltar_menu_principal()
                main()
            elif opcaodigitada == 3:
                #print("Você escolheu ativar restaurante\n")
                #dogstring
                '''
                Esta função é responsavel por ativar ou desativar um restaurante
                '''
                alternar_estado_restaurante()
                main()
            elif opcaodigitada == 4:
                print("Você escolheu sair do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
                main()
        except ValueError:
            print("Por favor, digite um número.")
            main()

if __name__ == "__main__":
    chamar_nome_do_app()
    main()