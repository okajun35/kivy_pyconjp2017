# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


'''
レイアウトの例、Kv側でDynamic Classesで宣言(@widgetをつける)することで
Python側で定義する必要がなくなりますなくなります。

'''
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
    '''
    ボタンを押した場合の挙動の確認
    '''
    labelText = StringProperty('未反応')

    def buttonClic(self):
       self.labelText = 'クリック'

    def buttonRelease(self):
       self.labelText = '離した'