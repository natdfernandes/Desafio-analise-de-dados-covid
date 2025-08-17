import streamlit as st
import supabase_db as db

st.set_page_config(page_title="Desafio análise de dados Covid", page_icon="🏥")

st.title("Análise COVID-19")

st.markdown(
    """
    Este dashboard interativo apresenta uma análise abrangente da evolução da pandemia de COVID-19 nos Estados Unidos, com base nos dados públicos disponibilizados pelo *The New York Times* ([GitHub - NYT COVID-19 Data](https://github.com/nytimes/covid-19-data)).

    A plataforma oferece visualizações dinâmicas e filtros personalizados que permitem explorar:

    * **Gráficos de linha e barra** com a evolução diária e acumulada de casos e óbitos por estado e condado.
    * **Tabelas interativas** com opções de busca e ordenação para facilitar comparações regionais.
    * **Filtros por período, estado e tipo de dado (casos/óbitos)** para análises específicas.
    * **Mapas temáticos** (se aplicável) com distribuição geográfica dos dados ao longo do tempo.

    O objetivo é proporcionar uma visão clara, acessível e explorável da pandemia, apoiando estudos, decisões e reflexões com base em dados confiáveis.
    """
)

st.header("Histórico de buscas")
history = db.get_history()
st.write(history.data)
