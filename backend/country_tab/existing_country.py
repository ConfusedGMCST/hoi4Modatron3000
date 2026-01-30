import config
from frontend.buttons import create_button
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QTabWidget, QLabel

#Creates the existing_country object on the right side of the country tab
def show(parent_layout, tag, name):
    vertical_container = QVBoxLayout()
    entry_layout = QHBoxLayout()
    tag_label = QLabel(tag)
    name_label = QLabel(name)

    entry_layout.addWidget(tag_label)
    entry_layout.addWidget(name_label)

    tag_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    name_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    vertical_container.addLayout(entry_layout)
    parent_layout.addLayout(vertical_container)
    vertical_container.addStretch()
    vertical_container.setObjectName(config.COUNTRY_CONTAINER_NAME)