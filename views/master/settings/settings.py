from tkinter import *
from views.master.settings.settings_designer import SettingsDesigner
from views.master.settings.photo.form_photo_designer import FormPhotoDesigner
from views.master.settings.profile.form_profile_designer import FormProfileDesigner

class Settings(SettingsDesigner):
    def __init__(self, main_body, id):
        self.id = id
        super().__init__(main_body)
        self.main_body = main_body
        self.side_menu_controls()

    def side_menu_controls(self):
        menu_width = 20
        menu_height = 2

        self.btnPhoto = Button(self.SettingsMenu, font=('roborto', 15), bg='#f1faff')
        self.btnprofile = Button(self.SettingsMenu, font=('roborto', 15), bg='#f1faff')
        self.btnAudit = Button(self.SettingsMenu, font=('roborto', 15), bg='#f1faff')
        self.btnRestore = Button(self.SettingsMenu, font=('roborto', 15), bg='#f1faff')
        self.btnBackup = Button(self.SettingsMenu, font=('roborto', 15), bg='#f1faff')

        btn_info = [
            ('Photo', self.btnPhoto, self.open_form_photo),
            ('Profile', self.btnprofile, self.open_form_profile),
            ('Audit', self.btnAudit, self.open_form_audit),
            ('Restore', self.btnRestore, self.open_form_restore),
            ('BackUp', self.btnBackup, self.open_form_backup)
        ]

        for text, btn, command in btn_info:
            self.btn_menu_config(btn, text, menu_width, menu_height, command)

    def btn_menu_config(self, btn, text, menu_width, menu_height, command):
        btn.config(text=text, anchor='w', bd=0, fg='black', width=menu_width, height=menu_height, command=command)
        btn.pack(side='top', fill='x')
        self.bind_hover_events(btn)
        
    def bind_hover_events(self, btn):
        btn.bind("<Enter>", lambda event:self.on_enter(event, btn))
        btn.bind("<Leave>", lambda event:self.on_leave(event, btn))
    
    def on_enter(self, event, btn):
        btn.config(bg='#ebd8d0', fg='black')
        
    def on_leave(self, event, btn):
        btn.config(bg='#f1faff', fg='black')

    def open_form_photo(self):
        self.clean_panel(self.main_body)
        FormPhotoDesigner(self.main_body, Settings, self.id)

    def open_form_profile(self):
        self.clean_panel(self.main_body)
        FormProfileDesigner(self.main_body, Settings, self.id)

    def open_form_audit(self):
        pass

    def open_form_restore(self):
        pass

    def open_form_backup(self):
        pass

    def clean_panel(self, panel):
        for widget in panel.winfo_children():
            widget.destroy()