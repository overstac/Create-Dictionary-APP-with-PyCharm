from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
import json

def search():
    word_in= word.text()
    word_in=word_in.lower()
    f= open("data.json")
    data= json.load(f)
    if word_in in data:
        element=data[word_in]
        st= "\n".join(element)
        output_label.setText(st)
    else:
        output_label.setText("What kind of word is that one ???\nTry another one !")

app= QApplication([])
window= QWidget()
window.setWindowTitle("Word Definitaion")
layout= QVBoxLayout()
layout1= QHBoxLayout()
layout.addLayout(layout1)

word= QLineEdit()
layout1.addWidget(word)

convert_btn= QPushButton("Covert!")
layout1.addWidget(convert_btn)
convert_btn.clicked.connect(search)

output_label= QLabel("")
layout.addWidget(output_label, alignment=Qt.AlignmentFlag.AlignLeft)

window.setLayout(layout)
window.show()
app.exec()