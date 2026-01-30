#THIS CODE IS BORROWED FROM https://github.com/Thomas-Holtvedt/opengs-maptool/, ANOTHER GREAT TOOL FOR HOI4 MODDING

import sys
from PyQt6.QtWidgets import QApplication
from frontend.window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Window()
    main_window.show()
    sys.exit(app.exec())
