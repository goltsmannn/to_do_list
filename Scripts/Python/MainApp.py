from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
Builder.load_file('../Kivy/markup.kv')


class MainPage(Screen):
    list_of_things = ObjectProperty()
    def change(self):
        self.list_of_things.add_widget(Button())

class TestApp(MDApp):
    sm = ScreenManager()

    def build(self):
        return MainPage()

if __name__ == '__main__':
    TestApp().run()
