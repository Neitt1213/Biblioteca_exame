from collections import deque
from datetime import date, timedelta

Prioridade = ["Professor", "Aluno", "Funcionario", "Terceirizado"]
Validos = Prioridade + ["Visitantes"]
filas_livros = {}
historico_usuarios = {}
disponibilidade_livros = {
    "O Senhor dos Anéis": True,
    "Introdução à Programação com Python": True,
    "Estruturas de Dados e Algoritmos em Python": True,
    "1984": True,
    "Dom Casmurro": True,
    "A Revolução dos Bichos": True,
    "Clean Code": True,
    "Python Fluente": True,
    "O Pequeno Príncipe": True,
    "O Nome do Vento": True,
    "A Guerra dos Tronos": True,
    "Harry Potter e a Pedra Filosofal": True,
    "O Código Da Vinci": True
}

livros_disponiveis = [
    ("O Senhor dos Anéis", "J.R.R. Tolkien", "978-8595084759"),
    ("Introdução à Programação com Python", "Nilo Ney Coutinho Menezes", "978-8575227183"),
    ("Estruturas de Dados e Algoritmos em Python", "Michael T. Goodrich et al.", "978-8582604110"),
    ("1984", "George Orwell", "978-8535914849"),
    ("Dom Casmurro", "Machado de Assis", "978-8573262681"),
    ("A Revolução dos Bichos", "George Orwell", "978-8535909555"),
    ("Clean Code", "Robert C. Martin", "978-8576082675"),
    ("Python Fluente", "Luciano Ramalho", "978-8575224625"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "978-8522005230"),
    ("O Nome do Vento", "Patrick Rothfuss", "978-8563560271"),
    ("A Guerra dos Tronos", "George R. R. Martin", "978-8535914849"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", "978-8532511010"),
    ("O Código Da Vinci", "Dan Brown", "978-8575422397")
]


# tupla com regras de empréstimo adicionada para exame
regra_emprestimo = (
    ("Professor", 5, 30),
    ("Aluno", 2, 7),
    ("Funcionario", 3, 15),
    ("Terceirizado", 1, 7),
    ("Visitantes", 1, 7)
)

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
        titulos = [livro["titulo"] for livro in historico_usuarios[nome]["livros"]]
        print(f"{nome} já está com o(s) livro(s): {', '.join(titulos)}")
        return False
    return True

# função adicionada para o exame
def validar_regras_emprestimo(tipo_usuario, nome):
    max_livros = 0
    for regra in regra_emprestimo:
        if regra[0] == tipo_usuario:
            max_livros = regra[1]
            break
    if nome in historico_usuarios:
        qtd_atual = len(historico_usuarios[nome]["livros"])
        if qtd_atual >= max_livros:
            print(f"Limite de {max_livros} livros para {tipo_usuario} atingido. Devolva algum antes de pegar outro.")
            return False
    return True

def cadastrar_usuario_pegar_livro():
    nome = input("Digite o nome do usuário: ").strip()
    tipo = selecionar_tipo_usuario()
    if not pode_pegar_livro(nome):
        print("Devolva os livros atuais antes de pegar outro.")
        return
    

    # validação da regra de empréstimo da tupla para exame
    if not validar_regras_emprestimo(tipo, nome):
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
    historico_usuarios[nome]["livros"].append({"titulo": livro, "data_emprestimo": date.today()})
    print(f"{nome} pegou o livro '{livro}'.")




def devolver_livro():
    nome = input("Digite o nome do usuário que vai devolver o livro: ").strip()
    if nome not in historico_usuarios or not historico_usuarios[nome]["livros"]:
        print("Usuário não possui livros para devolver ou não está cadastrado.")
        return
    livros = historico_usuarios[nome]["livros"]
    print(f"Livros de {nome}:")
    for i, livro_info in enumerate(livros, 1):
        print(f"{i}. {livro_info['titulo']}")
    while True:
        escolha = input("Escolha o número do livro para devolver: ").strip()
        if escolha.isdigit():
            n = int(escolha)
            if 1 <= n <= len(livros):
                livro_devolvido_info = livros.pop(n - 1)
                livro_devolvido = livro_devolvido_info['titulo']
                data_emprestimo = livro_devolvido_info['data_emprestimo']
                disponibilidade_livros[livro_devolvido] = True



                # calculo de atraso e multa baseado nas regras para o exame
                
                prazo_dias = 7  
                for regra in regra_emprestimo:
                    if regra[0] == historico_usuarios[nome]["tipo"]:
                        prazo_dias = regra[2]
                        break
                prazo = timedelta(days=prazo_dias)
                data_devolucao = date.today()
                atraso = (data_devolucao - (data_emprestimo + prazo)).days
                if atraso > 0:
                    multa = atraso * 1  
                    print(f"Atenção: O livro está {atraso} dia(s) atrasado(s). Multa: R${multa}.")
                else:
                    print("Livro devolvido no prazo, sem multa.")
                

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
            historico_usuarios[nome]["livros"].append({"titulo": livro, "data_emprestimo": date.today()})
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
        livros = ", ".join([livro["titulo"] for livro in dados["livros"]]) if dados["livros"] else "Nenhum livro"
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
