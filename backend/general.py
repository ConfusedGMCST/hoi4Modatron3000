#for import mod button
import config
from PyQt6.QtWidgets import QFileDialog, QLabel, QWidget, QVBoxLayout

def open_file_dialog(self, parent_object, layout):
    folder_dir = QFileDialog.getExistingDirectory(
        self,
        "Select a Folder",
        ""  # Starting directory (empty = home)
    )
    if folder_dir:
        #Sets all the proper directory config variables
        config.MOD_DIRECTORY = folder_dir
        config.MOD_DESCRIPTOR_DIR = f'{folder_dir}\\descriptor.mod'
        config.HISTORY_DIRECTORY = f'{folder_dir}\\history'
        config.COMMON_DIRECTORY = f'{folder_dir}\\common'

        with open(rf'{config.MOD_DESCRIPTOR_DIR}', 'r') as file:
            config.MOD_DESCRIPTOR = file.readlines()

        print(f"Selected file: {folder_dir}")

    selected_folder_label = parent_object.findChild(QLabel, "selected_folder_label")

    for i, v in enumerate(config.MOD_DESCRIPTOR):
        line = v.split("\"")
        if line[0] == 'supported_version=':
            config.MOD_VERSION = line[1]

    try:
        selected_folder_label.setText(f'{folder_dir}, Hoi4 version: {config.MOD_VERSION}')
    except AttributeError:
        selected_folder_label = QLabel(f'{folder_dir}, Hoi4 version: {config.MOD_VERSION}')
        selected_folder_label.setObjectName("selected_folder_label")
        layout.addWidget(selected_folder_label)
        return 0