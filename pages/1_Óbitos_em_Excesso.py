import streamlit as st
import pandas as pd

country_header = "country"
deaths_header = "deaths"
year_header = "year"
expected_deaths_header = "expected_deaths"
excess_deaths_header = "excess_deaths"
filter_by_country_key = "filter_by_country"


def display_about_content():
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


def load_data():
    url = "https://raw.githubusercontent.com/nytimes/covid-19-data/refs/heads/master/excess-deaths/deaths.csv"
    return pd.read_csv(url)


def update_filter_by_country():
    st.query_params[country_header] = st.session_state[filter_by_country_key]


def filter_by_country(df: pd.DataFrame):
    countries = df[country_header].unique()

    selected_countries = st.multiselect(
        label="Selecione os paises",
        options=countries,
        key=filter_by_country_key,
        default=st.query_params.get_all(country_header),
        on_change=update_filter_by_country,
    )

    if selected_countries:
        return df[(df[country_header].isin(selected_countries))]
    return df


def sum_deaths_grouped_by(data_frame: pd.DataFrame, group_by: str):
    return data_frame.groupby(group_by)[deaths_header].sum().reset_index()


def handle_data_view(key: str):
    return st.selectbox(
        label="Selecione a visão", options=["Gráfico", "Tabela"], key=key
    )


# Main
df = load_data()
filtered_df = df

display_about_content()

filtered_df = filter_by_country(df)

default_view, deaths_by_countries, deaths_by_year, expected_excess_deaths = st.tabs(
    [
        "Visão geral",
        "Mortes por Países",
        "Mortes por Ano",
        "Expectativa/Excesso de Mortes",
    ]
)

with default_view:
    st.write(filtered_df)
with deaths_by_countries:
    grouped_df = sum_deaths_grouped_by(filtered_df, country_header)

    view = handle_data_view("view_by_countries")

    if view == "Gráfico":
        st.bar_chart(data=grouped_df, x=country_header, y=deaths_header)
    else:
        st.write(grouped_df)
with deaths_by_year:
    filtered_df = filtered_df[filtered_df[year_header].astype(str).str.isdigit()]

    grouped_df = sum_deaths_grouped_by(filtered_df, year_header)

    view = handle_data_view("view_by_year")

    if view == "Gráfico":
        st.line_chart(data=grouped_df, x=year_header, y=deaths_header)
    else:
        st.write(grouped_df)
with expected_excess_deaths:
    grouped_df = (
        filtered_df.groupby(country_header)[
            [expected_deaths_header, excess_deaths_header]
        ]
        .sum()
        .reset_index()
    )

    view = handle_data_view("view_by_expected_excess_deaths")

    if view == "Gráfico":
        st.bar_chart(
            grouped_df.set_index(country_header)[
                [expected_deaths_header, excess_deaths_header]
            ]
        )
    else:
        st.write(grouped_df)
