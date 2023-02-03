import serial.tools.list_ports
import connection_module
import random
from matplotlib import pyplot as plt
import numpy
import kivy as kv
# from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import (NumericProperty, StringProperty, ReferenceListProperty, ObjectProperty)
from kivy.config import Config
from kivy.core.window import Window
from kivy.clock import Clock

Window.clearcolor = (61 / 255, 43 / 255, 52 / 255, 1)
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Builder.load_file("visuals.kv")


class Title(Label):
    temp_value = StringProperty("No target temperature set")







class Temp_prompt(Label):

    current = ""

    def temp_callback(self):
        # print(Window.connection.readline().decode("utf-8"))
        Temp_prompt.text = str(connection_module.filter_temp(Window.connection.readline().decode("utf-8")))
        print("Temp_prompt")

class Input_target(TextInput):
    # input_target = ObjectProperty()
    multiline = False

    def on_text(self, instance, value):
        Confirm.holder = value
        print(Confirm.holder)


class Confirm(Button):
    holder = 0



class Window(Widget):
    connection = connection_module.start()
    Clock.schedule_interval(Temp_prompt.temp_callback,0.5)

    def press(self):
        self.ids.set_t.text = str(self.ids.butn.holder)
        self.connection.write(self.ids.butn.holder.encode())




class GUIapp(App):

    def build(self):
        return Window()


if __name__ == '__main__':
    GUIapp().run()
