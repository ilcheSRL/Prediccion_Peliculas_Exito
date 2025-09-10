import pandas as pd

class IntegrationTransformer:
    def Cleaning_Data(self, df: pd.DataFrame, preview_rows: int = 5) -> pd.DataFrame:
        """
        Punto inicial de integración.
        Por ahora, solo muestra un preview (display) y retorna el DataFrame sin cambios.
        """
        df = df[df["periodo"] > 202301]


      
        return df
