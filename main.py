

from utils.utils import Utils
from Logic.Step_00_integration import IntegrationTransformer
from Logic.Step_01_Cleanning import CleaningTransformer
from Logic.Step_02_Feature_Engenierring import FeatureEngenieringTransformer
from Recursos.constante import (Data_N1)
 

def run_pipeline():
    # Paso 1: Lectura de datos con Utils
    customers = Utils.load_table(Data_N1)

    # Paso 2: Integración
    df = IntegrationTransformer().integrate_data(customers)
    df = CleaningTransformer().Cleaning_Data(df)
    df = FeatureEngenieringTransformer().Feature_Step_001_Data(df)

    return df
 
if __name__ == "__main__":
    run_pipeline()
