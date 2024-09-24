import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
from typing import List

class IBGEScraper:
    def __init__(self, headless: bool = True):
        self.base_url = "https://www.ibge.gov.br/cidades-e-estados/"

    def extract_state_info(self, state: str) -> dict:
        state_url = f"{self.base_url}{state}.html"
        response = requests.get(state_url)
        soup = BeautifulSoup(response.content, "html.parser")
        indicators = soup.select('.indicador')
        state_info = {
            ind.select('.ind-label')[0].text.strip(): ind.select('.ind-value')[0].text.strip().split('   ')[0]
            for ind in indicators
        }
        state_info['Estado'] = state.upper()
        return state_info

    def process_states(self, states: List[str]) -> pd.DataFrame:
        data = [self.extract_state_info(state) for state in states]
        dataframe = pd.DataFrame(data)
        dataframe.columns = [
            'Governador', 'Capital', 'Gentílico', 'Área (km²)', 'População', 
            'Densidade Demográfica (hab/km²)', 'Matrículas no Ensino Fundamental', 
            'IDH', 'Receitas (R$)', 'Despesas (R$)', 'Rendimento Per Capita (R$)', 
            'Total de Veículos', 'Estado'
        ]
        return dataframe

    def clean_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe.replace({
            ',': '.', ' hab/km²': '', ' km²': '', ' pessoas': '', ' matrículas': '', 
            ' veículos': '', 'R\$.*': ''
        }, regex=True, inplace=True)
        return dataframe

    def save_to_json(self, dataframe: pd.DataFrame, filename: str) -> None:
        dataframe.to_json(filename, orient='records', lines=True, force_ascii=False)
        print(f"Dados salvos em {filename}.")
