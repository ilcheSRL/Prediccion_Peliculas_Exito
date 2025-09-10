import pandas as pd

class IntegrationTransformer:
    def integrate_data(self, df: pd.DataFrame, preview_rows: int = 5) -> pd.DataFrame:
        """
        Punto inicial de integración.
        Por ahora, solo muestra un preview (display) y retorna el DataFrame sin cambios.
        """
        
        print(df.head(preview_rows))
        return df
