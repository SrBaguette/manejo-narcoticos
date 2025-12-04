import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)

    @staticmethod
    def mayor_departamento(df):
        conteo = df.groupby('departamento').size()
        depto_max = conteo.idxmax()
        dosis_max = df[df['departamento'] == depto_max]['dosis_g'].max()
        print("Departamento con mayor incautación:")
        print(f"Departamento: {depto_max}")
        print(f"Dosis: {dosis_max}")
        return depto_max, dosis_max

    @staticmethod
    def menor_departamento(df):
        conteo = df.groupby('departamento').size()
        depto_min = conteo.idxmin()
        dosis_min = df[df['departamento'] == depto_min]['dosis_g'].min()
        print("Departamento con menor incautación:")
        print(f"Departamento: {depto_min}")
        print(f"Dosis: {dosis_min}")
        return depto_min, dosis_min
            

    
    