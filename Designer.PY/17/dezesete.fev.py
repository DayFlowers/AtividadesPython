from PySide6.QtGui import QPixmap
from UI_tela import UI_Form

class Mainwindown (QWidget):
    def _init_(self):
        super()._init_()
        self.ui = UI_Form ()
        self.ui.setupUI(self)
        self.ui.open_btn.cliked.connect(self.open_image)
    
    def open_image(self):
        file_dialog=QFileDialog()
        file_path,_ =file_dialog.getOpenFileName(self,"open Image","","Images (*.pneg *.xpm *.JPG. *Jpeg *bmp);; All Files(*)")

        if file_path:
            pimaxp = QPixmap(file_path)
            self.ui.image.setPimaxp(pimaxp)
            self.ui.image.setScvaledContents(True)
            
    if __name__=="_main_":
        app=QApplication(sys.argv)
        Window= Mainwindown()
        Window.show()
        sys.exist(app.exec())