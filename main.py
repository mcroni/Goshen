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

from os.path import dirname
from os.path import join
from os.path import realpath


from plyer import notification
from plyer.utils import platform
from plyer.compat import PY2


from models import *
from pony.orm import *

db = Database()
db.bind('sqlite','details.sqlite')


class Drawer(NavigationDrawer):
    spinner = ObjectProperty(None)
    scroll_v = ObjectProperty(None)
    two_item = ObjectProperty(None)
    ml = ObjectProperty(None)

    def __init__(self,**kwargs):
        super(Drawer, self).__init__(**kwargs)

    def load(self):
        with db_session:
            persons = select(p for p in Person)
            for p in persons:
                #self.ids.scroll_v.add_widget(Button(text=p.name))
                print(("{} \t {}").format(p.name, p.number))






class GoshenTV(Screen):
    pass
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    #list of previous screens
class Testimonies(Screen, BoxLayout):
    def __init__(self, **kwargs):
        super(Testimonies, self).__init__(**kwargs)
class Requests(Screen):
    def do_notify(self, mode='normal'):
        title = 'Goshen Notify'
        message = 'You Have A New Message'
        # ticker = self.ids.ticker_text.text
        if PY2:
            title = title.decode('utf8')
            message = message.decode('utf8')
        kwargs = {'title': title, 'message': message,}

        if mode == 'fancy':
            kwargs['app_name'] = "Plyer Notification Example"
            if platform == "win":
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'tower.ico')
                kwargs['timeout'] = 4
            else:
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'tower.png')
        notification.notify(**kwargs)
class Sermons(Screen):
    pass
class Guide(Screen):
    pass
class Pastors(Screen, FloatLayout):
    pas_text_field = ObjectProperty(None)
    name_text_field = ObjectProperty(None)


    def register(self):
        p = Popup(title='Register',size_hint=(.8, None),height=dp(200))
        b = BoxLayout(orientation= 'vertical')
        text_field = SingleLineTextField(hint_text='name')
        pass_field = SingleLineTextField(hint_text='password')
        button = MDRaisedButton(text="Register")
        b.add_widget(text_field)
        b.add_widget(pass_field)
        b.add_widget(button)

        p.add_widget(b)
        p.open()
    def print_names(self):
        print(self.ids.pas_text_field.text,self.ids.name_text_field.text)

    












class Announcements(Screen):
    pass
class Calender(Screen):
    pass
class Donations(Screen):
    pass





class Directory(Screen):
    ml = ObjectProperty(None)
    scroll = ObjectProperty(None)
    one = ObjectProperty(None)
    def load(self):
        contacts = [
            ["Annie", "555-24235",],
            ["Bob", "555-15423",],
            ["Claire", "555-66098",]
        ]
        for c in contacts:
            print(c)
            self.ids.ml.add_widget(OneLineListItem(text=str(contacts[0])))


    def load_contacts(self):
        with db_session:
            persons = select(p for p in Person)
            for p in persons:
                # self.ids.scroll_v.add_widget(Button(text=p.name))
                #print(("{} \t {}").format(p.name, p.number))
                self.ids.ml.add_widget(TwoLineListItem(text=str(p.name),
                                                       secondary_text=str((p.number))))






class AvatarSampleWidget(ILeftBody, Image):
    pass




class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass

class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


######################3
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



        self.screen_list = ['screen1']
        self.theme_cls.theme_style = 'Dark'



        self.nav_drawer = Drawer()
        self.do_notify(mode='fancy')
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

    def do_notify(self, mode='normal'):
        title = 'Goshen Notify'
        message = 'You Have A New Message'
        # ticker = self.ids.ticker_text.text
        if PY2:
            title = title.decode('utf8')
            message = message.decode('utf8')
        kwargs = {'title': title, 'message': message,}

        if mode == 'fancy':
            kwargs['app_name'] = "Plyer Notification Example"
            if platform == "win":
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'tower.ico')
                kwargs['timeout'] = 4
            else:
                kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'tower.png')

if __name__=="__main__":
    from kivy.core.text import LabelBase
    LabelBase.register(name="Roboto",
                       fn_regular="Roboto-Regular.ttf",
                       fn_bold="Roboto-Thin.ttf")
    LabelBase.register(name="Icons",
                       fn_regular="icons.ttf",
                       fn_bold="icons.ttf")
    Jarvis().run()
