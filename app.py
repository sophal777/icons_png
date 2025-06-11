import os
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout,
    QFrame, QPushButton, QGraphicsDropShadowEffect
)
from PyQt5.QtCore import Qt, QPoint

class CustomLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom GUI Layout")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Main horizontal layout
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Left vertical layout
        left_layout = QVBoxLayout()

        # Top left widget (e.g. controls)
        top_left = QFrame()
        top_left.setStyleSheet("background-color: #222; border: 1px solid yellow;")
        top_left.setFixedHeight(90)
        top_left_layout = QHBoxLayout()
        top_left_layout.setContentsMargins(10, 10, 10, 10)

        self.exit_button = QPushButton("❌ Exit")
        self.settings_button = QPushButton("⚙ Settings")
        self.shutdown_button = QPushButton("⏻ Shutdown")

        # Optional: Style buttons
        for btn in [self.exit_button, self.settings_button, self.shutdown_button]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #444;
                    color: white;
                    border: none;
                    padding: 6px 10px;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #666;
                }
            """)
            top_left_layout.addWidget(btn)

        top_left.setLayout(top_left_layout)

        # Bottom left widget
        bottom_left = QFrame()
        bottom_left.setStyleSheet("background-color: #111; border: 1px solid yellow;")

        # Add top and bottom to left layout
        left_layout.addWidget(top_left)
        left_layout.addWidget(bottom_left)

        # Right widget (main content area)
        right_frame = QFrame()
        right_frame.setStyleSheet("background-color: #000; border: 1px solid yellow;")

        # Add shadow effect (optional)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setOffset(0, 0)
        self.setGraphicsEffect(shadow)

        # Add to main layout
        main_layout.addLayout(left_layout, 1)
        main_layout.addWidget(right_frame, 2)

        self.setLayout(main_layout)

        # Connect button signals
        self.exit_button.clicked.connect(self.close)
        self.shutdown_button.clicked.connect(self.shutdown_system)
        self.settings_button.clicked.connect(self.open_settings)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, "dragging") and self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    def shutdown_system(self):
        print("Shutdown triggered")
        # os.system("shutdown /s /t 1")  # Uncomment to shutdown (Windows)

    def open_settings(self):
        print("Settings window would open here.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomLayout()
    window.show()
    sys.exit(app.exec_())
