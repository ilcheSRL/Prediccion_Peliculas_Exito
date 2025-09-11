import pandas as pd

class Utils:
    @staticmethod
    def load_table(path: str) -> pd.DataFrame:
 
            df = pd.read_csv(path)
 
            return df
       
    def load_table_csv(path: str) -> pd.DataFrame:
 
            df = pd.read_csv(path, header = True, Sep = ",")
 
            return df
