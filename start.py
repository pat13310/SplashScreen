from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from spalsh.splash import Ui_Splash
import sys

# GLOBAL

progress_count = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
        # suppression de la barre des titres
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # effet ombrage

        #     self.shadow=QGraphicsDropShadowEffect(self)
        #     self.shadow.setBlurRadius(20)
        #     self.shadow.setXOffset(2)
        #     self.shadow.setYOffset(2)
        #     self.shadow.setColor(QColor(0,0,0,190))
        #     self.ui.frame.setGraphicsEffect(self.shadow)

        # QTIMER => START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progressbar)
        self.timer.start(250)

    def update_progressbar(self):
        global progress_count
        self.ui.progressBar.setValue(progress_count)

        if progress_count == 20:
            self.ui.label_information.setText("Chargement des modules ...")

        if progress_count == 30:
            self.ui.label_information.setText("Chargement des dictionnaires ...")

        if progress_count == 50:
            self.ui.label_information.setText("Chargement des applications ...")

        if progress_count > 100:
            self.timer.stop()
            self.close()

        progress_count += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = SplashScreen()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
