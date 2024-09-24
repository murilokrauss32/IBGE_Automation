from scripts.ibge_scraper import IBGEScraper

def main() -> None:
    scraper = IBGEScraper()
    estados = ['al', 'rn', 'ba', 'sp', 'rj', 'df', 'es', 'go', 'mg', 'pa', 'pb']
    dados_estados = scraper.process_states(estados)
    dados_limpos = scraper.clean_data(dados_estados)
    scraper.save_to_json(dados_limpos, "data/results.json")

if __name__ == "__main__":
    main()

