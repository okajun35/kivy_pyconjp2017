from kivy.app import App
from kivy.uix.widget import Widget


# グラフ描画に関しては以下から取得
# https://github.com/kivy-garden/garden.graph
# 本体はGraphの「__init__.py」のみ
# 本来はgarden側から呼び出すのべきだが、
# ScrollView 、Carouselでは描画できない問題
# https://github.com/kivy-garden/garden.graph/issues/7
# があり、そのためにコードを持ってきて書きなおした


class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)
