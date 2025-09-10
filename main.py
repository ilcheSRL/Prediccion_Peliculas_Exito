

from utils.utils import Utils
from Logic.Step_00_integration import IntegrationTransformer
from Recursos.constante import (Data_N1)
 

def run_pipeline():
    # Paso 1: Lectura de datos con Utils
    customers = Utils.load_table(Data_N1)

    # Paso 2: Integración
    df = IntegrationTransformer().integrate_data(customers)
    display(df)

    return df
