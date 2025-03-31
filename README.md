# Script para extração de tabelas em format PDF e conversão para CSV.
Script em python que utiliza tabula-py para extrair tabela de um pdf e converter em csv.

---

## Observações

- O tabula foi escolhido por ter apresentado o melhor resultado entre as opções de pacotes que extraem tabelas de arquivos PDFs. O tabula-py se trata de wrapper do tabula-java, por isso **é necessário que o java esteja instalado na máquina que vai executar o script**.

---

## Funcionalidades

- Extrai tabela contida no pdf indicado utilizando tabula.
- Processa tabela extraída(dataframe) renomeando duas colunas e convertendo em CSV.
- Compacta arquivo CSV no formato ZIP.


---

## Requisitos

- Python 3.12 ou superior
- **Java**, para funcionamento do tabula.
- Dependências listadas no arquivo requirements.txt.

---

## Execução do script

1. **Crie o ambiente virtual python**
  - python3 -m venv venv
  - source venv/bin/activate  # Linux/Mac
  - venv\Scripts\activate     # Windows

2. **Instale as dependências**
   - pip install -r requirements.txt

3. **Execute o script**
   - python src/main.py
