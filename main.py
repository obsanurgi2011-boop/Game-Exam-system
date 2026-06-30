from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from auth import UserAuth
from screens import LoginScreen, DashboardScreen, ExamScreen

class SM(ScreenManager):
    pass

class GoExam(App):
    def build(self):
        sm = SM()

        sm.auth = UserAuth()

        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ExamScreen(name="exam"))

        return sm

GoExam().run()
