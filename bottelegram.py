import telebot
from eth_request.request import consultar_eth
from eth_request.arqign.chavetelegram import chavetelegram



bot = telebot.TeleBot(chavetelegram())


@bot.message_handler(commands=["eth"])
def eth(mensagem):
    eth_text = consultar_eth()
    bot.reply_to(mensagem, eth_text)



def verificar(mensagem):
    return True



@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Olá Gostaria hoje de ver a cotação de qual moeda? (Click no item)
        /eth
        /bitcoin
        /Dolar
    Click em uma dessas opções para prosseguir.
    Responder qualquer outra opção não irá funcionar."""
    
    bot.reply_to(mensagem, texto)


bot.polling()