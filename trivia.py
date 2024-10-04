from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
question_list.append(Question("What is the most downloaded demon level?", 'The Nightmare', 'Bloodlust', 'Osiris', 'Jumper X'))
question_list.append(Question("What's the second most-liked Extreme Demon?", 'Cataclysm', 'Falling Up', 'Dark Odyssey', 'Tartarus'))
question_list.append(Question('What is the new gamemode added in Update 2.0?', 'Robot', 'Swing', 'Wave', 'Spider'))
app = QApplication([])
btn_ok = QPushButton('Answer')
lb_Question = QLabel("What's the second most-liked Extreme Demon in Geometry Dash?")
RadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton('Falling Up')
rbtn_2 = QRadioButton('Cataclysm')
rbtn_3 = QRadioButton('Dark Odeyssey')
rbtn_4 = QRadioButton('Tartarus')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
