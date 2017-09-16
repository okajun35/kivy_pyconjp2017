# -*- coding: utf-8 -*

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import StringProperty 
from os.path import splitext, basename


'''
コードは公式のサンプルをもとに改良しました
https://github.com/kivy/kivy/blob/master/examples/miscellaneous/multiple_dropfile.py
'''

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
            
            # 取得したファイルが画像ファイルかどうかを判定する
            if ext == b'.jpg' or ext == b'.JPG' or ext == b'.png' or ext == b'.PNG' or ext == b'.bmp' or ext == b'.BMP':
            #if ext == b'.jpg' or ext == b'.JPG':
             
                #self.file_name = filename.decode('utf-8')
                self.file_name = name
                self.image_name = filename.decode('utf-8')
            else:
                self.file_name = 'not image file'
                self.image_name = './image/no_image.jpg'


