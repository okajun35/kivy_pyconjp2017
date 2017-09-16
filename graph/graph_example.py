# -*- coding: utf-8 -*


from kivy.app import App
from kivy.uix.widget import Widget


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

