 Consulta de Cotação de Moedas via API

Projeto em Python que consulta em tempo real a cotação do Dólar (USD) para outras moedas, como Real (BRL), utilizando a [ExchangeRate API](https://www.exchangerate-api.com/).

 Tecnologias Utilizadas

- Python 3.x
- [requests](https://pypi.org/project/requests/) – para fazer requisições HTTP
- [python-dotenv](https://pypi.org/project/python-dotenv/) – para carregar variáveis de ambiente de forma segura

---

 Como executar o projeto localmente
 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/cotacao_api.git
cd cotacao_api

crie o ambiente virtual e o ative
# No Windows
python -m venv venv_nome
venv_seunome\Scripts\activate

# No Linux/Mac
python3 -m venv venv_nome
source venv_seunome/bin/activate

3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt

4. Crie o arquivo .env
No diretório raiz do projeto, crie um arquivo chamado .env com o seguinte conteúdo:

ini
Copiar
Editar
API_KEY=sua_chave_aqui
🔑 A chave pode ser obtida gratuitamente em https://www.exchangerate-api.com.

5. Execute o script
bash
Copiar
Editar
python consulta.py

O que o script faz?
Carrega a variável de ambiente API_KEY do arquivo .env

Faz uma requisição para o endpoint da ExchangeRate API

Exibe no terminal as cotações atuais do USD para:

BRL (Real)

EUR (Euro)

GBP (Libra Esterlina)

JPY (Iene)

E outras moedas que você pode configurar

🛑 Arquivos ignorados
O projeto contém um .gitignore com:

bash
Copiar
Editar
.env
venv*/
__pycache__/
Isso garante que arquivos sensíveis e desnecessários não sejam enviados ao GitHub.

☁️ Deploy e Restauração
Após clonar o projeto:

bash
Copiar
Editar
pip install -r requirements.txt
Recrie o .env com sua API_KEY e execute o consulta.py normalmente.


