from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import*
def check_win():
    label.setText("переможець")
    winner.setText(str(randint(1,100)))


app=QApplication([])
win=QWidget()

win.setWindowTitle("пітон")
win.resize(500,300)
label=QLabel("нажми шоб дізнатись переможця")
winner=QLabel("?")
btn=QPushButton("нажми")

styleSheet=("font-size:30px; color:#AC33FF")

label.setStyleSheet(styleSheet)
winner.setStyleSheet(styleSheet)

col=QVBoxLayout()

col.addWidget(label,alignment=Qt.AlignCenter)
col.addWidget(winner,alignment=Qt.AlignCenter)
col.addWidget(btn)

win.setLayout(col)

btn.clicked.connect(check_win)


win.show()
app.exec_()