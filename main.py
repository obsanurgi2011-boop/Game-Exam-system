# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import MainScreen, ExamScreen
from kivy.lang import Builder

Builder.load_file('ui.kv')

class MyScreenManager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(ExamScreen(name='exam'))
        return sm

if __name__ == '__main__':
    MainApp().run()
