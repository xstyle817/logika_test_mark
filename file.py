from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import*
def check_win():
    label.setText("переможець")
    winner.setText(str(randint(1,100)))

#створення додатку
app=QApplication([])
#створення вікна
win=QWidget()
#добавлення заголовку до вікна програми
win.setWindowTitle("пітон")
#задання розмірів вікна
win.resize(500,300)
#створення віджета підпис 
label=QLabel("нажми шоб дізнатись переможця")
winner=QLabel("?")
#створення віджета кнопка
btn=QPushButton("нажми")
#створення патерну для вигляду віджетів
styleSheet=("font-size:30px; color:#AC33FF")

label.setStyleSheet(styleSheet)
winner.setStyleSheet(styleSheet)
#створення вертикальної лінії
col=QVBoxLayout()
#добавлення елементів на вертикальну лінію
col.addWidget(label,alignment=Qt.AlignCenter)
col.addWidget(winner,alignment=Qt.AlignCenter)
col.addWidget(btn)
#добавлення лінії до вікна
win.setLayout(col)
#підключення функції до кнопки при натескані на неї
btn.clicked.connect(check_win)


win.show()
app.exec_()