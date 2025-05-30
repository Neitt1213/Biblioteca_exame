#Lucas Nunes Alves da Silva RA:1996656
# Nathan Nogueira Carrara RA:1999644
# Igor Yano Maraci RA:1992650
from collections import deque
import sys
Prioridade = ["Professor", "Aluno", "Funcionario", "Terceirizado"]
Validos = Prioridade + ["Visitantes"]
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
def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar usuário e pegar livro")
    print("2. Devolver livro")
    print("3. Mostrar filas de espera")
    print("4. Exibir histórico de usuários")
    print("5. Atender próximo usuário da fila")
    print("6. Sair")
def exibir_tipos_usuario():
    print("\nTipos de usuários:")
    for i, tipo in enumerate(Validos, 1):
        print(f"{i}. {tipo}")
def selecionar_tipo_usuario():
    exibir_tipos_usuario()
    while True:
        escolha = input("Escolha o número do tipo de usuário: ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(Validos):
            return Validos[int(escolha) - 1]
        print("Opção inválida. Tente novamente.")
def exibir_livros_disponiveis():
    print("\nLivros disponíveis:")
    for i, (titulo, autor, isbn) in enumerate(livros_disponiveis, 1):
        status = "Disponível" if disponibilidade_livros[titulo] else "Indisponível"
        print(f"{i}. {titulo} - {autor} (ISBN: {isbn}) - {status}")
def selecionar_livro():
    exibir_livros_disponiveis()
    while True:
        escolha = input("Escolha o número do livro: ").strip()
        if escolha.isdigit():
            n = int(escolha)
            if 1 <= n <= len(livros_disponiveis):
                titulo = livros_disponiveis[n - 1][0]
                return titulo
        print("Opção inválida. Tente novamente.")
def inicializar_filas(livro):
    if livro not in filas_livros:
        filas_livros[livro] = {tipo: deque() for tipo in Validos}
def add_usuario_fila(livro, nome, tipo):
    inicializar_filas(livro)
    filas_livros[livro][tipo].append({"nome": nome, "tipo": tipo})
    print(f"{nome} ({tipo}) entrou na fila para o livro '{livro}'.")
def pode_pegar_livro(nome):
    if nome in historico_usuarios and historico_usuarios[nome]["livros"]:
        print(f"{nome} já está com o(s) livro(s): {', '.join(historico_usuarios[nome]['livros'])}")
        return False
    return True
def cadastrar_usuario_pegar_livro():
    nome = input("Digite o nome do usuário: ").strip()
    tipo = selecionar_tipo_usuario()
    if not pode_pegar_livro(nome):
        print("Devolva os livros atuais antes de pegar outro.")
        return
    livro = selecionar_livro()
    if not disponibilidade_livros[livro]:
        print(f"O livro '{livro}' não está disponível, será adicionado à fila.")
        add_usuario_fila(livro, nome, tipo)
        if nome not in historico_usuarios:
            historico_usuarios[nome] = {"tipo": tipo, "livros": []}
        return
    disponibilidade_livros[livro] = False
    if nome not in historico_usuarios:
        historico_usuarios[nome] = {"tipo": tipo, "livros": []}
    historico_usuarios[nome]["livros"].append(livro)
    print(f"{nome} pegou o livro '{livro}'.")
def devolver_livro():
    nome = input("Digite o nome do usuário que vai devolver o livro: ").strip()
    if nome not in historico_usuarios or not historico_usuarios[nome]["livros"]:
        print("Usuário não possui livros para devolver ou não está cadastrado.")
        return
    livros = historico_usuarios[nome]["livros"]
    print(f"Livros de {nome}:")
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")
    while True:
        escolha = input("Escolha o número do livro para devolver: ").strip()
        if escolha.isdigit():
            n = int(escolha)
            if 1 <= n <= len(livros):
                livro_devolvido = livros.pop(n - 1)
                disponibilidade_livros[livro_devolvido] = True
                print(f"Livro '{livro_devolvido}' devolvido com sucesso.")
                tentar_atender_fila(livro_devolvido)
                return
        print("Opção inválida. Tente novamente.")
def tentar_atender_fila(livro):
    if livro not in filas_livros:
        return
    for tipo in Prioridade + ["Visitantes"]:
        fila = filas_livros[livro][tipo]
        if fila:
            usuario = fila.popleft()
            nome = usuario["nome"]
            tipo_usuario = usuario["tipo"]
            disponibilidade_livros[livro] = False
            if nome not in historico_usuarios:
                historico_usuarios[nome] = {"tipo": tipo_usuario, "livros": []}
            historico_usuarios[nome]["livros"].append(livro)
            print(f"Usuário {nome} ({tipo_usuario}) foi atendido da fila para o livro '{livro}'.")
            return
def mostrar_filas():
    if not filas_livros:
        print("Não há filas de espera no momento.")
        return
    for livro, filas in filas_livros.items():
        print(f"\nFila para o livro '{livro}':")
        total = 0
        for tipo in Prioridade + ["Visitantes"]:
            fila = filas.get(tipo, deque())
            if fila:
                print(f" {tipo}:")
                for usuario in fila:
                    print(f"  - {usuario['nome']}")
                total += len(fila)
        if total == 0:
            print(" Fila vazia.")
def exibir_historico():
    if not historico_usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return
    print("\nHistórico de usuários e livros:")
    for nome, dados in historico_usuarios.items():
        livros = ", ".join(dados["livros"]) if dados["livros"] else "Nenhum livro"
        print(f"{nome} ({dados['tipo']}): {livros}")
def atender_proximo_usuario():
    print("Escolha o livro para atender a próxima pessoa da fila:")
    livro = selecionar_livro()
    if livro not in filas_livros or all(not filas_livros[livro][tipo] for tipo in Validos):
        print(f"Não há ninguém na fila para o livro '{livro}'.")
        return
    tentar_atender_fila(livro)
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_usuario_pegar_livro()
        elif opcao == "2":
            devolver_livro()
        elif opcao == "3":
            mostrar_filas()
        elif opcao == "4":
            exibir_historico()
        elif opcao == "5":
            atender_proximo_usuario()
        elif opcao == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()