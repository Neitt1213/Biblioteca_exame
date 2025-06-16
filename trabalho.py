from collections import deque
from datetime import date, timedelta

Prioridade = ("Professor", "Aluno", "Funcionario", "Terceirizado")
Validos = Prioridade + ("Visitantes",)
filas_livros = {}
historico_usuarios = {}
disponibilidade_livros = {
    "O Senhor dos Anéis": True,
    "Introdução à Programação com Python": True,
    "Estruturas de Dados e Algoritmos em Python": True
}

livros_disponiveis = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "978-8595084759"),
    ("Introdução à Programação com Python", "Nilo Ney Coutinho Menezes", "978-8575227183"),
    ("Estruturas de Dados e Algoritmos em Python", "Michael T. Goodrich et al.", "978-8582604110")
]

def selecionar_tipo_usuario():
    print("\nSelecione o tipo de usuário:")
    for i, tipo in enumerate(Validos, 1):
        print(f"{i}. {tipo}")
    while True:
        escolha = input("Escolha uma opção: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(Validos):
                return Validos[escolha - 1]
        print("Opção inválida. Tente novamente.")

def selecionar_livro():
    print("\nLivros disponíveis:")
    for i, (titulo, autor, isbn) in enumerate(livros_disponiveis, 1):
        status = "Disponível" if disponibilidade_livros[titulo] else "Emprestado"
        print(f"{i}. {titulo} - {autor} (ISBN: {isbn}) [{status}]")
    while True:
        escolha = input("Escolha um livro pelo número: ")

        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(livros_disponiveis):
                return livros_disponiveis[escolha - 1][0]
        print("Opção inválida. Tente novamente.")

def pode_pegar_livro(nome):
    livros_emprestados = len(historico_usuarios[nome]["livros"])
    if livros_emprestados > 0:
        print(f"{nome} já está com o(s) livro(s): {', '.join([livro['livro'] for livro in historico_usuarios[nome]['livros']])}")
        return False
    return True

def inicializar_fila(livro):
    if livro not in filas_livros:
        filas_livros[livro] = {t: deque() for t in Validos}

def add_usuario_fila(livro, nome, tipo):
    inicializar_fila(livro)
    if nome in historico_usuarios and historico_usuarios[nome]['livros']:
        print("Usuários com livros emprestados não podem entrar na fila de espera.")
        return
    if nome not in [u["nome"] for fila in filas_livros[livro].values() for u in fila]:
        filas_livros[livro][tipo].append({"nome": nome, "tipo": tipo})
        print(f"{nome} foi adicionado à fila de espera para o livro '{livro}'.")
    else:
        print("Você já está na fila de espera para este livro.")

def tentar_atender_fila(livro):
    if livro not in filas_livros:
        return
    for tipo in Prioridade + ("Visitantes",):
        fila = filas_livros[livro][tipo]
        while fila:
            usuario = fila.popleft()
            nome = usuario["nome"]
            tipo_usuario = usuario["tipo"]
            if nome in historico_usuarios and historico_usuarios[nome]['livros']:
                print(f"Usuário {nome} já possui um livro emprestado. Passando para o próximo da fila.")
                continue
            disponibilidade_livros[livro] = False
            if nome not in historico_usuarios:
                historico_usuarios[nome] = {"tipo": tipo_usuario, "livros": []}
            historico_usuarios[nome]["livros"].append({"livro": livro, "data": date.today()})
            print(f"Usuário {nome} ({tipo_usuario}) foi atendido da fila para o livro '{livro}'.")
            return

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ").strip()
    if not nome:
        print("Nome não pode ser vazio.")
        return
    if nome in historico_usuarios:
        print("Usuário já cadastrado.")
        return
    tipo = selecionar_tipo_usuario()
    historico_usuarios[nome] = {"tipo": tipo, "livros": []}
    print(f"Usuário {nome} ({tipo}) cadastrado com sucesso.")

def logar_usuario():
    nome = input("Digite o nome do usuário: ").strip()
    if nome not in historico_usuarios:
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return None
    print(f"Bem-vindo, {nome}!")
    return nome

def pegar_livro(nome):
    livros_emprestados = [livro_info['livro'] for livro_info in historico_usuarios[nome]['livros']]
    if livros_emprestados:
        print("Usuários só podem possuir 1 livro emprestado por vez. Devolva o livro atual antes de pegar outro.")
        return

    tipo = historico_usuarios[nome]["tipo"]
    livro = selecionar_livro()
    if livro in livros_emprestados:
        return print("Não pode pegar o mesmo livro novamente.")
    if disponibilidade_livros[livro]:
        historico_usuarios[nome]["livros"].append({"livro": livro, "data": date.today()})
        disponibilidade_livros[livro] = False
        print(f"Livro '{livro}' emprestado com sucesso.")
    else:
        print(f"O livro '{livro}' não está disponível.")
        add_usuario_fila(livro, nome, tipo)

def devolver_livro(nome):
    livros = historico_usuarios[nome]["livros"]
    if not livros:
        print("Você não possui livros para devolver.")
        return
    print("\nSeus livros emprestados:")
    for i, info in enumerate(livros, 1):
        print(f"{i}. {info['livro']}")
    while True:
        escolha = input("Escolha o número do livro para devolver: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(livros):
                break
        print("Opção inválida. Tente novamente.")
    devolvido = livros.pop(escolha - 1)
    livro = devolvido["livro"]
    disponibilidade_livros[livro] = True
    print(f"Livro '{livro}' devolvido com sucesso.")
    tentar_atender_fila(livro)

def consultar_prazo(nome):
    livros = historico_usuarios[nome]["livros"]
    if not livros:
        print("Você não possui livros emprestados.")
        return
    print("\nSeus livros emprestados:")
    for info in livros:
        print(f"- {info['livro']}")

def mostrar_filas_espera():
    print("\nFilas de espera (por prioridade):")
    vazio = True
    for livro, filas in filas_livros.items():
        total = sum(len(fila) for fila in filas.values())
        if total:
            print(f"\nLivro: {livro}")
            for tipo in Prioridade + ("Visitantes",):
                fila = filas[tipo]
                if fila:
                    print(f"  {tipo}: ", end="")
                    print(", ".join([u['nome'] for u in fila]))
            vazio = False
    if vazio:
        print("Não há filas de espera no momento.")

def exibir_usuarios():
    print("\nUsuários cadastrados:")
    if not historico_usuarios:
        print("Nenhum usuário cadastrado.")
        return
    for nome, info in historico_usuarios.items():
        print(f"- {nome} ({info['tipo']})")

def exibir_livros_emprestados():
    print("\nFila de usuários com livros emprestados:")
    emprestimos = []
    for nome, info in historico_usuarios.items():
        for livro in info["livros"]:
            emprestimos.append((nome, info["tipo"], livro["livro"]))
    if not emprestimos:
        print("Nenhum livro emprestado no momento.")
        return
    for nome, tipo, livro in emprestimos:
        print(f"{nome} ({tipo}) está com '{livro}'")

def exibir_livros_disponiveis():
    for i, (titulo, autor, isbn) in enumerate(livros_disponiveis, 1):
        status = "Disponível" if disponibilidade_livros[titulo] else "Emprestado"
        print(f"{i}. {titulo} - {autor} (ISBN: {isbn}) [{status}]")

def menu_usuario(nome):
    while True:
        print("\nMenu do Usuário:")
        print("1. Pegar Livro")
        print("2. Devolver Livro")
        print("3. Consultar Prazo de Devolução")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            pegar_livro(nome)
        elif opcao == "2":
            devolver_livro(nome)
        elif opcao == "3":
            consultar_prazo(nome)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_livro():
    print("\nCadastrar novo livro")
    titulo = input("Digite o título do livro: ").strip()
    autor = input("Digite o autor do livro: ").strip()
    isbn = input("Digite o ISBN do livro: ").strip()

    if not titulo or not autor or not isbn:
        print("Todos os campos são obrigatórios.")
        return

    novo_livro = (titulo, autor, isbn)
    livros_disponiveis.append(novo_livro)
    disponibilidade_livros[titulo] = True
    print(f"Livro cadastrado com sucesso: {novo_livro}")
    print(livros_disponiveis)

def excluir_livro():
    print("\nExcluir livro")
    if not livros_disponiveis:
        print("Não há livros disponíveis para excluir.")
        return

    exibir_livros_disponiveis()
    while True:
        escolha = input("Escolha o número do livro para excluir: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(livros_disponiveis):
                break
        print("Opção inválida. Tente novamente.")

    livro_removido = livros_disponiveis[escolha - 1]
    titulo_removido = livro_removido[0]

    for info in historico_usuarios.items():
        livros_emprestados = [livro['livro'] for livro in info['livros']]
        if titulo_removido in livros_emprestados:
            print(f"O livro '{titulo_removido}' está emprestado e não pode ser excluído.")
            return

    
    livros_disponiveis.pop(escolha - 1)
    disponibilidade_livros.pop(titulo_removido, None)
    filas_livros.pop(titulo_removido, None)

    print(f"Livro excluído com sucesso: {livro_removido}")

def excluir_usuario(nome):
    if nome in historico_usuarios:
        livros = historico_usuarios[nome]["livros"]
        for livro_info in livros:
            titulo = livro_info["livro"]
            disponibilidade_livros[titulo] = True
        del historico_usuarios[nome]
        print(f"Usuário {nome} excluído com sucesso e seus livros foram devolvidos.")
    else:
        print("Usuário não encontrado.")

def menu_administrador():
    while True:
        print("\nMenu do Administrador:")
        print("1. Mostrar Fila de Espera")
        print("2. Histórico de Eventos")
        print("3. Cadastrar Livro")
        print("4. Excluir Livro")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            mostrar_filas_espera()
        elif opcao == "2":
            print("\nHistórico de eventos:")
            if not historico_usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for nome, info in historico_usuarios.items():
                    livros = ", ".join([livro['livro'] for livro in info['livros']]) if info['livros'] else "Nenhum livro emprestado"
                    print(f"- {nome} ({info['tipo']}): {livros}")
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            excluir_livro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente XD.")

def main():
    try:
        while True:
            print("\nMenu Principal:")
            print("1. Cadastrar Usuário")
            print("2. Logar Usuário")
            print("3. Menu do Administrador")
            print("4. Sair")
            opcao = input("Escolha uma opção: ").strip()
            if opcao == "1":
                cadastrar_usuario()
            elif opcao == "2":
                nome = logar_usuario()
                if nome:
                    menu_usuario(nome)
            elif opcao == "3":
                menu_administrador()
            elif opcao == "4":
                print("Encerrando o programa. tchau Tchau!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrompido pelo usuário. Volte Sempre!")

if __name__ == "__main__":
    main()
