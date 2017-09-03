# -*- coding: utf-8 -*
from kivy.config import Config

Config.set('graphics', 'width', '1024')  # configは先頭で指定しないとうまく反映されない場合がある
Config.set('graphics', 'height', '705')  
#Config.set('graphics', 'height', '768')  

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import NumericProperty
from kivy.clock import Clock

from kivy.core.window import Keyboard, Window

from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from time import strftime
from datetime import date

#from kivy.garden.graph import Graph, MeshLinePlot
from graph import Graph, MeshLinePlot

import garden
from math import sin, cos , pi

from kivy.properties import StringProperty

from kivy.uix.label import Label
#from kivy.graphics import Fbo

from kivy.animation import Animation

from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line
import datetime

from kivy.properties import StringProperty 
from kivy.core.window import Window
from os.path import splitext, basename

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty



import numpy as np
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as pl


from kivy.garden.mapview import MapView, MapMarkerPopup

resource_add_path('image')
resource_add_path('fonts')
LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する
#LabelBase.register(DEFAULT_FONT, 'A-TTC-Ryumin-Regular.ttc') #有料フォントを指定する


class CalculatorRoot(BoxLayout):
        
    clear_bool = BooleanProperty(False)

    def __init__(self, **kwargs):
        super(CalculatorRoot, self).__init__(**kwargs)

    def print_number(self, number):
        '''入力された値が入る'''
        if self.clear_bool:
            self.clear_display()

        text = "{}{}".format(self.display.text, number) # 今までの入力された文字列と入力された値が表示される
        self.display.text = text

        print("数字「{0}」が押されました".format(number))

    def print_operator(self, operator):
        if self.clear_bool:
            self.clear_bool = False

        text = "{} {} ".format(self.display.text, operator)
        self.display.text = text

        print("演算子「{0}」が押されました".format(operator))

    def print_point(self, operator):
        # 「.」が押されれた場合の処理

        print("（未実装）演算子「{0}」が押されました".format(operator))

    def clear_display(self):
        self.display.text = ""
        self.clear_bool = False

        print("「c」が押されました")
    def del_char(self):
        ''' "<x"を押された場合の計算結果を表示  '''

        self.display.text = self.display.text[:-1]

        print("「<x」が押されました")

    def calculate(self):
        ''' "="を押された場合の計算結果を表示  '''
        try:
            self.display.text = str(eval(self.display.text)) # 単一の式を評価  例：eval("5 + 10")　は15になる
            self.clear_bool = True

            print('計算完了')
        except:
            # 数字を入力せずに　'=’を押した場合などのエラー対策
            print('error　入力ミス')


# --------------------------------------

class ImageWidget(Widget):
    file_name  = StringProperty('drag')    # プロパティの追加
    image_name = StringProperty('./image/no_image.jpg')    # プロパティの追加

    def __init__(self, **kwargs):
        super(ImageWidget, self).__init__(**kwargs)
 
         # get app instance to add function from widget
        app = App.get_running_app()

        # add function to the list
        app.drops.append(self.on_dropfile)

    def on_dropfile(self, widget, filename):
        # a function catching a dropped file
        # if it's dropped in the widget's area
        if self.collide_point(*Window.mouse_pos):
            # on_dropfile's filename is bytes (py3)
            
            path, ext = splitext(filename)
            name = basename(filename.decode('utf-8'))
            
            print(ext)
            if ext == b'.jpg' or ext == b'.JPG' or ext == b'.png' or ext == b'.PNG' or ext == b'.bmp' or ext == b'.BMP':
            #if ext == b'.jpg' or ext == b'.JPG':
             
                #self.file_name = filename.decode('utf-8')
                self.file_name = name
                self.image_name = filename.decode('utf-8')
            else:
                self.file_name = 'not image file'
                self.image_name = './image/no_image.jpg'





# ------------------
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



#--------------------------------------------

'''
class Graph2(Graph):
    def __init__(self, **kwargs):
        super(Graph2, self).__init__(**kwargs)
        print('call Graph2')
        #self._fbo = Fbo(size=self.size, with_stencilbuffer=False)
        self._fbo = Fbo(with_stencilbuffer=False)
        #self.add_widget(self.graph_plot_sample())
'''



class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)
        print('test')
        #self._fbo = Fbo(size=self.size, with_stencilbuffer=False)
        #self.add_widget(self.graph_plot_sample())

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

class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)
        


    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.2, 0.5, 0.2)
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30*time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30*time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")


class HorizonalBoxWidget1(Widget):
    pass

class HorizonalBoxWidget2(Widget):
    pass

class HorizonalBoxWidget3(Widget):
    pass

class HBoxWidget(Widget):
    pass


class ExampleBoxWidget(Widget):
    pass

class ExampleBoxWidget2(Widget):
    pass


class ExampleButton(Widget):
    labelText = StringProperty('未反応')

    def buttonClic(self):
       self.labelText = 'クリック'

    def buttonRelease(self):
       self.labelText = '離した'


class MainSlide(Widget):
    def __init__(self, **kwargs):
        super(MainSlide, self).__init__(**kwargs)
 #       self.add_widget(GraphWidget())


    def call_glph(self):
        print('call')
        self.add_line()
        print('add')

    def call_matplot(self):
        print('call')
        self.ids.graph_matplot.add_widget(self.graph_plot_sample())   # matplotlibのグラフを表示する(動作が劇的に重くなるので一旦コメントアウト)

    def del_matplot(self):
        print('delete')
        self.ids.graph_matplot.clear_widgets()   # matplotlibのグラフを表示する(動作が劇的に重くなるので一旦コメントアウト)
        print('delete_comp')


    def graph_plot_sample(self):
        self.fig, ax = pl.subplots()
        x = np.linspace(-np.pi, np.pi)
        y = np.sin(x)

        x2 = np.linspace(-np.pi, np.pi)
        y2 = np.cos(x)

        ax.set_xlabel("X label")
        ax.set_ylabel("Y label")
        ax.grid(True)
        ax.plot(x, y)
        ax.plot(x2, y2)
        return self.fig.canvas

    def add_line(self):
        self.graph = self.ids.graph_plot4.ids.graph_plot
        plot = []
        plot.append(MeshLinePlot(color=[1, 0, 0, 1])) #赤
        plot.append(MeshLinePlot(color=[0, 1, 0, 1])) #緑

        plot[0].points = [(x, sin(x / 10.)) for x in range(0, 101)] # Sin波
        plot[1].points = [(x, cos(x / 10.)) for x in range(0, 101)] # Cos波
        
        self.graph.add_plot(plot[0])
        self.graph.add_plot(plot[1])


class Pres(App):
    time = NumericProperty(0)

    stop_watch_start  = False   # ストップウォッチが作動しているかどうか
    stop_watch_second = 0       # ストップウォッチの秒
    
    def __init__(self, **kwargs):
        super(Pres, self).__init__(**kwargs)
        self.title = 'PyconJP2017'    # ウィンドウの名前を変更
        self.drops = []               # ドラッグアンドドロップに使用


    def build(self):
        Window.bind(on_key_down=self.handle_key)
        Clock.schedule_interval(self.update_time, 0)

        Window.bind(on_dropfile=self.handledrops)   # ドラッグアンドドロップに使用


        return super(Pres, self).build()

    def update_time(self, dt):
        self.time += dt
        
        self.root.ids.time.text = strftime('[b]%H:%M:%S[/b]')
        today        =    date.today()
        self.root.ids.today.text = str(today.year) + '/' + str(today.month) + '/' + str(today.day)

        if self.stop_watch_start:
            self.stop_watch_second += dt
        
        m, s = divmod(self.stop_watch_second, 60)  # 分、秒を取得する
        ms = s * 100 % 100 # ミリ秒を取得

        self.root.ids.stopwatch.text = '{0:2d}:{1:2d}.[size=40]{2:2d}[/size]'.format(int(m), int(s), int(ms))

    def start_stop(self):   # ストップウォッチ
        if self.stop_watch_start:
            self.stop_watch_start = False
            self.root.ids.start_stop.text = 'Start'
        else:
            self.stop_watch_start = True
            self.root.ids.start_stop.text = 'Stop'

            
    def reset(self): # リセットボタンをクリック
        #print('reset')
        
        if self.stop_watch_start:
            self.root.ids.start_stop.text = 'Start'
            self.stop_watch_start = False

        self.stop_watch_second = 0
        print('{}'.format(self.stop_watch_second))
        self.root.ids.lap.text = '00:00:00'

    def record_lap(self): #ラップを取得する
        self.root.ids.lap.text = self.root.ids.stopwatch.text

    def handledrops(self, *args):
        # this will execute each function from list with arguments from
        # Window.on_dropfile
        #
        # make sure `Window.on_dropfile` works on your system first,
        # otherwise the example won't work at all
        for func in self.drops:
            func(*args)


    def handle_key(self, window, code, code2, char, modifier):
        sm = self.root.ids.sm
        
        if code == Keyboard.keycodes['right']:
            sm.transition.direction = 'left'
            sm.current = sm.next()
        if code == Keyboard.keycodes['left']:
            sm.transition.direction = 'right'
            sm.current = sm.previous()
        

    def test(self):
        print('test')


if __name__ == '__main__':
    Pres().run()

