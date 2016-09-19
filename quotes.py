from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from mat.list import MDList
from mat.grid import SmartTile,SmartTileWithLabel
from mat.button import MDFloatingActionButton
import threading
from mat.list import OneLineListItem,OneLineAvatarListItem
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import mat.snackbar as Snackbar
from kivy.uix.image import AsyncImage
from mat.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch
#convert this into python2 format before building

from models_sql import *
import _thread
session = Session()

from kivy.clock import Clock


