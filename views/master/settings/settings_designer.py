from tkinter import *

class SettingsDesigner():

    def __init__(self, main_panel):
        self.SettingsMenu = LabelFrame(main_panel, text='Settings Menu', font=("Roborto", 20), padx=5, pady=5, bd=0, bg='#f1faff')
        self.SettingsMenu.pack(side=TOP, expand=NO, fill='both')
        self.SettingsMenu.grid_columnconfigure(1, weight=1)

    def side_menu_controls(self):
        pass

    def btn_menu_config(self, btn, text, icon, menu_width, menu_height):
        pass
        
    def bind_hover_events(self, btn):
        pass
    
    def on_enter(self, event, btn):
        pass
        
    def on_leave(self, event, btn):
        pass