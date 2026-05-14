````markdown
# API Biblioteca 📚

Projeto desenvolvido em Python para gerar dados fictícios de uma biblioteca utilizando APIs públicas de livros.

O sistema busca:
- títulos reais;
- autores reais;
- editoras;
- anos de publicação;

E gera automaticamente:
- IDs;
- usuários fictícios;
- empréstimos;
- planilha Excel pronta para modelagem no MySQL Workbench.

---

# 🚀 Funcionalidades

✅ Busca livros automaticamente pela API Open Library  
✅ Gera autores reais  
✅ Gera editoras reais  
✅ Cria IDs automáticos  
✅ Exporta para Excel (`.xlsx`)  
✅ Escolha do local de salvamento por janela gráfica  
✅ Compatível com MySQL Workbench  

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Requests
- Tkinter
- OpenPyXL
- Open Library API

---

Entre na pasta:

```bash
cd api-biblioteca
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute o arquivo Python:

```bash
python biblioteca_api.py
```

O programa irá:

1. Buscar livros automaticamente
2. Gerar os dados
3. Abrir uma janela para escolher onde salvar
4. Criar a planilha Excel

---

# 📊 Estrutura da Planilha

A planilha contém:

| Campo           | Descrição                   |
| --------------- | --------------------------- |
| id_livro        | ID do livro                 |
| titulo          | Nome do livro               |
| autor           | Nome do autor               |
| id_autor        | ID do autor                 |
| editora         | Nome da editora             |
| ano_publicacao  | Ano de publicação           |
| id_usuario      | ID do usuário               |
| usuario         | Usuário fictício            |
| id_emprestimo   | ID do empréstimo            |
| data_emprestimo | Data fictícia de empréstimo |

---

# 🌐 API Utilizada

Open Library API:

[https://openlibrary.org/developers/api](https://openlibrary.org/developers/api)

---

Projeto desenvolvido para fins acadêmicos e prática de modelagem de banco de dados.

---

# 📜 Licença

Este projeto é livre para estudos e uso educacional.


