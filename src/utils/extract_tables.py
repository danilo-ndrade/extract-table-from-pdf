import pandas as pd
import tabula
import logging

def extract_tables(pdf_path, pages):
    try:
        logging.info(f"Extraindo tabelas do PDF: {pdf_path}, páginas: {pages}")
        tables = tabula.read_pdf(pdf_path, pages=pages, lattice=True, multiple_tables=True)
        if not tables:
            logging.error(f"Nenhuma tabela encontrada no PDF: {pdf_path}")
            return None
        return pd.concat(tables, ignore_index=True)
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair tabelas do PDF: {e}")