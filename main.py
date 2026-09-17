import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from gerenciador_dados import carregar_provas, salvar_provas, validar_e_formatar_data

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update, context):
    await update.message.reply_text('Hello, World!')

async def add(update, context):
    if not context.args or len(context.args) < 2:
        await update.message.reply_text('Uso incorreto. Digite no formatdo: /add DD/MM/AAAA Nome da Matéria - Descrição')
        return

    data_texto = context.args[0]
    descricao = context.args[1:]

    data_valida = validar_e_formatar_data(data_texto)
    if not data_valida:
        await update.message.reply_text('Data inválida. use o formato DD/MM/AAAA (ex: 20/10/2026).')
        return

    provas = carregar_provas()
    nova_prova = {
        "data": data_valida,
        "descricao": descricao
    }
    
    provas.append(nova_prova)
    salvar_provas(provas)

    await update.message.reply_text(f'✅ Prova cadastrada com sucesso para {data_texto}!')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.run_polling()

if __name__ == '__main__':
    main()