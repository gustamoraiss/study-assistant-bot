import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from gerenciador_dados import carregar_provas, salvar_provas, validar_e_formatar_data
from datetime import datetime

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update, context):
    await update.message.reply_text('Seja bem-vindo(a) ao Bot Assistent de estudos! Algum compromisso à adicionar?')

async def add(update, context):
    if not context.args or len(context.args) < 2:
        await update.message.reply_text('Uso incorreto. Digite no formato: /add DD/MM/AAAA Nome da Matéria - Descrição')
        return

    data_texto = context.args[0]
    descricao = " ".join(context.args[1:])

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

async def provas(update, context):
    provas = carregar_provas()
    if not provas:
        return await update.message.reply_text('Você não tem nenhuma prova cadastrada no momento.')
    
    provas_ordenadas = sorted(provas, key=lambda p: p['data'])
    mensagem = '📚 Suas Provas Cadastradas:\n\n'

    for i, prova in enumerate(provas_ordenadas, 1):
        data_valida = datetime.strptime(prova['data'], "%Y-%m-%d")
        data_exibicao = data_valida.strftime('%d/%m/%Y')
        mensagem += f"{i}. 📅 {data_exibicao} - {prova['descricao']}\n"

    await update.message.reply_text(mensagem)

async def concluir(update, context):
    provas = carregar_provas()

    if (context.args and not context.args[0].isdigit()) or not context.args:
        return await update.message.reply_text("Você deve digitar o número da prova a ser removida (ex: /concluir 1). Para consultar, digite o comando /provas.")
    
    elif not provas:
        return await update.message.reply_text("Você não tem nenhuma prova para concluir.")

    elif context.args and context.args[0].isdigit():
        numero = int(context.args[0])
        provas_ordenadas = sorted(provas, key=lambda p: p['data'])
        if numero >= 1 and numero <= len(provas_ordenadas):
            prova_removida = provas_ordenadas[numero - 1]
            provas_ordenadas.pop(numero - 1)
            salvar_provas(provas_ordenadas)
            return await update.message.reply_text(f"✅ Prova '{prova_removida['descricao']}' concluída com sucesso!")
        else:
            return await update.message.reply_text(f"Número inválido! Escolha um número entre 1 e {len(provas_ordenadas)}.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('add', add))
    app.add_handler(CommandHandler('provas', provas))
    app.add_handler(CommandHandler('concluir', concluir))
    app.run_polling()

if __name__ == '__main__':
    main()