import streamlit as st
import pandas as pd

country_header = "country"

st.title("Óbitos em Excesso Durante a Pandemia de Coronavírus")

with st.expander("Sobre está página"):
    st.markdown(
        """
    Este painel apresenta dados sobre **óbitos em excesso** registrados durante a pandemia de COVID-19, com base no levantamento do *The New York Times*. Os dados incluem mortes por todas as causas em 32 países, permitindo uma análise mais ampla do verdadeiro impacto da pandemia além dos números oficiais de óbitos por COVID-19.

    Os dados foram coletados de registros civis, departamentos de saúde e outras fontes oficiais. Como nem todas as mortes relacionadas à COVID-19 foram oficialmente registradas (por falta de testes ou óbitos fora de hospitais), o número de **óbitos em excesso** — diferença entre mortes registradas e o número esperado com base em anos anteriores — oferece um retrato mais completo.

    ### O que você encontrará nesta seção:

    * Dados por país e, em alguns casos, por cidade.
    * Informações organizadas por semana ou mês.
    * Comparação entre mortes reais e mortes esperadas.
    * Base de cálculo construída a partir de médias históricas (2010–2019, dependendo do país).
    * Tabelas com colunas como: país, localidade, datas, número de óbitos, óbitos esperados e excedentes.

    ### Metodologia:

    * O número de óbitos esperados foi calculado com modelos estatísticos que consideram tendências demográficas e variações sazonais.
    * As análises podem ser afetadas por atrasos ou falhas nos sistemas de registro, especialmente em países com menor cobertura estatística.
    * Alguns estados e países foram excluídos por inconsistência ou falta de dados.

    ### Fontes e Licença:

    * Os dados foram coletados e organizados por jornalistas e especialistas do *The New York Times*, com o apoio de pesquisadores e demógrafos.
    * Estão disponíveis para uso público não comercial, desde que seja feita a devida atribuição ao NYT.
    * Para mais informações, acesse: [Link para o gráfico interativo original](https://www.nytimes.com/interactive/2020/04/21/world/coronavirus-missing-deaths.html)
    """
    )

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/refs/heads/master/excess-deaths/deaths.csv"
df = pd.read_csv(url)

filtered_df = df


def filter_by_country(df: pd.DataFrame):
    countries = df[country_header].unique()

    selected_countries = st.multiselect(
        label="Selecione os paises",
        options=countries,
        default=st.query_params.get_all(country_header),
    )

    if selected_countries:
        st.query_params[country_header] = selected_countries
        return df[(df[country_header].isin(selected_countries))]
    return df


filtered_df = filter_by_country(df)
st.write(filtered_df)
