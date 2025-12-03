import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)
    @staticmethod
    def buscarpordane(df,codigo):
        resultados = df[df["codigo_dane"] == codigo]
        if resultados.empty:
            print("No se encontró ningún registro con ese código.")
        else:
            print(resultados)