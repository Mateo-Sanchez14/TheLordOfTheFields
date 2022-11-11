from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class FirstWindow(Screen):
    pass
class SecondWindow(Screen):
    pass
class ScreenManager(ScreenManager):
    pass

kv = Builder.load_file('new_window.kv')

class TestApp(App):
    def build(self):
        return kv

if __name__ == 'main':
    TestApp().run()


