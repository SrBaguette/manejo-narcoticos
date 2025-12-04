from admindatos import AdminDatos
from matplotlib import pyplot as plt
class Graficas:
    pass

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
    
    
