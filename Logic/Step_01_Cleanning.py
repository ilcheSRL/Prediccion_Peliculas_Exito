import pandas as pd

class CleaningTransformer:
    def Cleaning_Data(self, df: pd.DataFrame, preview_rows: int = 5) -> pd.DataFrame:
        """
        Punto inicial de integración.
        Por ahora, solo muestra un preview (display) y retorna el DataFrame sin cambios.
        """
 
         
        df = df.loc[df["periodo"] > 202310].copy()
        df = df
        print("🔄  Check  Step_1 --> 📊")
      
        return df
