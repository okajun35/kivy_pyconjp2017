# -*- coding: utf-8 -*
from kivy.config import Config
from kivy.app import App

Config.set('graphics', 'width', '1024')  # 画面サイズはkivy.core.windowよりセットしないと変更しない
Config.set('graphics', 'height', '705')  


from kivy.core.window import Keyboard, Window

from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path

from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.graphics import Color, Line
#from kivy.garden.graph import Graph, MeshLinePlot
from graph import Graph, MeshLinePlot
from kivy.garden.mapview import MapView, MapMarkerPopup
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty

from time import strftime
from datetime import date
from math import sin, cos , pi
import datetime
import numpy as np
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
import matplotlib.pyplot as pl

from calc import calc_example
from drag_drop import  drag_drop
from clock import  analog_clock
from anime import  anime_example
from layout import layout_example
from graph_example import graph_example

#Config.set('graphics', 'height', '768')  
resource_add_path('image')
resource_add_path('fonts')
#LabelBase.register(DEFAULT_FONT, 'mplus-2c-regular.ttf') #日本語が使用できるように日本語フォントを指定する
LabelBase.register(DEFAULT_FONT, 'A-TTC-Ryumin-Regular.ttc') #有料フォントを指定する


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
        self.ids.graph_matplot.clear_widgets()   # matplotlibのグラフを削除する
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
        
    def on_start(self):
        ''' 起動時に呼ばれる '''
        print('DEMO start')

    def on_stop(self):
        ''' 終了時に呼ばれる '''

        print('DEMO end')

    def build(self):
        Window.bind(on_key_down=self.handle_key)   # スライドをキー操作でずらすのに使用
        Clock.schedule_interval(self.update_time, 0) # 時計の表示に使用

        Window.bind(on_dropfile=self.handledrops)   # ドラッグアンドドロップに使用


        return super(Pres, self).build()

    def update_time(self, dt):
        '''
        デジタル時計の表示とストップウォッチの表示
        
        '''
        self.time += dt
        
        # デジタル時計の年月日の表示
        self.root.ids.time.text = strftime('[b]%H:%M:%S[/b]')
        today        =    date.today()
        # デジタル時計の時刻の表示
        self.root.ids.today.text = str(today.year) + '/' + str(today.month) + '/' + str(today.day)

        # ストップウォッチのタイマーを表示
        if self.stop_watch_start:
            self.stop_watch_second += dt
        
        m, s = divmod(self.stop_watch_second, 60)  # 分、秒を取得する
        ms = s * 100 % 100 # ミリ秒を取得

        self.root.ids.stopwatch.text = '{0:2d}:{1:2d}.[size=40]{2:2d}[/size]'.format(int(m), int(s), int(ms))

    def start_stop(self):   
        '''ストップウォッチのスタートボタンの操作'''

        if self.stop_watch_start:
            self.stop_watch_start = False
            self.root.ids.start_stop.text = 'Start'
        else:
            self.stop_watch_start = True
            self.root.ids.start_stop.text = 'Stop'

            
    def reset(self):
        '''ストップウォッチのリセットボタンの操作'''

        #print('reset')
        
        if self.stop_watch_start:
            self.root.ids.start_stop.text = 'Start'
            self.stop_watch_start = False

        self.stop_watch_second = 0
        print('{}'.format(self.stop_watch_second))
        self.root.ids.lap.text = '00:00:00'

    def record_lap(self):
        '''ストップウォッチのリセットボタンの操作'''

        self.root.ids.lap.text = self.root.ids.stopwatch.text

    def handledrops(self, *args):
        '''ドラッグされたファイルパスを取得する  '''
        for func in self.drops:
            func(*args)


    def handle_key(self, window, code, code2, char, modifier):
        '''スライドをキーボードの左右ボタンで動かす'''

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

