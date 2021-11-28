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

Builder.load_string('''

<Button>:
    size_hint_y: None
    height: 40


<one_task>:
    BoxLayout:
        CheckBox:
            id: checkbox
            pos_hint: {"x":0.6, "y":0.4}
            size_hint: 0.05,0.05

<MainPage>:
    list_of_things: list_of_things
    BoxLayout:
        orientation: 'horizontal'
        BoxLayout:
            padding:[5, 18, 5, 15]
            canvas:
                Color:
                    rgba: .1, .1, .1, .6
                Rectangle:
                    pos: self.pos
                    size: self.size
            orientation: 'vertical'
            size_hint: 0.33, 1

            Label:
                text: "To-do list"
                text_size: self.width-20, self.height-20

            Label:
                text: "Пользователя"
                text_size: self.width-20, self.height-20
                
            TextInput:   
                size_hint: (.8, None)
                height: 30
                multiline: False
                
            Label:

                text: "Холст/записки"
                text_size: self.width-20, self.height-20
            TextInput:   
                size_hint: (.2, None)
                height: 350
                multiline: False    
            Button:
            Button:
        BoxLayout:
            orientation: 'vertical'
            padding:[15,20,15,20]
            ScrollView:
                GridLayout:
                    id: list_of_things
                    canvas:
                        Color:
                            rgba: .1, .1, 1, .3
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    height: self.minimum_height
                    size_hint_y: None
                    cols: 1
                    spacing: 25
                    padding: 25
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40


            
            ScrollView:
                GridLayout:
                    canvas:
                        Color:
                            rgba: 1, 1, .1, .3
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    height: self.minimum_height
                    size_hint_y: None
                    cols: 1
                    spacing: 25
                    padding: 25
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40


            ScrollView:
                GridLayout:
                    canvas:
                        Color:
                            rgba: .1, 1, .1, .3
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    height: self.minimum_height
                    size_hint_y: None
                    cols: 1
                    spacing: 25
                    padding: 25
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40


            ScrollView:
                GridLayout:
                    canvas:
                        Color:
                            rgba: 1, .1, .1, .3
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    height: self.minimum_height
                    size_hint_y: None
                    cols: 1
                    spacing: 25
                    padding: 25
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40
                    Button:
                        size_hint_y: None
                        height: 40
    AnchorLayout:
        anchor_x: 'right'
        anchor_y: 'bottom'          
        Button:
            text: "add"
            font_size: "10sp"
            size: 90, 50
            size_hint: None, None
            on_press: root.change()
                


                


''')



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