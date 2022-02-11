
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextFieldRound
from random import randint


class AskQuestion(Screen):
    def __init__(self, manager, **kw):
        super().__init__(**kw)

        self.man = manager

        img = MDIconButton(
            icon = "Шар-01.png",
            user_font_size = "550sp",
            pos_hint={'center_x': 0.5, 'center_y':0.5},
            on_press = self.action
        )

        self.question = MDTextFieldRound(
            hint_text = "Введите вопрос",
            icon_left = "help",
            pos_hint = {'center_x':0.5, 'center_y':0.45},
            size_hint = (0.25, 0.05),
            normal_color = (1,156/255,0,1),
            color_active = (1,156/255,0,1)
        )

        self.add_widget(img)
        self.add_widget(self.question)

    def action(self,button):
        res = randint(1,5)
        if self.question.text != "":
            if res == 1:
                self.man.switch_to_absolutely()
            elif res == 2:
                self.man.switch_to_good_chance()
            elif res == 3:
                self.man.switch_to_doubts()
            elif res == 4:
                self.man.switch_to_unlikely()
            elif res == 5:
                self.man.switch_to_dont_know()
