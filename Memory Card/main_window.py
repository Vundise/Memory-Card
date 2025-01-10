from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QRadioButton, QGroupBox, QButtonGroup


main_win = QWidget()
main_win.setWindowTitle("Memory card")

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
btn_ans = QPushButton("Відповісти")
rest = QSpinBox()
question = QLabel()
title = QLabel()

ans1 = QRadioButton("1")
ans2 = QRadioButton("2")
ans3 = QRadioButton("3")
ans4 = QRadioButton("4")

group = QGroupBox("Варіанти відповідей")
radio_group = QButtonGroup()
radio_group.addButton(ans1)
radio_group.addButton(ans2)
radio_group.addButton(ans3) 
radio_group.addButton(ans4)

question = QLabel("Запитання")
minutes = QLabel("Хвилини")
correct = QLabel("Результат")
lb_result = QLabel("")
lb_correct = QLabel("")

v_line2 = QVBoxLayout()
v_line1 = QVBoxLayout()
h_line = QHBoxLayout()

v_line1.addWidget(ans1)
v_line1.addWidget(ans2)
v_line2.addWidget(ans3)
v_line2.addWidget(ans4)

h_line.addLayout(v_line2)
h_line.addLayout(v_line1)

group.setLayout(h_line)

ans_group = QGroupBox()

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result)
layout_res.addWidget(lb_correct)

ans_group.setLayout(layout_res)
h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
v_main = QVBoxLayout()

h1_main.addWidget(btn_menu)
h1_main.addWidget(btn_rest, alignment=Qt.AlignRight)
h1_main.addWidget(rest, alignment=Qt.AlignRight)
h1_main.addWidget(minutes)
h1_main.addStretch(1)

h2_main.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h3_main.addWidget(ans_group)
h3_main.addWidget(group)

ans_group.hide()

h4_main.addStretch(1)
h4_main.addWidget(btn_ans, stretch=2)
h4_main.addStretch(1)

v_main.addLayout(h1_main, stretch=1)
v_main.addLayout(h2_main, stretch=2)
v_main.addLayout(h3_main, stretch=8)
v_main.addLayout(h4_main)

v_main.setSpacing(5)
main_win.setLayout(v_main)
main_win.resize(650, 450)






