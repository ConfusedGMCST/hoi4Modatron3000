#for import mod button
import config
from PyQt6.QtWidgets import QFileDialog, QLabel, QWidget, QVBoxLayout

def open_file_dialog(self, parent_object, layout):
    file_dir, _ = QFileDialog.getOpenFileName(
        self,
        "Select a File",
        "",  # Starting directory (empty = home)
        "All Files (*);;Python Files (*.py);;Text Files (*.txt)"
    )
    if file_dir:
        config.MOD_DIRECTORY = file_dir
        print(f"Selected file: {file_dir}")

    selected_file_label = parent_object.findChild(QLabel, "selected_file_label")

    try:
        selected_file_label.setText(file_dir)
    except AttributeError:
        selected_file_label = QLabel(file_dir)
        selected_file_label.setObjectName("selected_file_label")
        layout.addWidget(selected_file_label)
        return 0