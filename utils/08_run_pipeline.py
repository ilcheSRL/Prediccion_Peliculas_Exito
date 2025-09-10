

from utils.00_utils import Utils
from business_logic.integration import IntegrationTransformer
from constante import (Data_N1)

utils/00_utils 

def run_pipeline():
    # Paso 1: Lectura de datos con Utils
    customers = Utils.load_table(Data_N1)

    # Paso 2: Integración
    df = IntegrationTransformer().integrate_data(customers)

    return df
