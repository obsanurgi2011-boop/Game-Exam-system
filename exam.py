from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from reportlab.pdfgen import canvas
from screens import tr

class ExamsScreen(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        layout.add_widget(Label(text=tr('exam_list', self.manager.lang), font_size=24, size_hint_y=0.2))
        layout.add_widget(Button(text=tr('start_exam', self.manager.lang), on_press=lambda x: self.start_exam()))
        layout.add_widget(Button(text=tr('end_exam', self.manager.lang), on_press=lambda x: self.end_exam()))
        layout.add_widget(Button(text=tr('generate_certificate', self.manager.lang), on_press=lambda x: self.trigger_certificate()))
        layout.add_widget(Button(text=tr('cancel', self.manager.lang), on_press=lambda x: setattr(self.manager, 'current', 'dashboard')))
        
        self.add_widget(layout)

    def start_exam(self):
        print("Exam started...")

    def end_exam(self):
        print("Exam ended...")

    def trigger_certificate(self):
        user = self.manager.auth.current_user
        name = user['username'] if user else 'Student'
        generate_certificate(name, "General Aptitude Exam", "2026-07-01")

def generate_certificate(student_name, exam_name, date_str, filename='certificate.pdf'):
    c = canvas.Canvas(filename, pagesize=(600, 400))
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(300, 350, "Certificate of Achievement")
    c.setFont("Helvetica", 18)
    c.drawCentredString(300, 300, f"Presented to {student_name}")
    c.drawString(50, 250, f"Exam: {exam_name}")
    c.drawString(50, 220, f"Date: {date_str}")
    c.save()
    print(f"Certificate saved as {filename}")
    
