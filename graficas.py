from admindatos import AdminDatos
import pandas as pd
import matplotlib.pyplot as plt
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