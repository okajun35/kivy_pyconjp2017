from kivy.app import App
from kivy.uix.widget import Widget


# �O���t�`��Ɋւ��Ă͈ȉ�����擾
# https://github.com/kivy-garden/garden.graph
# �{�̂�Graph�́u__init__.py�v�̂�
# �{����garden������Ăяo���ׂ̂������A
# ScrollView �ACarousel�ł͕`��ł��Ȃ����
# https://github.com/kivy-garden/garden.graph/issues/7
# ������A���̂��߂ɃR�[�h�������Ă��ď����Ȃ�����


class GraphWidget(Widget):
    def __init__(self, **kwargs):
        super(GraphWidget, self).__init__(**kwargs)
