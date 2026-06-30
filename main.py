from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from auth import UserAuth
from screens import LoginScreen, DashboardScreen, AdminScreen
from exam import ExamsScreen

class MyApp(App):
    def build(self):
        self.auth = UserAuth()
        
        sm = ScreenManager()
        sm.auth = self.auth
        sm.lang = 'en'  # Afaan jalqabaa (Default language)
        
        # Wiijitoota screens adda addaa galchuu
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(AdminScreen(name='admin'))
        sm.add_widget(ExamsScreen(name='exams'))
        
        return sm

if __name__ == '__main__':
    MyApp().run()
    
