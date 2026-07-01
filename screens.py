# screens.py
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        start_btn = Button(text='Start Exam', size_hint=(1, 0.2))
        start_btn.bind(on_press=self.goto_exam)
        layout.add_widget(start_btn)
        self.add_widget(layout)

    def goto_exam(self, instance):
        self.manager.current = 'exam'

class ExamScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = []
        self.current_q = 0
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.question_label = Label(text='', size_hint=(1, 0.2))
        self.options_box = BoxLayout(orientation='vertical', size_hint=(1, 0.6))
        self.next_button = Button(text='Next', size_hint=(1, 0.2))
        self.next_button.bind(on_press=self.next_question)
        self.layout.add_widget(self.question_label)
        self.layout.add_widget(self.options_box)
        self.layout.add_widget(self.next_button)
        self.add_widget(self.layout)
        self.load_question()

    def load_question(self):
        from exam import get_questions
        self.questions = get_questions()
        self.show_question()

    def show_question(self):
        if self.current_q >= len(self.questions):
            self.show_result()
            return
        q = self.questions[self.current_q]
        self.question_label.text = q['question']
        self.options_box.clear_widgets()
        for option in q['options']:
            btn = Button(text=option)
            btn.bind(on_press=self.select_option)
            self.options_box.add_widget(btn)

    def select_option(self, instance):
        self.selected_answer = instance.text

    def next_question(self, instance):
        # Save answer and go to next
        self.current_q += 1
        self.show_question()

    def show_result(self):
        from exam import check_answer
        score = 0
        for i, q in enumerate(self.questions):
            if check_answer(i, getattr(self, 'selected_answer', '')):
                score += 1
        popup = Popup(title='Result', content=Label(text=f'Your score: {score}/{len(self.questions)}'), size_hint=(0.6, 0.4))
        popup.open()
