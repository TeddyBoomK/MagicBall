from absolutely import Absolutely
from ask_question import AskQuestion
from dont_know import DontKnow
from doubts import Doubts
from good_chance import GoodChance
from hard_question import HardQuestion
from impossible import Impossible
from unlikely import Unlikely
from again_later import AgainLater

from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ask_question = AskQuestion(self, name="задай вопрос")
        self.again_later = AgainLater(self, name="задай этот вопрос позже")
        self.absolutely = Absolutely(self, name='безусловно')
        self.good_chance = GoodChance(self, name="шансы хорошие")
        self.doubts = Doubts(self, name="есть сомнения")
        self.hard_question = HardQuestion(self, name="сложный вопрос")
        self.impossible = Impossible(self, name="я не могу на это ответить")
        self.unlikely = Unlikely(self, name="маловероятно")
        self.dont_know = DontKnow(self, name="не выйдет")

        self.add_widget(self.ask_question)
        self.add_widget(self.absolutely)
        self.add_widget(self.again_later)
        self.add_widget(self.good_chance)
        self.add_widget(self.doubts)
        self.add_widget(self.hard_question)
        self.add_widget(self.impossible)
        self.add_widget(self.unlikely)
        self.add_widget(self.dont_know)

    def switch_to_ask_question(self, button=None):
        self.ask_question.question.text = ""
        self.switch_to(self.ask_question, direction='left')

    def switch_to_again_later(self, button=None):
        self.switch_to(self.again_later, direction='right')

    def switch_to_absolutely(self, button=None):
        self.switch_to(self.absolutely, direction='right')

    def switch_to_good_chance(self, button=None):
        self.switch_to(self.good_chance, direction='right')

    def switch_to_doubts(self, button=None):
        self.switch_to(self.doubts, direction='right')

    def switch_to_hard_question(self, button=None):
        self.switch_to(self.hard_question, direction='right')

    def switch_to_impossible(self, button=None):
        self.switch_to(self.impossible, direction='right')

    def switch_to_unlikely(self, button=None):
        self.switch_to(self.unlikely, direction='right')

    def switch_to_dont_know(self, button=None):
        self.switch_to(self.dont_know, direction='right')
