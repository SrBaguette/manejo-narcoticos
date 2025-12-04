from admindatos import AdminDatos
import matplotlib.pyplot as plt
import pandas as pd

class Graficas:
    @staticmethod
    def pormesgra(df):
        df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
        mensual = df.groupby(df['fecha'].dt.to_period('D'))["dosis_g"].sum()
        plt.figure(figsize=(10,5))
        mensual.plot(kind='bar')
        plt.xlabel('Dia')
        plt.ylabel('Gramos incautados')
        plt.title('Incautaciones por dias')
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def Grafica_quartiles(df):
        plt.figure(figsize=(10, 7))
        plt.boxplot(df["dosis_g"])
        plt.yscale("log") 
        plt.title("Caja y Bigotes (Escala Logarítmica)")
        plt.ylabel("dosis_g (log)")
        plt.show()


    @staticmethod
    def Grafica_Departamento_Mayor(df):
        datos = df.groupby('departamento')['dosis_g'].max().sort_values().tail(10)
        datos.plot(kind='bar', title='Dosis incautada por departamento')
        plt.xlabel('Departamento')
        plt.ylabel('Dosis_g')
        plt.tight_layout()
        plt.show()

    @staticmethod
    def Grafica_Departamento_Menor(df):
        datos = df.groupby('departamento')['dosis_g'].min().sort_values().tail(10)
        datos.plot(kind='bar', title='Dosis incautada por departamento')
        plt.xlabel('Departamento')
        plt.ylabel('Dosis_g')
        plt.tight_layout()
        plt.show()

    def GraficaMunicipios_Mayor(df):
        datos = df.groupby('municipio')['dosis_g'].max().sort_values().tail(10)
        datos.plot(kind='bar', title='Dosis incautada por municipio')
        plt.xlabel('Municipio')
        plt.ylabel('Dosis_g')
        plt.tight_layout()
        plt.show()
        
        
    @staticmethod
    def GraficaMunicipios_Menor(df):
        datos = df.groupby('municipio')['dosis_g'].min().sort_values().tail(10)
        datos.plot(kind='bar', title='Dosis incautada por municipio')
        plt.xlabel('Municipio')
        plt.ylabel('Dosis_g')
        plt.tight_layout()
        plt.show()
        
        
        
        