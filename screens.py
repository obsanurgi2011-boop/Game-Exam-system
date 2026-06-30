from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

# --- Hiika Afaanotaa ---
translations = {
    'en': {
        'login': 'Login', 'logout': 'Logout', 'username': 'Username', 'password': 'Password',
        'admin_panel': 'Admin Panel', 'create_user': 'Create User', 'manage_exams': 'Manage Exams',
        'exam': 'Exam', 'student': 'Student', 'teacher': 'Teacher', 'result': 'Result',
        'save': 'Save', 'cancel': 'Cancel', 'start_exam': 'Start Exam', 'end_exam': 'End Exam',
        'error': 'Error', 'success': 'Success', 'language': 'Language', 'exam_list': 'Exam List'
    },
    'om': {
        'login': 'Seeni', 'logout': 'Bahi', 'username': 'Maqaa Fayyadamaa', 'password': 'Jecha Icchitii',
        'admin_panel': 'Xalaya Bulchiinsaa', 'create_user': 'Fayyadamaa Uumi', 'manage_exams': 'Qormaata Bulchi',
        'exam': 'Qormaata', 'student': 'Barataa', 'teacher': 'Barsiisaa', 'result': 'Bu\'aa',
        'save': 'Olkaayi', 'cancel': 'Dhiisi', 'start_exam': 'Qormaata Jalqabi', 'end_exam': 'Qormaata Xumuri',
        'error': 'Soba / Dogoggora', 'success': 'Milkaa\'ina', 'language': 'Afaan', 'exam_list': 'Tarree Qormaataa'
    },
    'am': {
        'login': 'ግባ', 'logout': 'ውጣ', 'username': 'የተጠቃሚ ስም', 'password': 'የይለፍ ቃል',
        'admin_panel': 'የአስተዳዳሪ ፓነል', 'create_user': 'ተጠቃሚ ፍጠር', 'manage_exams': 'ፈተናዎችን አደራጅ',
        'exam': 'ፈተና', 'student': 'ተማሪ', 'teacher': 'አስተማሪ', 'result': 'ውጤት',
        'save': 'አስቀምጥ', 'cancel': 'ሰርዝ', 'start_exam': 'ፈተና ጀምር', 'end_exam': 'ፈተና ጨርስ',
        'error': 'ስህተት', 'success': 'ተሳክቷል', 'language': 'ቋንቋ', 'exam_list': 'የፈተናዎች ዝርዝር'
    }
}

def tr(key, lang='en'):
    return translations.get(lang, translations['en']).get(key, key)


class LoginScreen(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=40, spacing=15)
        
        layout.add_widget(Label(text=tr('login', self.manager.lang).upper(), font_size=28, size_hint_y=0.2))
        
        self.username_input = TextInput(hint_text=tr('username', self.manager.lang), multiline=False, size_hint_y=0.12)
        self.password_input = TextInput(hint_text=tr('password', self.manager.lang), password=True, multiline=False, size_hint_y=0.12)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        
        lang_box = BoxLayout(orientation='horizontal', size_hint_y=0.12, spacing=10)
        lang_box.add_widget(Label(text=tr('language', self.manager.lang), font_size=16))
        self.lang_spinner = Spinner(text=self.manager.lang, values=['en', 'om', 'am'])
        self.lang_spinner.bind(text=self.change_lang)
        lang_box.add_widget(self.lang_spinner)
        layout.add_widget(lang_box)
        
        layout.add_widget(Button(text=tr('login', self.manager.lang), size_hint_y=0.15, on_press=lambda x: self.do_login()))
        self.add_widget(layout)

    def change_lang(self, spinner, text):
        self.manager.lang = text
        self.on_enter()

    def do_login(self):
        username = self.username_input.text
        password = self.password_input.text
        if self.manager.auth.authenticate(username, password):
            self.manager.current = 'dashboard'
        else:
            Popup(title=tr('error', self.manager.lang), content=Label(text='Invalid credentials'), size_hint=(0.6, 0.4)).open()


class DashboardScreen(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        user = self.manager.auth.current_user
        role = user.get('role', 'student') if user else 'student'
        name = user['username'] if user else ''
        
        layout.add_widget(Label(text=f"Welcome {name} ({role.upper()})", font_size=22, size_hint_y=0.2))
        
        if role == 'admin':
            layout.add_widget(Button(text=tr('admin_panel', self.manager.lang), on_press=lambda x: setattr(self.manager, 'current', 'admin')))
        
        layout.add_widget(Button(text=tr('manage_exams', self.manager.lang), on_press=lambda x: setattr(self.manager, 'current', 'exams')))
        layout.add_widget(Button(text=tr('logout', self.manager.lang), on_press=lambda x: self.logout()))
        self.add_widget(layout)

    def logout(self):
        self.manager.auth.current_user = None
        self.manager.current = 'login'


class AdminScreen(Screen):
    def on_enter(self, *args):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        layout.add_widget(Label(text=tr('admin_panel', self.manager.lang), font_size=24, size_hint_y=0.2))
        layout.add_widget(Button(text=tr('create_user', self.manager.lang), on_press=lambda x: self.add_user_popup()))
        layout.add_widget(Button(text=tr('cancel', self.manager.lang), on_press=lambda x: setattr(self.manager, 'current', 'dashboard')))
        
        self.add_widget(layout)

    def add_user_popup(self):
        self.popup = Popup(title=tr('create_user', self.manager.lang), content=CreateUserBox(self), size_hint=(0.8, 0.6))
        self.popup.open()


class CreateUserBox(BoxLayout):
    def __init__(self, parent_screen, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.parent_screen = parent_screen
        self.username_input = TextInput(hint_text=tr('username', parent_screen.manager.lang), multiline=False)
        self.password_input = TextInput(hint_text=tr('password', parent_screen.manager.lang), password=True, multiline=False)
        self.role_spinner = Spinner(text='student', values=['student', 'teacher', 'admin'])
        
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.role_spinner)
        
        btn_box = BoxLayout(size_hint_y=0.3, spacing=10)
        btn_box.add_widget(Button(text=tr('save', self.parent_screen.manager.lang), on_press=self.save_user))
        btn_box.add_widget(Button(text=tr('cancel', self.parent_screen.manager.lang), on_press=lambda x: self.parent_screen.popup.dismiss()))
        self.add_widget(btn_box)

    def save_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text
        role = self.role_spinner.text
        if username and password:
            if self.parent_screen.manager.auth.add_user(username, password, role):
                Popup(title=tr('success', self.parent_screen.manager.lang), content=Label(text='User added successfully.'), size_hint=(0.6, 0.4)).open()
                self.parent_screen.popup.dismiss()
            else:
                Popup(title=tr('error', self.parent_screen.manager.lang), content=Label(text='User already exists.'), size_hint=(0.6, 0.4)).open()
        
