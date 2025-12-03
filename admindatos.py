import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)

    @staticmethod
    def mayor_incautacion(df):
        return df.loc[df["departamento","dosis_g"].idxmax()]
        

    @staticmethod
    def menor_incautacion(df):
        return df.loc[df["dosis_g"].idxmin()]
        

    
    