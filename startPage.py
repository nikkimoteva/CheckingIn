from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
import kivy.event
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from db import DataBase
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.utils import platform
import NotificationAnnoyer
import Asker
import Data



class AskerPage(Screen):
    option = ObjectProperty(None)

    def options(self):
        NotificationAnnoyer.adding_dict()
        sm.current = "adding_task"


class AddingTask(Screen):
    task_title = ObjectProperty(None)
    task_key = ObjectProperty(None)
    deadline = ObjectProperty(None)
    deadtime = ObjectProperty(None)

    def adding(self):
        NotificationAnnoyer.adding_task(self.task_title.text, "task" + self.task_key.text,
                                        self.deadline.text, self.deadtime.text)
        Data.dump(NotificationAnnoyer.tasks_dict)
        task_added()
        sm.current = "asker"

    def go_back(self):
        sm.current = "asker"



#class NAPage(Screen):
    #task = NotificationAnnoyer.


class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and \
                self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    current = ""

    def next(self):
        sm.current = "asker"

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = name


class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()

def task_added():
    pop = Popup(title='Task added',
                content=Label(text='The current task was added to the list.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

def wind():
    if platform not in ('android', 'ios'):
        Config.set('graphics', 'resizable', '0')
        Window.size = (320, 420)


kv = Builder.load_file("checkingin.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main"),
           AskerPage(name="asker"), AddingTask(name="adding_task")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "adding_task"


class CheckingIn(App):
    def build(self):
        return sm


if __name__ == "__main__":
    CheckingIn().run()