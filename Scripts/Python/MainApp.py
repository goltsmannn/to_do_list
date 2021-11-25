from random import randint
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.properties import NumericProperty, ReferenceListProperty


Builder.load_file('../Kivy/markup.kv')


class Grid(FloatLayout):
    pass


class Block(FloatLayout):
    pass


class RootWidget(AnchorLayout):
    listHah = ObjectProperty()

    def change(self):
        self.listHah.add_widget(TextInput())


class myButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
