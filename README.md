# 🎓 Bot Assistente de Estudos para Telegram

Um bot para gerenciamento de avaliações e prazos acadêmicos desenvolvido em Python, focado em organização e controle de datas de provas de forma prática diretamente pelo Telegram.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **Biblioteca:** `python-telegram-bot` (Comunicação assíncrona com a API do Telegram)
- **Persistência de Dados:** Arquivos locais no formato JSON
- **Segurança:** `python-dotenv` (Gerenciamento seguro de variáveis de ambiente)

---

## ⚡ Funcionalidades

- **`/start`**: Mensagem de boas-vindas e apresentação do assistente.
- **`/add <DD/MM/AAAA> <Matéria - Descrição>`**: Cadastro de avaliações com validação automática de datas.
- **`/provas`**: Listagem de todas as avaliações cadastradas ordenadas cronologicamente (da data mais próxima para a mais distante).
- **`/concluir <número>`**: Conclusão e remoção de uma avaliação através do índice numérico da lista.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.10 ou superior instalado.
- Uma conta no Telegram e um Token de Bot obtido via [@BotFather](https://t.me/BotFather).

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/gustamoraiss/study-assistant-bot.git](https://github.com/gustamoraiss/study-assistant-bot.git)
   cd study-assistant-bot
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure a variável de ambiente:**
   Crie um arquivo `.env` na raiz do projeto e insira seu token:
   ```env
   TELEGRAM_TOKEN=seu_token_aqui
   ```

5. **Execute o Bot:**
   ```bash
   python main.py
   ```

---

## 📂 Estrutura do Projeto

```text
├── .env                  # Variáveis de ambiente (Token do bot - ignorado pelo Git)
├── .gitignore            # Proteção contra envio de chaves de API e arquivos temporários
├── gerenciador_dados.py  # Funções de leitura/escrita em JSON e validação de datas
├── main.py               # Handlers de comandos e inicialização do bot do Telegram
├── provas.json           # Armazenamento persistente de dados
├── README.md             # Documentação do projeto
└── requirements.txt      # Dependências e bibliotecas do projeto
```