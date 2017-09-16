# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


#class HorizonalBoxWidget1(Widget):
#    pass

#class HorizonalBoxWidget2(Widget):
#    pass

#class HorizonalBoxWidget3(Widget):
#    pass

#class HBoxWidget(Widget):
#    pass


#class ExampleBoxWidget(Widget):
#    pass

#class ExampleBoxWidget2(Widget):
#    pass


class ExampleButton(Widget):
    labelText = StringProperty('未反応')

    def buttonClic(self):
       self.labelText = 'クリック'

    def buttonRelease(self):
       self.labelText = '離した'