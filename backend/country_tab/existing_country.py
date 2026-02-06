import config
from frontend.buttons import create_button
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QProgressBar, QTabWidget, QLabel

#Creates the existing_country object on the right side of the country tab
def show(parent_layout, tag, name):
    vertical_container = QVBoxLayout()
    entry_layout = QHBoxLayout()
    tag_label = create_button(entry_layout, tag, lambda: set_tag(tag))
    name_label = QLabel(name)

    entry_layout.addWidget(tag_label)
    entry_layout.addWidget(name_label)

    name_label.setAlignment(Qt.AlignmentFlag.AlignRight)
    vertical_container.addLayout(entry_layout)
    parent_layout.addLayout(vertical_container)
    vertical_container.addStretch()
    vertical_container.setObjectName(config.COUNTRY_CONTAINER_NAME)

def set_tag(tag):
    config.SELECTED_TAG = tag
    config.COUNTRY_DIRECTORY = f'{config.HISTORY_DIRECTORY}\\countries\\{config.SELECTED_TAG} - {config.COUNTRY_DICTIONARY[tag]}.txt'
    with open(f'{config.COUNTRY_DIRECTORY}', 'r') as file:
        data = file.readlines()
        new_data = []
        for i, v in enumerate(data):
            v = v.removesuffix("\\n")
            v = v.removeprefix("\\t")
            new_data.append(v)
        for i, v in enumerate(new_data):
            if "capital" in v:
                mod_text = v.split(" ")
                config.COUNTRY_CAPITOL = mod_text[2]
        config.COUNTRY_TAG_INPUT.setText(tag)
        config.COUNTRY_CAPITOL_INPUT.setText(config.COUNTRY_CAPITOL)
    with open(f'{config.LOCALISATION_DIRECTORY}\\country_{tag}_l_{config.MOD_LANG}.yml', 'r') as file:
        data = file.readlines()
        new_data = []
        for i, v in enumerate(data):
            v = v.strip()
            new_data.append(v)
        for i, v in enumerate(new_data):
            if f"{tag}_{config.NEUTRALITY_IDEOLOGY}: " in v:
                text = v.split(":")
                text[1] = text[1].strip()
                text[1] = text[1].split("\"")
                print(text[1])
                config.COUNTRY_NAME_TEXT = text[1][1]
                #Excuse the UNREADABILITY of this code, I apologize - all this does is separate the localisation file's line into several parts to extract the actual value we're looking for, the country name
        config.COUNTRY_NAME_INPUT.setText(config.COUNTRY_NAME_TEXT)

def search(text):
    try:
        print(config.COUNTRY_DICTIONARY[text])
    except KeyError:
        print("Invalid search!")