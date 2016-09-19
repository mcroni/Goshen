from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from mat.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.factory import Factory


from mat.button import MDIconButton
from mat.label import MDLabel
from mat.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
from mat.navigationdrawer import NavigationDrawer
from mat.selectioncontrols import MDCheckbox
from mat.dialog import MDDialog
from theming import ThemeManager
from mat.dialog import MDDialog
from mat.textfields import SingleLineTextField
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from mat.button import MDRaisedButton
from mat.list import MDList
from mat.list import TwoLineListItem, OneLineListItem
import mat.snackbar as Snackbar
from mat.grid import SmartTile,SmartTileWithLabel

from mat.button import MDFloatingActionButton
from socket import socket
from OpenSSL import SSL


import threading

from pastors import *
from testimonies import *
from announcements import *
from request import *
from gallery import *
from sermons import *
from quotes import *

#from plyer import call
#from plyer.platforms.android.notification import AndroidNotification



#from models import *

from persons import *
from models_sql import *

session = Session()
person_session = Person_session()

sock = socket()



class Quotes(Screen):
    name_and_quo = {}
    def __init__(self, **kwargs):
        super(Quotes, self).__init__(**kwargs)
        self.load()

        #self.ids.search_input.bind(text=self.some_func)

    def load(self):
        """ im not sure i will be needing this function in final version"""
        for name,quotes in session.query(Quotations.name,Quotations.quotes):
            n_q = []
            n_q.append(("'{}'".format(name),quotes))
            print(n_q)
            # self.name_and_quo['{}'.format(name)]= name
            # self.name_and_quo['{}'.format(quotes)]=quotes
            #print(self.name_and_quo.values())
            #b = str(name)
            #bb = b[2:-3]
            #names.append(bb)

    def some_func(self, *args):
        returned_name = self.ids.search_input.text
        self.ids.ml.clear_widgets()
        query = session.query(Quotations.name).filter(Quotations.name.like('%{}%'.format(returned_name)))
        for record in query:
            self.ids.ml.add_widget(OneLineListItem(text=record.name))
        print(len(self.ids.ml.children))
        if len(self.ids.ml.children) == 0:
            self.show_example_snackbar('simple')

    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Person Not Found :-(", duration=1)


class Guide(Screen):
    pass

class DBScroll(Popup):
    pass

class Calender(Screen):
    pass
class Donations(Screen):
    pass




class MyTile(SmartTile):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('pressed popup',str(self.source))



class TitheButton(Button):
    def __init__(self,**kwargs):
        super(TitheButton,self).__init__(**kwargs)


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('touched',self.text)
            self.add_tithe()
        return super(TitheButton, self).on_touch_down(touch)

    def add_tithe(self):
        p = TithePopup()
        p.title= self.text
        p.open()



class GoshenTV(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    #list of previous screens

class Drawer(NavigationDrawer):
    def __init__(self,**kwargs):
        super(Drawer, self).__init__(**kwargs)







class TithePopup(Popup):
    def __init__(self,**kwargs):
        super(TithePopup,self).__init__(**kwargs)

    # def on_add(self,month,amount):
    #     print('called me',month, amount)
    #     tithe_to_pay = ((10 / 100) * int(self.ids.amount.text))
    #     print(tithe_to_pay)
    #     tithe = Tithes(month=self.title, amount=tithe_to_pay)
    #     session.add(tithe)
    #     session.commit()
    #     self.ids.amount.text=''
    #     self.ids.amount.hint_text = 'Tithe has Been Recorded'

        #print(self.text) #chale use this trick to add the figures to the db with neccessarily calling them with
        # message = OBjectProperty.blah blah su=hit

# class TitheViewer(Screen):
#     def __init__(self,**kwargs):
#         super(TitheViewer,self).__init__(**kwargs)
#         for month,amount in session.query(Tithes.month,Tithes.amount):
#             self.ml.add_widget(OneLineListItem(text=month +'\t\t\t\t\t\t\t\t\t\t\t\t\t\t '+ str(amount)))
#
# # amount




from kivy.utils import get_color_from_hex
import random




class Tithe(Screen):
    months = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Tithe,self).__init__(**kwargs)

        months_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

        colors = ['#f8bbd0','#90caf9','#2196f3','#1a237e','#90a4ae','#d7ccc8','#AA00FF','#f57f17','#4db6ac',
                 '#827717','#f0f4c3','#F5F5F5','#cccccc','#e6ee9c','#b39ddb','#ffca28']

        for month in months_list:
            self.ids.months.add_widget(TitheButton(text=month,
                                                   background_color=get_color_from_hex(random.choice(colors)),
                                                   on_pressed= lambda x: self.add_tithe()))





class CustomListItem(OneLineListItem):
    def __init__(self,**kwargs):
        super(CustomListItem,self).__init__(**kwargs)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('im touched',self.text)
        return super(CustomListItem,self).on_touch_down(touch)

class Search(Screen):
    def __init__(self,**kwargs):
        super(Search,self).__init__(**kwargs)
        #self.load()

        self.ids.search_input.bind(text=self.some_func)
    def load(self):
        """ im not sure i will be needing this function in final version"""
        for name in session.query(Person.name):
            b = str(name)
            bb = b[2:-3]
            names.append(bb)

    def some_func(self,*args):
        returned_name = self.ids.search_input.text
        self.ids.ml.clear_widgets()
        query = person_session.query(Person.name).filter(Person.name.like('%{}%'.format(returned_name)))
        for record in query:
            self.ids.ml.add_widget(CustomListItem(text=record.name))
        print(len(self.ids.ml.children))
        if len(self.ids.ml.children) == 0:
            self.show_example_snackbar('simple')


    def show_example_snackbar(self, snack_type):
        if snack_type == 'simple':
            Snackbar.make("Person Not Found :-(", duration=1)











class AvatarSampleWidget(ILeftBody, Image):
    pass
class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass
class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class SubButton(Popup):
    pass



class Jarvis(App):
    def __init__(self, **kwargs):
        super(Jarvis, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        if key == 27:
            if self.screen_list:
                self.my_screenmanager.current = self.screen_list.pop()
                return True

            

    theme_cls = ThemeManager()
    nav_drawer = ObjectProperty()

    def toast(self):
        Gallery.toast()

    def build(self):
        self.title= "GoshenApp"
        self.my_screenmanager = ScreenManager()

        main_screen = MainScreen(name='screen1')
        testimonies = Testimonies(name='testimonies')
        pastors = Pastors(name='pastors')
        requests = Requests(name='requests')
        sermons = Sermons(name='sermons')
        guide = Guide(name='guide')
        announcements = Announcements(name='announcements')
        donations = Donations(name='donations')
        quotes = Quotes(name='quotes')
        gallery = Gallery(name='gallery')
        tithe = Tithe(name='tithe')
        requests_reader = RequestsReader(name='requests_reader')
        #tithe_viewer = TitheViewer(name='tithe_viewer')
        search = Search(name= 'search')



        screen_lists = [main_screen, testimonies, pastors, requests, sermons, guide,
                         announcements,donations,gallery,tithe,requests_reader,
                         search,quotes]

        for screen in screen_lists:
            self.my_screenmanager.add_widget(screen)


        self.screen_list = []
        self.screen_list.append('screen1')
        self.theme_cls.theme_style = 'Dark'
        self.nav_drawer = Drawer()

        return self.my_screenmanager

    def theme_swap(self):
        if self.theme_cls.theme_style == 'Light':
            self.theme_cls.theme_style = 'Dark'
        else:
            self.theme_cls.theme_style = 'Light'

    def change_screen(self, next_screen):
        self.my_screenmanager.current = next_screen

        if self.my_screenmanager.current not in self.screen_list:
            self.screen_list.append(self.my_screenmanager.current)
        print(len(self.screen_list))

    def onBackButton(self):
        pass
        


    def on_pause(self):
        return True

    def on_resume(self):
        pass


    def popman(self):
        pop = DBScroll(auto_dismiss = False)
        pop.open()


if __name__=="__main__":
    from kivy.core.text import LabelBase
    LabelBase.register(name="Roboto",
                       fn_regular="Roboto-Regular.ttf",
                       fn_bold="Roboto-Thin.ttf")
    LabelBase.register(name='icons',
                       fn_regular='icons.ttf',)

    Jarvis().run()
