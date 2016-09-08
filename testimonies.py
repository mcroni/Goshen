from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from mat.list import MDList
from kivy.properties import ObjectProperty
from mat.list import TwoLineListItem, OneLineListItem
from main import DBScroll



from models_sql import *

session = Session()


import time
import threading

class F(Popup):
    def __init__(self, **kwargs):
        super(F, self).__init__(**kwargs)

    def shiemor(self):
        popt = PopThread()
        popt.start()
        dbt = DBThread()
        dbt.start()

        self.name = self.ids.name.text


    def popman(self):
        pop = DBScroll(auto_dismiss=True)
        pop.open()



class Testimonies(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(Testimonies, self).__init__(**kwargs)

    def read(self):
        content = ScrollView()
        mdlist = MDList()
        content.add_widget(mdlist)
        title = "Testimonies"
        pop = Popup(title= title,content= content,background= 'white.png')
        pop.open()
        for name,message in session.query(Testify.name,Testify.message):
            mdlist.add_widget(TwoLineListItem(text=str(name),secondary_text=str(message)))
        print('reading testimonies')


    def share(self):
        pop = F()
        pop.open()


class DBThread(threading.Thread):
    def __init__(self,**kwargs):
        super(DBThread,self).__init__(**kwargs)

    def run(self):
        add_testimony = Testify(name= '', message='')
        session.add(add_testimony)


class PopThread(threading.Thread):
    def __init__(self, **kwargs):
        super(PopThread, self).__init__(**kwargs)

    def run(self):
        pop = DBScroll(auto_dismiss=True)
        pop.open()

