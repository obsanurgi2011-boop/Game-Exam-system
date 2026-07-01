from kivy.app import App
from kivy.uix.label import Label

class ExamApp(App):
    def build(self):
        return Label(text="Exam System APK Working ✔")

if __name__ == "__main__":
    ExamApp().run()