#(SOME OF) THIS CODE IS BORROWED FROM https://github.com/Thomas-Holtvedt/opengs-maptool/, ANOTHER GREAT TOOL FOR HOI4 MODDING
import config
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QTabWidget, QLabel
from PyQt6.QtGui import QFont
from UI.buttons import create_slider, create_button, create_checkbox, create_line_edit
from backend.general import open_file_dialog

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

    #startup/general tab
        self.general_tab = QWidget()
        self.tabs.addTab(self.general_tab, config.GENERAL_LABEL_TEXT)
        general_tab_layout = QVBoxLayout(self.general_tab)
        self.general_label = QLabel(config.GENERAL_LABEL_TEXT)
        font = QFont()
        font.setPointSize(config.GENERAL_LABEL_FONT_SIZE)
        self.general_label.setFont(font)
        general_tab_layout.addWidget(self.general_label)
        general_tab_layout.addStretch()
        create_button(general_tab_layout, "Import Mod", lambda: open_file_dialog(self, self.general_tab, general_tab_layout))
        # self.test_button = create_button(test_tab_layout, "Test", lambda: test_func("Hello World!", "test"))