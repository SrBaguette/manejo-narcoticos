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
    @staticmethod
    def Graficas_Todas(df):
        fig, axs = plt.subplots(2, 3, figsize=(20, 10))
        axs = axs.flatten()
       # ------------------------------
        ax = axs[0]
        df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
        mensual = df.groupby(df['fecha'].dt.to_period('D'))["dosis_g"].sum()
        mensual.plot(kind='bar', ax=ax)
        ax.set_xlabel('Día')
        ax.set_ylabel('Gramos incautados')
        ax.set_title('Incautaciones por día')
        # ------------------------------
        ax = axs[1]
        ax.boxplot(df["dosis_g"])
        ax.set_yscale("log")
        ax.set_title("Caja y Bigotes (Escala Logarítmica)")
        ax.set_ylabel("dosis_g (log)")
        # ------------------------------
        ax = axs[2]
        datos = df.groupby('departamento')['dosis_g'].max().sort_values().tail(10)
        datos.plot(kind='bar', ax=ax)
        ax.set_title('Departamentos con mayor dosis incautada')
        ax.set_xlabel('Departamento')
        ax.set_ylabel('dosis_g')
        # ------------------------------
        ax = axs[3]
        datos = df.groupby('departamento')['dosis_g'].min().sort_values().tail(10)
        datos.plot(kind='bar', ax=ax)
        ax.set_title('Departamentos con menor dosis incautada')
        ax.set_xlabel('Departamento')
        ax.set_ylabel('dosis_g')
        # ------------------------------    
        ax = axs[4]
        datos = df.groupby('municipio')['dosis_g'].max().sort_values().tail(10)
        datos.plot(kind='bar', ax=ax)
        ax.set_title('Municipios con mayor dosis incautada')
        ax.set_xlabel('Municipio')
        ax.set_ylabel('dosis_g')
        # ------------------------------
        ax = axs[5]
        datos = df.groupby('municipio')['dosis_g'].min().sort_values().tail(10)
        datos.plot(kind='bar', ax=ax)
        ax.set_title('Municipios con menor dosis incautada')
        ax.set_xlabel('Municipio')
        ax.set_ylabel('dosis_g')

        plt.tight_layout()
        plt.show()
            
            
        
        