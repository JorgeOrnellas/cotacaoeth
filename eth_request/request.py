from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.infomoney.com.br/cotacoes/cripto/ativo/ethereum-eth/"

def consultar_eth() -> str:
    response = urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    line_info = soup.findAll('div', class_='line-info')[0]
    eth_real_value = line_info.find('div', class_='value').find('p').text
    eth_variacao = line_info.find('div', class_='percentage').find('p').text
    eth_variacao = eth_variacao.replace('\n', '').strip('. ')
    
    return f'O Ethereum hoje está R$ {eth_real_value} e variou no dia de hoje {eth_variacao}'
