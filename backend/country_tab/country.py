import config
import os
from backend.country_tab.existing_country import show

def clear_layout(layout):
    if layout is None:
        return
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.setParent(None)
            widget.deleteLater()
        else:
            clear_layout(item.layout())

def holderFunc():
    pass

def new_country(widget):
    widget.setText(f'{config.NEW_COUNTRY_BUTTON_TEXT}')
    if config.MOD_DIRECTORY == "null":
        widget.setText(f'{config.NEW_COUNTRY_BUTTON_TEXT} (Select a directory!)')
        return 0
    
def load_countries(parent_layout):
    clear_layout(parent_layout)
    country_files = os.listdir(f'{config.HISTORY_DIRECTORY}\\countries')
    country_dict = {}
    for i, v in enumerate(country_files):
        v = v.removesuffix(".txt")
        v_list = v.split(" - ")
        country_dict[v_list[0]] = v_list[1]
    config.COUNTRY_DICTIONARY = country_dict
    for key, value in country_dict.items():
        show(parent_layout, key, value)

def done_button(name_input, capitol_input, tag):
    data = []
    with open(f'{config.LOCALISATION_DIRECTORY}\\country_{config.SELECTED_TAG}_l_{config.MOD_LANG}.yml', 'r') as file:
        data = file.readlines()
    with open(f'{config.LOCALISATION_DIRECTORY}\\country_{config.SELECTED_TAG}_l_{config.MOD_LANG}.yml', 'w') as file:
        for i, v in enumerate(data):
            if f"{config.SELECTED_TAG}_{config.NEUTRALITY_IDEOLOGY}: " in v:
                file.write(f"{config.SELECTED_TAG}_{config.NEUTRALITY_IDEOLOGY}: \"{name_input.text()}\"\n")
            else:
                file.write(v)
    with open(f'{config.COUNTRY_DIRECTORY}', 'r') as file:
        data = file.readlines()
    with open(f'{config.COUNTRY_DIRECTORY}', 'w') as file:
        for i, v in enumerate(data):
            if f"capital = {config.COUNTRY_CAPITOL}" in v:
                file.write(f"capital = {capitol_input.text()}\n")
            else:
                file.write(v)
    #next do tag input (lowk forget where I set tags but I'll thug it out)