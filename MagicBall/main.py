from manager import Manager
from kivymd.app import MDApp

class MagicBallApp(MDApp):
    def build(self):
        manager = Manager()
        return manager

MagicBallApp().run()