from kivy.app import App
from kivy.uix.label import Label

class ExamApp(App):
    def build(self):
        return Label(text="Exam System Working ✔ APK Success")

ExamApp().run()