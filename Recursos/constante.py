# project/constants.py

import os

# Directorio base del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas a los archivos CSV de entrada
RESOURCES_DIR = os.path.join(BASE_DIR, '')
Data_N1 = os.path.join(RESOURCES_DIR, 'master_df.csv')
Data_N2 = os.path.join(RESOURCES_DIR, 'Base_Movie_Princial.csv')

