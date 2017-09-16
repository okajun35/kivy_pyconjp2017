# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.animation import Animation
from math import sin, cos , pi

class AnimeWidget(Widget):
    def __init__(self, **kwargs):
        super(AnimeWidget, self).__init__(**kwargs)
        print('anime test')
        
    def animate(self):
    
        #animation = Animation(pos=(100, 100), t='out_bounce')
        #animation += Animation(pos=(200, 100), t='out_bounce')
        #animation &= Animation(size=(500, 500))
        #animation += Animation(size=(100, 50))
        
        x = 0.0
        y = 0.0
        r = 50
        
        pos_x = 512
        pos_y = 350
        
        x =  pos_x
        y =  pos_y
        animation = Animation(pos=(x, y), t='out_bounce', duration = 0.05)

        for i in range(1,150):
            r = r + 2  # 螺旋
            
            x = r * cos(i/10) + pos_x
            y = r * sin(i/10) + pos_y

            animation += Animation(pos=(x, y), t='out_bounce', duration = 0.05 )

        #animation &= Animation(size=(30, 30))
        

        animation.repeat = True

        animation.start(self.info_button)
