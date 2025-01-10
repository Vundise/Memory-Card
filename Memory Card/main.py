from PyQt5.QtWidgets import QApplication
app = QApplication([])
from random import choice, shuffle
from main_window import *
from menu_window import *

class Question():
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.correct = 0
        self.attemps = 0
        self.isAsking = True

    def got_right(self):
        self.correct += 1
        self.attemps += 1

    def got_wrong(self):
        self.attemps += 1
    
Q1 = Question("Яблуко", "Apple", "Aple", "Pineapple", "Pinaple")
Q2 = Question("Груша", "Pineapple", "Painapple", "Apple", "Watermelon")
Q3 = Question("Арбуз", "Watermelon", "Apple", "Pineapple", "Aple")
Q4 = Question("Банан", "Banan", "Bannan", "Watermelom", "Apple")

radio_list = [ans1, ans2, ans3, ans4]
question_list = [Q1, Q2, Q3, Q4]

def new_question():
    global cur_Q 
    cur_Q = choice(question_list)
    question.setText(cur_Q.question)
    lb_correct.setText(cur_Q.answer)
    shuffle(radio_list)
    radio_list[0].setText(cur_Q.wrong_answer1)
    radio_list[1].setText(cur_Q.wrong_answer2)
    radio_list[2].setText(cur_Q.wrong_answer3)
    radio_list[3].setText(cur_Q.answer)

new_question()

def check_result():
    radio_group.setExclusive(False)

    for ans in radio_list:      
        if ans.isChecked():
            if ans.text() == lb_correct.text():
                lb_result.setText("Правильно")
                cur_Q.got_right()
                ans.setChecked(False)
                break
    else:
        lb_result.setText("Неправильно")
        cur_Q.got_wrong()
    radio_group.setExclusive(True)
        
#def new_question():

def switch_screen():
    if btn_ans.text() == "Відповісти":
        check_result()
        group.hide()
        ans_group.show()

        btn_ans.setText("Наступне питання")
    else:
        new_question()
        ans_group.hide()
        group.show()

        btn_ans.setText("Відповісти")

def menu_generation():
    if cur_Q.attemps == 0:
        correct_procent = 0
    else:
        correct_procent = (cur_Q.correct / cur_Q.attemps) * 100
    
    text = f"Разів відповіли: {cur_Q.attemps}\n" f"Відповідей: {cur_Q.correct}\n" f"Успішніть: {correct_procent}"

    main_win.hide()
    main_win2.show()

    q_stat.setText(text)

def back_menu():
    main_win2.hide()
    main_win.show()

def menu_stat():
    e_quest.clear()
    e_ans.clear()
    e_wrong1.clear()
    e_wrong2.clear()
    e_wrong3.clear()

def add_question():
    questi = Question(e_quest.text(), e_ans.text(), e_wrong1.text(), e_wrong2.text(), e_wrong3.text())
    question_list.append(questi)
    menu_stat()



btn_menu.clicked.connect(menu_generation)
btn_back.clicked.connect(back_menu)
btn_clear.clicked.connect(menu_stat)
btn_add_question.clicked.connect(add_question)
btn_ans.clicked.connect(switch_screen)





main_win.show()
app.exec_()