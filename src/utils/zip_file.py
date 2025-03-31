import zipfile
import os
import logging

def zip_file(csv_path, zip_path):
    try:
        logging.info(f"Compactando arquivo {csv_path} para {zip_path}")
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            zip_file.write(csv_path, os.path.basename(csv_path))
        return True
    except Exception as e:
        logging.error(f"Erro ao criar arquivo zip: {e}")