agenda = {}

def adicionar_contato():
    nome_contato = input("Digite o nome do contato: ")
    telefone_contato = input("Digite o número de telefone do contato: ")
    email_contato = input("Digite o e-mail do contato: ")
    agenda[nome_contato] = {"Telefone": telefone_contato, "E-mail": email_contato}
    print("\033[1;31;42m Contato adicionado!\033[m")

def buscar_contato():
    add_busca = input("Digite o nome, telefone ou email do contato: ")
    resultados = []
    for nome, contato in agenda.items():
        if add_busca.lower() in nome.lower() or add_busca in contato["Telefone"] or add_busca.lower() in contato["E-mail"].lower():
            resultados.append((nome, contato))
    if len(resultados) > 0:
        print("\033[4;31;42m contato encontrado:\033[m")
        for nome, contato in resultados:
            print(f"\033[1;31;40m Nome: {nome}, Telefone: {contato['Telefone']}, E-mail: {contato['E-mail']} \033[m")
    else:
        print("\033[1;32;41m Nenhum contato encontrado!\033[m")

def listar_contatos():
    if len(agenda) > 0:
        print("Lista de contatos:")
        if len(agenda) > 0:
            print("\033[4;33;40m Somente esse(s) contato(s) esta(ão) na sua agenda: \033[m")
            for nome, contato in agenda.items():
                print(f"\033[1;31;40m Nome: {nome}, Telefone: {contato['Telefone']}, E-mail: {contato['E-mail']} \033[m")
    else:
        print("\033[1;32;41m A lista de contatos está vazia! \033[m")

def remover_contato():
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in agenda:
        del agenda[nome]
        print("\033[1;31;42m Contato foi removido com sucesso! \033[m")
    else:
        print("\033[1;32;41m Contato não encontrado! \033[m")

def menu():
    print("=-=-=-=-Agenda Telefônica-=-=-=-=")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar contatos")
    print("4 - Remover contato")
    print("5 - Sair")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    opcao = input("Digite o número para ir a opção desejada: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        buscar_contato()
    elif opcao == "3":
        listar_contatos()
    elif opcao == "4":
        remover_contato()
    elif opcao == "5":
        print("\033[1;35;40m programa encerrado! \033[m")
        return
    else:
        print("\033[1;32;41m Opção inválida! \033[m")

    print("\n")
    menu()

menu()
