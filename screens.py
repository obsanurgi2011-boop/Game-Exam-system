from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from exam import ExamEngine

class LoginScreen(Screen):
    def login(self):
        u = self.ids.user.text
        p = self.ids.pwd.text

        if self.manager.auth.login(u, p):
            self.manager.current = "dashboard"
        else:
            Popup(title="Error",
                  content=Label(text="Invalid login"),
                  size_hint=(0.6,0.4)).open()


class DashboardScreen(Screen):
    def start_exam(self):
        self.manager.exam = ExamEngine()
        self.manager.current = "exam"


class ExamScreen(Screen):
    def on_pre_enter(self):
        self.load_q()

    def load_q(self):
        q = self.manager.exam.current()
        self.ids.question.text = q["q"]

        for i in range(4):
            self.ids[f"opt{i}"].text = q["a"][i]

    def select(self, i):
        if not self.manager.exam.answer(i):
            Popup(title="Result",
                  content=Label(text=f"Score: {self.manager.exam.score}"),
                  size_hint=(0.6,0.4)).open()
            self.manager.current = "dashboard"
        else:
            self.load_q()
