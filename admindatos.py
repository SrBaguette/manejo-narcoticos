import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)
    
    @staticmethod
    def Estadisticas(df):
        Maxima_dosis = df["dosis_g"].max()
        Minima_dosis = df["dosis_g"].min()
        Promedio_dosis = df["dosis_g"].mean()
        Desviacion_estandar = df["dosis_g"].std()
        Conteo_de_dosis = df["dosis_g"].count()
        Quartil_1 = df["dosis_g"].quantile(0.25)
        Quartil_2 = df["dosis_g"].quantile(0.50)
        Quartil_3 = df["dosis_g"].quantile(0.75)

        print("La maxima incautancion de droga es :",Maxima_dosis)
        print("La minima incautancion de droga es :",Minima_dosis)
        print("El promedio incautancion de droga es :",Promedio_dosis)
        print("La desviacion estandar de incautacion de droga es: ",Desviacion_estandar) 
        print("El total de dosis incautadas es : ",Conteo_de_dosis)
        print("El primer Quartil de droga incautada es :",Quartil_1)
        print("El segundo Quartil de droga incautada es :",Quartil_2)
        print("El tercer Quartil de droga incautada es :",Quartil_3)
