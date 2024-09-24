# IBGE Automation

Este projeto realiza a automação de consultas no site do IBGE utilizando Selenium, Requests e BeautifulSoup, salvando os dados coletados em um arquivo JSON.

## Dependências
- pandas
- requests
- beautifulsoup4
- unittest

## Como executar
1. Clone o repositório:
    ```
    git clone https://github.com/seuusuario/IBGE_Automation.git
    ```
2. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```
3. Execute o script principal:
    ```
    python scripts/main.py
    ```

4. Para rodar os testes:
    ```
    python -m unittest discover tests
    ```

## Estrutura do Projeto
- `scripts/`: Contém os scripts principais do projeto.
- `data/`: Diretório onde os dados coletados serão salvos.
- `tests/`: Contém os testes automatizados para garantir a robustez do código.
