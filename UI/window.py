#(SOME OF) THIS CODE IS BORROWED FROM https://github.com/Thomas-Holtvedt/opengs-maptool/, ANOTHER GREAT TOOL FOR HOI4 MODDING
import config
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QTabWidget, QLabel
from UI.buttons import create_slider, create_button, create_checkbox, create_line_edit
from backend.test import test_func

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # MAIN LAYOUT
        self.setWindowTitle(config.TITLE)
        self.resize(config.WINDOW_SIZE_WIDTH,
                    config.WINDOW_SIZE_HEIGHT)
        main_layout = QVBoxLayout(self)
        self.setLayout(main_layout)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs, stretch=1)

        self.progress = QProgressBar()
        self.progress.setVisible(False)
        main_layout.addWidget(self.progress)
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.setValue(0)

    #test tab
        self.test_tab = QWidget()
        self.tabs.addTab(self.test_tab, "test")
        test_tab_layout = QVBoxLayout(self.test_tab)
        test_tab_layout.addStretch()
        self.test_button = create_button(test_tab_layout, "Test", lambda: test_func("Hello World!", "test"))