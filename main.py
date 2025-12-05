import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt5.QtGui import QIcon,QFont
from admindatos import AdminDatos
df=AdminDatos.leer_csv("encautaciones_de_drogas.csv")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Incautaciones de Narcoticos")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("icon.png"))
        self.initUI()
    def initUI(self):
        self.button=QPushButton("Estadistias Generales",self)
        self.button.setGeometry(150,200,200,100)
        self.button.clicked.connect(self.on_click)
    def on_click(self):
        self.stats_window=StatsWindow(df)
        self.stats_window.show()

class StatsWindow(QWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Estadisticas Generales")
        self.setGeometry(800, 350, 500, 500)
        self.setWindowIcon(QIcon("icon.png"))

        text = AdminDatos.EstadisticasGUI(self.df)

        label = QLabel(text, self)
        label.setWordWrap(True)
        label.setGeometry(10, 10, 480, 480)
        label.setFont(QFont("Arial", 8))
        label.setStyleSheet("color:blue; background:gray")


def main():
    app =QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
def otherwindow(self):
    self.setWindowTitle("Incautaciones de Narcoticos")
    self.setGeometry(700,300,500,500)
    self.setWindowIcon(QIcon("icon.png"))
    label=QLabel(AdminDatos.EstadisticasGUI(df),self)
    label.setWordWrap(True)
    label.setGeometry(0,0,500,200)
    label.setFont(QFont("Arial",8))
    label.setStyleSheet("color:blue;background:gray")
if __name__=="__main__":
    main()