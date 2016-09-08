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

sock = socket()





import threading

from directory import *
from pastors import *
from testimonies import *
from announcements import *
from request import *

#from plyer import call
#from plyer.platforms.android.notification import AndroidNotification



#from models import *
from models_sql import *
session = Session()



class Sermons(Screen):
    pass

class Guide(Screen):
    pass

class DBScroll(Popup):
    pass

class Calender(Screen):
    pass
class Donations(Screen):
    pass


#use random to implement different themes

class GalleryAlbums(SmartTileWithLabel):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('pressed '+ str(self.text))

class Gallery(Screen,GridLayout):
    scroller = ObjectProperty(None)
    grid = ObjectProperty(None)
    def __init__ (self,**kwargs):
        super(Gallery, self).__init__(**kwargs)
        #albums = [album for album in session.query(Albums.name)] #i need to fix this bug, it prints the names with trailing ''
        if len(self.ids.grid.children) == 0:
            for album in session.query(Albums.name):
                str_album = str(album).strip()
                tt_album = str_album[2:-3]
                print(tt_album)
                album = GalleryAlbums(text=tt_album,source='mac.png',)
                self.ids.grid.add_widget(album)



        # if len(self.ids.grid.children) == 0:
        #     for i in range(10):
        #         src = ("http://placehold.it/480x270.png&text=slide-%d&.png" % i)
        #         image = MyTile(source=src, allow_stretch=True)
        #         self.ids.grid.add_widget(image)


            # will get back to you




class GalleryPopup(Popup):
    def __init__(self, **kwargs):
        super(GalleryPopup, self).__init__(**kwargs)


class MyTile(SmartTile):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('pressed popup',str(self.source))
            f = GalleryPopup()
            f.title =self.source
            f.ids.image.source = str(f.title) #this is crude but it works for me
            f.open()



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

    def on_add(self,month,amount):
        print('called me',month, amount)
        tithe_to_pay = ((10 / 100) * int(self.ids.amount.text))
        print(tithe_to_pay)
        tithe = Tithes(month=self.title, amount=tithe_to_pay)
        session.add(tithe)
        session.commit()
        self.ids.amount.text=''
        self.ids.amount.hint_text = 'Tithe has Been Recorded'

        #print(self.text) #chale use this trick to add the figures to the db with neccessarily calling them with
        # message = OBjectProperty.blah blah su=hit

class TitheViewer(Screen):
    def __init__(self,**kwargs):
        super(TitheViewer,self).__init__(**kwargs)
        for month,amount in session.query(Tithes.month,Tithes.amount):
            self.ml.add_widget(OneLineListItem(text=month +'\t\t\t\t\t\t\t\t\t\t\t\t\t\t '+ str(amount)))






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



















class AvatarSampleWidget(ILeftBody, Image):
    pass
class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass
class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class SubButton(Popup):
    pass


class Login(Screen):
    def __init__(self,**kwargs):
        super(Login,self).__init__(**kwargs)


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
        directory = Directory(name='directory')
        goshen_tv = GoshenTV(name='goshen_tv')
        gallery = Gallery(name='gallery')
        tithe = Tithe(name='tithe')
        requests_reader = RequestsReader(name='requests_reader')
        tithe_viewer = TitheViewer(name='tithe_viewer')
        login = Login(name='login')

        screenn_lists = [main_screen, testimonies, pastors, requests, sermons, guide,
                         announcements,donations,
                         directory,goshen_tv,gallery,tithe,requests_reader,tithe_viewer,login]

        for screen in screenn_lists:
            self.my_screenmanager.add_widget(screen)




        self.screen_list = []
        self.screen_list.append('screen1')
        self.theme_cls.theme_style = 'Light'
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
    LabelBase.register(name="Icons",
                       fn_regular="icons.ttf",
                       fn_bold="icons.ttf")
    Jarvis().run()
