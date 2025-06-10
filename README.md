# icons_png


https://github.com/sophal777/icons_png/commit/443a0221a1c234b37e6f7d3d54fc8b5b6754d79c


CODE 


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import urllib.request

class IconWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Load PNG from GitHub URL")
        self.init_ui()

    def init_ui(self):
        url = "https://raw.githubusercontent.com/sophal777/icons_png/main/home.png"

        # Download image data from URL
        image_data = urllib.request.urlopen(url).read()

        # Load image data into QPixmap
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        label = QLabel()
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = IconWindow()
    window.show()
    sys.exit(app.exec_())
