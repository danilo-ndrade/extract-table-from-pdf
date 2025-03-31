import logging

def process_dataframe(df, csv_path):
    """Manipula dataframe com modificações necessárias e salva em CSV."""
    try:
        logging.info("Processando DataFrame: renomeando colunas e salvando como CSV")
        df = df.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'})
        df.to_csv(csv_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Erro ao processar DataFrame: {e}")