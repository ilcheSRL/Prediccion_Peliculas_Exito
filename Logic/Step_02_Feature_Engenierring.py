
import pandas as pd

class FeatureEngenieringTransformer:
    def Feature_Step_001_Data(self, df: pd.DataFrame, preview_rows: int = 5) -> pd.DataFrame:
        """
        Punto inicial de integración.
        Por ahora, solo muestra un preview (display) y retorna el DataFrame sin cambios.
        """

        
        #df["periodo"] = pd.to_numeric(df["periodo"], errors="coerce")
        #df = df[df["target"] == 1]

        print("🔄  Check  Step_2 --> INGENIERIA DE VARIABLES📊")
        display(df.head())

      
        return df
