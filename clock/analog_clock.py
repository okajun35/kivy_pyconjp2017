# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
from kivy.clock import Clock
from math import sin, cos , pi

import datetime




# code from -making a clock in kivy(https://stackoverflow.com/questions/18923321/making-a-clock-in-kivy)


class MyClockWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(MyClockWidget, self).__init__(**kwargs)



class Ticks(Widget):
    def __init__(self, **kwargs):
        #super(Ticks, self).__init__(**kwargs)
        super().__init__(**kwargs)


        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)
        
        Clock.schedule_interval(self.update_clock, 1)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            #Color(0.2, 0.5, 0.2)
            Color(1, 0, 0)

            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            #Color(0.3, 0.6, 0.3)
            Color(0, 0, 0)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            #Color(0.4, 0.7, 0.4)
            Color(0, 0, 0)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")

class MyClockApp(App):
    pass
    #def build(self):
    #    clock = MyClockWidget()
        
    #    Clock.schedule_interval(clock.ticks.update_clock, 1)
    #    return clock