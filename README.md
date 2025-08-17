# Desafio análise de dados covid-19
Repositório destinado ao desafio de análise de dados sobre a covid-19. 
O projeto está hospedado no seguinte link: https://verificacao-de-dados-covid.streamlit.app/

## Iniciar streamLit

Instalar dependencias com comando `pip install -r requirement.txt`
Rodar comando `streamlit run Análise_COVID-19.py`

## Sobre o projeto

Utilizei do desafio para estudar e aprender mais a usar e me esfocei ao máximo para entregar no prazo do dia 18/08/2025, mas que independente do resultado pretendo continuar estudando e expandir esse projeto.

### Tecnologias usadas

Foi utilizado Streamlit para o servidor web, gerando componentes com design elegante e funcionalidade responsiva e acessivel.
Junto foi utilizado a biblioteca Pandas para manipulação de dados do repósitorio público [Coronavirus (Covid-19) Data in the United States](https://github.com/nytimes/covid-19-data).
Foi realiza a integração com supabase, para gerencia de banco de dados fácil de configurar e acessar.

#### Conexão com banco de dados
Foi utilizado o _Secrets management_ do Streamlit para gerenciar a conexão com o banco de dados do supabase. Para uso local edite o arquivo `secrets.toml` (Verifique a [documentação](https://docs.streamlit.io/develop/concepts/connections/secrets-management) de onde encontrar em seu sistema) com os seguintes valores:
```toml
supabase_url = "sua_url"
supabase_key = "sua_key"
```