from admindatos import AdminDatos
import matplotlib.pyplot as plt
class Graficas:
    pass
 
    @staticmethod
    def Grafica_quartiles(df):
        plt.figure(figsize=(10, 7))
        plt.boxplot(df["dosis_g"])
        plt.yscale("log") 
        plt.title("Caja y Bigotes (Escala Logarítmica)")
        plt.ylabel("dosis_g (log)")
        plt.show()

