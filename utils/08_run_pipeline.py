import pandas as pd
from Logic._00_Integracion import IntegrationTransformer
from project.constants import Data_N1  # importar la constante con la ruta

def run_pipeline():
    # Leer el DataFrame desde constants.py
    df = pd.read_csv(Data_N1)

    # Paso 1: Integración
    df = IntegrationTransformer().integrate_data(df)

    # Mostrar resultado
    print("=== DataFrame Integrado ===")
    print(df.head())  # primeras filas

if __name__ == "__main__":
    run_pipeline()

