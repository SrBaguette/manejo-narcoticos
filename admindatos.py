import pandas as pd
import matplotlib.pyplot as plt
class AdminDatos:
    @staticmethod
    def leer_csv(archivocsv):
        return pd.read_csv(archivocsv)