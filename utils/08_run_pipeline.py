from constante import Data_N1
from utils.utils import Utils
from business_logic.integration import IntegrationTransformer

def run_pipeline():
    # Paso 1: Lectura de datos con Utils
    customers = Utils.load_table(Data_N1)

    # Paso 2: Integración
    df = IntegrationTransformer().integrate_data(customers)

    return df
