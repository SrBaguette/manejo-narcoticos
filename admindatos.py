import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)
    
    @staticmethod
    def mayor_municipio(df):
        conteo = df['municipio'].value_counts()
        municipio_top = conteo.idxmax()
        dosis_municipio = df[df['municipio'] == municipio_top]['dosis_g'].sum()

        print("Municipio con mayor incautacion: ")
        print(f"Municipio: {municipio_top}")
        print(f"Dosis: {dosis_municipio}")

        return municipio_top, dosis_municipio
    
    @staticmethod
    def menor_departamento(df):
        conteo = df['departamento'].value_counts()
        departamento_top = conteo.idxmax()
        dosis_departamento = df[df['departamento'] == departamento_top]['dosis_g'].min()

        print("Departamento con menor incautacion: ")
        print(f"Departamento: {departamento_top}")
        print(f"Dosis: {dosis_departamento}")

        return departamento_top, dosis_departamento






    

