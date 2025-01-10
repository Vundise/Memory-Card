from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QRadioButton, QGroupBox, QButtonGroup, QLineEdit

main_win2 = QWidget()

q_quest = QLabel("Введіть запитання:")
q_ans = QLabel("Введіть вірну відповідь:")
q_wrong1 = QLabel("Введіть першу хибну відповідь:")
q_wrong2 = QLabel("Введіть другу хибну відповідь:")
q_wrong3 = QLabel("Введіть третю хибну відповідь:")
q_stat_text = QLabel("Статистика")
q_stat = QLabel("")

q_stat_text.setStyleSheet("font-size: 19px; font-weight: bold;")

e_quest = QLineEdit()
e_ans = QLineEdit()
e_wrong1 = QLineEdit()
e_wrong2 = QLineEdit()
e_wrong3 = QLineEdit()

v_line_label = QVBoxLayout()
v_line_edit = QVBoxLayout()
h_line_el = QHBoxLayout()

v_line_label.addWidget(q_quest)
v_line_label.addWidget(q_ans)
v_line_label.addWidget(q_wrong1)
v_line_label.addWidget(q_wrong2)
v_line_label.addWidget(q_wrong3)

v_line_edit.addWidget(e_quest)
v_line_edit.addWidget(e_ans)
v_line_edit.addWidget(e_wrong1)
v_line_edit.addWidget(e_wrong2)
v_line_edit.addWidget(e_wrong3)

h_line_el.addLayout(v_line_label)
h_line_el.addLayout(v_line_edit)

btn_add_question = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")
btn_back = QPushButton("Назад")

h_line_btn = QHBoxLayout()

h_line_btn.addWidget(btn_add_question)
h_line_btn.addWidget(btn_clear)

v_line_up = QVBoxLayout()
v_line_up.addLayout(h_line_el)
v_line_up.addLayout(h_line_btn)
v_line_up.addWidget(q_stat_text)
v_line_up.addWidget(q_stat)
v_line_up.addWidget(btn_back)

main_win2.setLayout(v_line_up)

main_win2.resize(600, 500)

