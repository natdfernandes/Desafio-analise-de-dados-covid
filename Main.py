import streamlit as st

st.set_page_config(page_title="Desafio análise de dados Covid", page_icon="🏥")

st.title("COVID-19 nos EUA (2020–2023)")

st.markdown(
    """
    Este dashboard interativo apresenta uma análise abrangente da evolução da pandemia de COVID-19 nos Estados Unidos, com base nos dados públicos disponibilizados pelo *The New York Times* ([GitHub - NYT COVID-19 Data](https://github.com/nytimes/covid-19-data)).

    A plataforma oferece visualizações dinâmicas e filtros personalizados que permitem explorar:

    * **Gráficos de linha e barra** com a evolução diária e acumulada de casos e óbitos por estado e condado.
    * **Tabelas interativas** com opções de busca e ordenação para facilitar comparações regionais.
    * **Filtros por período, estado e tipo de dado (casos/óbitos)** para análises específicas.
    * **Mapas temáticos** (se aplicável) com distribuição geográfica dos dados ao longo do tempo.

    O objetivo é proporcionar uma visão clara, acessível e explorável da pandemia entre 2020 e 2023, apoiando estudos, decisões e reflexões com base em dados confiáveis.
    """
)
