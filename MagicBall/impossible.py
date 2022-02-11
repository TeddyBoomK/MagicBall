from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton


class Impossible(Screen):
    def __init__(self, manager, **kw):
        super().__init__(**kw)
        img = MDIconButton(
            icon="Шар-09.png",
            user_font_size="550sp",
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            on_press=manager.switch_to_ask_question
        )

        self.add_widget(img)