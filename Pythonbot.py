# Chatbot de Biblioteca

# Base de livros da biblioteca (chaves padronizadas em minúsculo)
livros_disponiveis = [
    {"titulo": "O caçador de pipas", "autor": "Khaled Hosseini", "quantidade": 6},
    {"titulo": "As cronicas de Narnia", "autor": "C.S. Lewis", "quantidade": 2},
    {"titulo": "A menina que roubava livros", "autor": "Markus Zusak", "quantidade": 3},
    {"titulo": "Assassinato No Expresso do Oriente", "autor": "Agatha Christie", "quantidade": 15}
]

def exibir_menu():
    """Exibir as opções disponíveis no chatbot da biblioteca"""
    print("\n--- Bem-vindo à Biblioteca Digital ---")
    print("1. Listar todos os livros disponíveis")
    print("2. Buscar os livros pelo título")
    print("3. Emprestar um livro")
    print("4. Sair")


def listar_livros():
    """Retornar uma string com os livros e suas quantidades"""
    resultado = "\n**Acervo da Biblioteca:**\n"
    for livro in livros_disponiveis:
        resultado += f"- {livro['titulo']} (Autor: {livro['autor']}) | Disponíveis: {livro['quantidade']}\n"
    return resultado


def buscar_livro(titulo_busca: str):
    """Busca um livro por seu título"""
    titulo_busca = titulo_busca.lower().strip()
    encontrados = [l for l in livros_disponiveis if titulo_busca in l["titulo"].lower()]

    if not encontrados:
        return f"❌ Nenhum livro foi encontrado com o termo '{titulo_busca}'."

    resposta = f"\n🔍 **Resultados da busca para '{titulo_busca}':**\n"
    for livro in encontrados:
        resposta += f"- {livro['titulo']} por {livro['autor']} (Disponíveis: {livro['quantidade']}\n"
    return resposta


def emprestar_livro(titulo_busca: str):
    """Simula o empréstimo de um livro diminuindo a quantidade no estoque."""
    titulo_busca = titulo_busca.lower().strip()
    for livro in livros_disponiveis:
        if titulo_busca in livro["titulo"].lower():
            if livro["quantidade"] > 0:
                livro["quantidade"] -= 1
                return f"✅ Empréstimo realizado! O livro '{livro['titulo']}' foi emprestado com sucesso. Restam {livro['quantidade']} unidades."
            else:
                return f"⚠️ Desculpe, o livro '{livro['titulo']}' está esgotado no momento!"
    return f"❌ Livro '{titulo_busca}' não foi encontrado no acervo."