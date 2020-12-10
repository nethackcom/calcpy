from PyQt5 import QtWidgets
import CalcDesign
import keyboard


class CalcApp(QtWidgets.QMainWindow, CalcDesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Устанавливаем конвертированый дизайн приложения
        self.setupUi(self)

        self.pushButton_0.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_1.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_2.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_3.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_4.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_5.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_6.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_7.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_8.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_9.clicked.connect(self.buttonsSetTextLineEdit)

        self.pushButton_plus.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_minus.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_multiplication.clicked.connect(self.buttonsSetTextLineEdit)
        self.pushButton_division.clicked.connect(self.buttonsSetTextLineEdit)

        self.pushButton_result.clicked.connect(self.buttonResult)

        self.pushButton_C.clicked.connect(self.buttonClear)
        self.pushButton_CE.clicked.connect(self.buttonClearScreen)

    def buttonsSetTextLineEdit(self):
        # Определяем с помощью метода sender какая из кнопок была нажата
        # Берем значение кнопки из метода sender и вставляем в наш lineEdit
        sender = self.sender()
        return self.lineEdit.insert(sender.text())

    def buttonResult(self):
        try:
            return self.lineEdit.setText(str(eval(self.lineEdit.text())))
        except Exception:
            return self.lineEdit.setText('Ошибка операции...')

    def buttonClear(self):
        if len(self.lineEdit.text()) > 0:
            expression = list(self.lineEdit.text())
            del expression[-1]
            self.lineEdit.setText(''.join(expression))

    def buttonClearScreen(self):
        return self.lineEdit.clear()

    def checkKeyboardButtons(self):
        # Добавляем горячие клавиши
        # При нажатии на enter будет происходить вычисление
        keyboard.add_hotkey('enter', self.buttonResult)

    def blockKeyboardButtons(self):
        blockButtons = [chr(button) for button in range(65, 90)] + [chr(button) for button in range(97, 122)]
        [keyboard.block_key(i) for i in blockButtons]


def run():
    app = QtWidgets.QApplication([])
    app.setStyleSheet(open('style.qss').read())
    window = CalcApp()
    window.checkKeyboardButtons()
    window.blockKeyboardButtons()
    window.show()

    app.exec()


if __name__ == '__main__':
    run()
