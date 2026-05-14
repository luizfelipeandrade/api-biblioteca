import requests
import pandas as pd
from tkinter import Tk, filedialog
import random

# Temas para buscar livros
temas = [
    "programação",
    "história",
    "matemática",
    "ciência",
    "literatura",
    "tecnologia",
    "filosofia"
]

# Lista de editoras reais para fallback
editoras_reais = [
    "Companhia das Letras",
    "Editora Record",
    "Saraiva",
    "Novatec",
    "Alta Books",
    "Intrínseca",
    "Rocco",
    "Pearson",
    "Atlas",
    "Campus Elsevier"
]

livros = []

id_livro = 1
id_autor = 1
id_usuario = 1
id_emprestimo = 1

for tema in temas:

    print(f"Buscando livros de: {tema}")

    url = f"https://openlibrary.org/search.json?q={tema}&language=por"

    resposta = requests.get(url)

    # Verifica se a API respondeu corretamente
    if resposta.status_code != 200:
        print(f"Erro ao buscar tema: {tema}")
        continue

    dados = resposta.json()

    # Pega os livros encontrados
    docs = dados.get("docs", [])

    # Se não encontrar nada, pula
    if not docs:
        print(f"Nenhum livro encontrado para: {tema}")
        continue

    # Limita quantidade
    for item in docs[:15]:

        titulo = item.get("title", "Título desconhecido")

        # Autor
        autores = item.get("author_name", ["Autor desconhecido"])
        autor = autores[0]

        # Editora
        editoras_api = item.get("publisher")

        if editoras_api and len(editoras_api) > 0:
            editora = editoras_api[0]
        else:
            editora = random.choice(editoras_reais)

        # Ano
        ano = item.get("first_publish_year", "Desconhecido")

        # Adiciona na lista
        livros.append({
            "id_livro": id_livro,
            "titulo": titulo,
            "autor": autor,
            "id_autor": id_autor,
            "editora": editora,
            "ano_publicacao": ano,
            "id_usuario": id_usuario,
            "usuario": f"Usuário {id_usuario}",
            "id_emprestimo": id_emprestimo,
            "data_emprestimo": f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/2026"
        })

        id_livro += 1
        id_autor += 1
        id_usuario += 1
        id_emprestimo += 1

# Verifica se encontrou livros
if not livros:
    print("\nNenhum livro encontrado.")
    exit()

# Cria DataFrame
df = pd.DataFrame(livros)

# Janela para escolher onde salvar
Tk().withdraw()

caminho = filedialog.asksaveasfilename(
    defaultextension=".xlsx",
    filetypes=[("Arquivo Excel", "*.xlsx")],
    title="Salvar planilha da biblioteca"
)

# Salva arquivo
if caminho:
    df.to_excel(caminho, index=False)

    print("\nArquivo Excel criado com sucesso!")
    print(caminho)

else:
    print("\nSalvamento cancelado.")