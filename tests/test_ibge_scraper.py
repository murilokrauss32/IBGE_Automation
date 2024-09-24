import unittest
import pandas as pd
from scripts.ibge_scraper import IBGEScraper

class TestIBGEScraper(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.scraper = IBGEScraper()

    def test_extract_state_info(self):
        estado = 'sp'
        state_info = self.scraper.extract_state_info(estado)
        self.assertIsInstance(state_info, dict)
        self.assertIn('Governador', state_info)
        self.assertEqual(state_info['Estado'], 'SP')

    def test_process_states(self):
        estados = ['sp', 'rj']
        dataframe = self.scraper.process_states(estados)
        self.assertIsInstance(dataframe, pd.DataFrame)
        self.assertEqual(len(dataframe), 2)
        self.assertIn('Governador', dataframe.columns)
        self.assertIn('Estado', dataframe.columns)
    
    def test_clean_data(self):
        # Simulating a dataframe with dirty data
        data = {
            'Governador': ['Nome Teste'],
            'População': ['10.000.000 pessoas'],
            'Área (km²)': ['123.456 km²'],
            'Densidade Demográfica (hab/km²)': ['80 hab/km²'],
            'Estado': ['SP']
        }
        df = pd.DataFrame(data)
        clean_df = self.scraper.clean_data(df)
        
        self.assertEqual(clean_df['População'][0], '10.000.000')
        self.assertEqual(clean_df['Área (km²)'][0], '123.456')
        self.assertEqual(clean_df['Densidade Demográfica (hab/km²)'][0], '80')

    def test_save_to_json(self):
        data = {
            'Governador': ['Nome Teste'],
            'População': ['10.000.000'],
            'Estado': ['SP']
        }
        df = pd.DataFrame(data)
        filename = "test_dados_estados.json"
        self.scraper.save_to_json(df, filename)
        
        # Verifying that the JSON file was created successfully
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('"Governador": "Nome Teste"', content)
            self.assertIn('"Estado": "SP"', content)

if __name__ == "__main__":
    unittest.main()
