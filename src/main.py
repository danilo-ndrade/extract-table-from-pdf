import logging
from pathlib import Path
from utils.extract_tables import extract_tables
from utils.process_dataframe import process_dataframe
from utils.zip_file import zip_file

"""Config para logs"""
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RAIZ = Path(__file__).resolve().parent.parent

PDF_PATH = RAIZ / 'data' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'
CSV_PATH = RAIZ / 'data' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.csv'
ZIP_PATH = RAIZ / 'data' / 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.zip'
PAGES = '3-181'

def main():
    try:
        logging.info("Iniciando o processo.")
        df = extract_tables(PDF_PATH, PAGES)
        if df is None:
            raise ValueError("Nenhuma tabela foi extraída do PDF.")
        
        process_dataframe(df, CSV_PATH)  # Agora lança erro em caso de falha
        zip_file(CSV_PATH, ZIP_PATH)
        
        logging.info("Processo concluído com sucesso.")
    except Exception as e:
        logging.error(f"Erro no processo: {e}")

if __name__ == "__main__":
    main()