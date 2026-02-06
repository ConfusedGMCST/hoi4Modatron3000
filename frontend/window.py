#(SOME OF) THIS CODE IS BORROWED FROM https://github.com/Thomas-Holtvedt/opengs-maptool/, ANOTHER GREAT TOOL FOR HOI4 MODDING
import config
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QTabWidget, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from frontend.buttons import create_slider, create_button, create_checkbox, create_line_edit
from backend import general
from backend.country_tab import country, existing_country

class Window(QWidget):
    def __init__(self):
        super().__init__()

        title_font = QFont()
        title_font.setPointSize(config.TITLE_FONT_SIZE)
        label_font = QFont()
        label_font.setPointSize(config.LABEL_FONT_SIZE)

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
        self.general_label.setFont(title_font)
        general_tab_layout.addWidget(self.general_label)

        self.startup_label = QLabel("Select your mod directory to get started!")
        self.startup_label.setFont(label_font)
        general_tab_layout.addWidget(self.startup_label)

        general_tab_layout.addStretch()

        create_button(general_tab_layout, "Import Mod", lambda: general.open_file_dialog(self, self.general_tab, general_tab_layout))
        
    #country maker tab
        self.country_tab = QWidget()
        self.tabs.addTab(self.country_tab, config.COUNTRY_LABEL_TEXT)
        country_tab_layout = QVBoxLayout(self.country_tab)

        self.country_label = QLabel(config.COUNTRY_LABEL_TEXT)
        self.country_label.setFont(title_font)
        country_tab_layout.addWidget(self.country_label)

        country_tab_sub_layout_1 = QHBoxLayout()
        country_tab_layout.addLayout(country_tab_sub_layout_1)

        country_properties_layout = QVBoxLayout()
        country_existing_countries_list = QVBoxLayout()

        country_tab_sub_layout_1.addLayout(country_properties_layout)
        country_tab_sub_layout_1.addLayout(country_existing_countries_list)

        new_country_button = create_button(country_properties_layout, config.NEW_COUNTRY_BUTTON_TEXT, lambda: country.new_country(new_country_button))
        existing_countries_label = QLabel("Existing Countries")

        existing_countries_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        country_existing_countries_list.addWidget(existing_countries_label)
        country_existing_sublist = QVBoxLayout()
        
        countries_load_search = create_line_edit(country_existing_countries_list, "Search")
        countries_search_button = create_button(country_existing_countries_list, "Search", lambda: existing_country.search(countries_load_search.text()))
        countries_load_list = create_button(country_existing_countries_list, "Load Existing Countries", lambda: country.load_countries(country_existing_sublist))
        country_name_input = create_line_edit(country_properties_layout, config.COUNTRY_NAME_TEXT)
        country_tag_input = create_line_edit(country_properties_layout, config.COUNTRY_TAG_TEXT)
        country_capitol_input = create_line_edit(country_properties_layout, config.COUNTRY_CAPITOL)

        config.COUNTRY_CAPITOL_INPUT = country_capitol_input
        config.COUNTRY_NAME_INPUT = country_name_input
        config.COUNTRY_TAG_INPUT = country_tag_input

        country_existing_countries_list.addLayout(country_existing_sublist)
        country_properties_layout.addStretch()
        country_existing_countries_list.addStretch()
        country_tab_layout.addStretch()