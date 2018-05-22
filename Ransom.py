from main_window import *

encrypt(os.path.dirname(os.path.realpath(__file__)))
app = QApplication(sys.argv)
myWindow = MyWindow()
myWindow.show()
app.exec_()