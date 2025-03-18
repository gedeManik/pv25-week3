import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week 3 - (F1D022046 - I Gede Manik Ariyasa)")
        self.setGeometry(100, 100, 400, 300)

        self.label = QLabel("x: 0, y: 0", self)
        self.label.setGeometry(50, 50, 100, 20)

        self.setMouseTracking(True)  
        #setMouseTracking label ini agar saat cursor berada di label maka label akan dipindah random
        self.label.setMouseTracking(True)

    #mouseMoveEvent ada di QWidget
    def mouseMoveEvent(self, event):
        self.label.setText(f"x: {event.x()}, y: {event.y()}")

        #jika cursor menyentuh label maka label dipindah random
        if self.label.geometry().contains(event.pos()):
            self.move_label_randomly()

    def move_label_randomly(self):
        x = random.randint(0, self.width() - self.label.width())
        y = random.randint(0, self.height() - self.label.height())
        self.label.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())
