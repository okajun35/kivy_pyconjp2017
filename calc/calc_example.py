# -*- coding: utf-8 -*

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty



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

