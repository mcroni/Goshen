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




from plyer.platforms.android.notification import AndroidNotification

from screens import *
from models import *
session = Session()


class CallerButton(TwoLineListItem):
    def __init__(self,**kwargs):
        super(CallerButton,self).__init__(**kwargs)

    def on_touch_down(self,touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            print('calling')
            notiff = AndroidNotification()
            title = 'goshen'
            notiff.notify(title= title, message='Calling ', app_name='goshen_app',app_icon='tower.ico',timeout=10)






class Directory(Screen,FloatLayout):
    ml = ObjectProperty(None)
    scroller = ObjectProperty(None)
    def load_contacts(self):
        for name,number in session.query(Person.name,Person.number):
            self.ids.ml.add_widget(CallerButton(text=str(name),secondary_text=str(number)))
                





class Drawer(NavigationDrawer):
    def __init__(self,**kwargs):
        super(Drawer, self).__init__(**kwargs)








######################################
class AvatarSampleWidget(ILeftBody, Image):
    pass
class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass
class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass
#########################################################################







class Jarvis(App):
    def __init__(self, **kwargs):
        super(Jarvis, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        if key == 27:
            return self.onBackButton()

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
        goshen_tv = GoshenTV(name= 'goshen_tv')
        gallery = Gallery(name='gallery')

        self.my_screenmanager.add_widget(main_screen)
        self.my_screenmanager.add_widget(testimonies)
        self.my_screenmanager.add_widget(pastors)
        self.my_screenmanager.add_widget(requests)
        self.my_screenmanager.add_widget(sermons)
        self.my_screenmanager.add_widget(guide)
        self.my_screenmanager.add_widget(announcements)
        self.my_screenmanager.add_widget(donations)
        self.my_screenmanager.add_widget(directory)
        self.my_screenmanager.add_widget(goshen_tv)
        self.my_screenmanager.add_widget(gallery)



        self.screen_list = ['screen1']
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
        if self.screen_list:
            self.my_screenmanager.current = self.screen_list.pop()
            return True

        return False


    def on_pause(self):
        return True

    def on_resume(self):
        pass

if __name__=="__main__":
    from kivy.core.text import LabelBase
    LabelBase.register(name="Roboto",
                       fn_regular="Roboto-Regular.ttf",
                       fn_bold="Roboto-Thin.ttf")
    LabelBase.register(name="Icons",
                       fn_regular="icons.ttf",
                       fn_bold="icons.ttf")
    Jarvis().run()
