import webbrowser
import random
import datetime
from urllib.parse import quote

import kivymd_fbo_fix  # noqa: F401  # tambalan bug FBO KivyMD 2.0.0, harus diimpor sebelum widget lain

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogContentContainer,
    MDDialogButtonContainer,
)
from kivymd.uix.textfield import MDTextField, MDTextFieldHintText
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.snackbar import MDSnackbar, MDSnackbarText
from kivy.properties import NumericProperty, StringProperty

import database as db

Window.size = (390, 760)

WHATSAPP_NUMBER = "6281957035348"

KV = '''
#:import dp kivy.metrics.dp

ScreenManager:
    SplashScreen:
    LoginScreen:
    RegisterScreen:
    MainScreen:
    MenuScreen:
    ProfileScreen:
    RiwayatScreen:
    AlamatScreen:
    PembayaranScreen:
    NotifikasiScreen:
    TemaScreen:
    BantuanScreen:
    UlasanScreen:

# =============================================
# 1. SPLASH SCREEN
# =============================================
<SplashScreen>:
    name: "splash"
    md_bg_color: 214/255, 206/255, 189/255, 1

    MDBoxLayout:
        orientation: "vertical"
        size_hint: None, None
        size: dp(300), dp(150)
        pos_hint: {"center_x": .5, "center_y": .5}
        
        MDLabel:
            text: "SELAMAT DATANG DI\\nPENTOL MAMA RETA"
            halign: "center"
            font_style: "Title"
            bold: True
            size_hint_y: None
            height: dp(70)
            text_size: self.width, None
            
        Widget:
            size_hint_y: None
            height: dp(24) 

        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            
            Widget:

            MDButton:
                style: "filled"
                theme_bg_color: "Custom"
                md_bg_color: 72/255, 50/255, 36/255, 1
                pos_hint: {"center_x": .5}
                on_release: app.root.current = "login"

                MDButtonText:
                    text: "Tekan Di sini"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1

            Widget:
        
# =============================================
# 2. LOGIN SCREEN
#=============================================
<LoginScreen>:
    name: "login"
    md_bg_color: 221/255, 211/255, 192/255, 1

    MDBoxLayout:
        orientation: "vertical"

        MDFloatLayout:
            size_hint_y: None
            height: dp(190)
            md_bg_color: 62/255, 42/255, 30/255, 1

            MDBoxLayout:
                orientation: "vertical"
                size_hint: None, None
                size: dp(260), dp(120)
                pos_hint: {"center_x": .5, "center_y": .62}
                spacing: dp(4)

                Widget:
                    size_hint: None, None
                    size: dp(60), dp(60)
                    pos_hint: {"center_x": .5}
                    canvas.before:
                        Color:
                            rgba: 232/255, 163/255, 61/255, 1
                        Ellipse:
                            pos: self.pos
                            size: self.size

                MDLabel:
                    text: "[b]Pentol[/b] [color=E8A33D]Mama Reta[/color]"
                    markup: True
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    size_hint_y: None
                    height: dp(26)
                    text_size: self.width, None

                MDLabel:
                    text: "Pentol Lumer Keju - Kediri"
                    halign: "center"
                    font_style: "Body"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 201/255, 191/255, 174/255, 1
                    size_hint_y: None
                    height: dp(20)
                    text_size: self.width, None

        ScrollView:
            MDBoxLayout:
                id: form_card
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(28), dp(26), dp(28), dp(26)
                spacing: dp(10)
                radius: [dp(28), dp(28), 0, 0]
                md_bg_color: 221/255, 211/255, 192/255, 1

                MDLabel:
                    text: "Selamat Datang!"
                    bold: True
                    font_style: "Headline"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 62/255, 42/255, 30/255, 1
                    adaptive_height: True

                MDLabel:
                    text: "Masuk untuk menikmati pengalaman pesan lebih mudah."
                    theme_text_color: "Custom"
                    text_color: 45/255, 30/255, 20/255, 1
                    font_style: "Body"
                    role: "medium"
                    adaptive_height: True
                    padding: 0, dp(4), 0, dp(14)

                MDTextField:
                    id: email_field
                    mode: "filled"
                    theme_bg_color: "Custom"
                    theme_line_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Alamat Email"

                Widget:
                    size_hint_y: None
                    height: dp(8)

                MDTextField:
                    id: password_field
                    mode: "filled"
                    theme_bg_color: "Custom"
                    theme_line_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    password: True
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Password"

                Widget:
                    size_hint_y: None
                    height: dp(6)

                MDLabel:
                    id: form_error_label
                    text: ""
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 192/255, 57/255, 43/255, 1
                    font_style: "Body"
                    role: "small"
                    size_hint_y: None
                    height: dp(18) if self.text else 0

                MDButton:
                    style: "filled"
                    theme_bg_color: "Custom"
                    md_bg_color: 192/255, 57/255, 43/255, 1
                    theme_width: "Custom"
                    size_hint_x: 1
                    height: dp(50)
                    radius: [dp(25)]
                    on_release: root.cek_login()

                    MDButtonText:
                        text: "Masuk Sekarang"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        halign: "center"

                MDLabel:
                    text: "atau"
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 45/255, 30/255, 20/255, 1
                    adaptive_height: True
                    padding: 0, dp(8), 0, dp(8)
                    
                MDButton:
                    style: "filled"
                    theme_bg_color: "Custom"
                    md_bg_color: 111/255, 190/255, 68/255, 1
                    theme_width: "Custom"
                    size_hint_x: 1
                    height: dp(50)
                    radius: [dp(25)]
                    on_release: root.lanjut_whatsapp()

                    MDButtonText:
                        text: "Lanjut Via WhatsApp"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        halign: "center"

                MDButton:
                    style: "text"
                    pos_hint: {"center_x": .5}
                    on_release: app.root.current = "register"

                    MDButtonText:
                        text: "Belum punya akun? Daftar di sini"
                        theme_text_color: "Custom"
                        text_color: 62/255, 42/255, 30/255, 1
                        halign: "center"

# =============================================
# 2b. REGISTER SCREEN
# =============================================
<RegisterScreen>:
    name: "register"
    md_bg_color: 221/255, 211/255, 192/255, 1

    MDBoxLayout:
        orientation: "vertical"

        MDFloatLayout:
            size_hint_y: None
            height: dp(140)
            md_bg_color: 62/255, 42/255, 30/255, 1

            MDLabel:
                text: "[b]Buat Akun Baru[/b]"
                markup: True
                halign: "center"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                font_style: "Title"
                pos_hint: {"center_x": .5, "center_y": .5}

        ScrollView:
            MDBoxLayout:
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                padding: dp(28), dp(26), dp(28), dp(26)
                spacing: dp(10)
                radius: [dp(28), dp(28), 0, 0]
                md_bg_color: 221/255, 211/255, 192/255, 1

                MDTextField:
                    id: reg_nama
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Nama Lengkap"

                Widget:
                    size_hint_y: None
                    height: dp(8)

                MDTextField:
                    id: reg_email
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Alamat Email"

                Widget:
                    size_hint_y: None
                    height: dp(8)

                MDTextField:
                    id: reg_password
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    password: True
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Password"

                Widget:
                    size_hint_y: None
                    height: dp(8)

                MDTextField:
                    id: reg_confirm
                    mode: "filled"
                    theme_bg_color: "Custom"
                    fill_color_normal: 1, 1, 1, 1
                    fill_color_focus: 1, 1, 1, 1
                    text_color_normal: 62/255, 42/255, 30/255, 1
                    text_color_focus: 62/255, 42/255, 30/255, 1
                    password: True
                    size_hint_y: None
                    height: dp(56)

                    MDTextFieldHintText:
                        text: "Ulangi Password"

                Widget:
                    size_hint_y: None
                    height: dp(6)

                MDLabel:
                    id: reg_error_label
                    text: ""
                    halign: "center"
                    theme_text_color: "Custom"
                    text_color: 192/255, 57/255, 43/255, 1
                    font_style: "Body"
                    role: "small"
                    size_hint_y: None
                    height: dp(18) if self.text else 0

                MDButton:
                    style: "filled"
                    theme_bg_color: "Custom"
                    md_bg_color: 192/255, 57/255, 43/255, 1
                    size_hint_x: 1
                    height: dp(50)
                    radius: [dp(25)]
                    on_release: root.daftar_akun()

                    MDButtonText:
                        text: "Daftar"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        halign: "center"

                MDButton:
                    style: "text"
                    pos_hint: {"center_x": .5}
                    on_release: app.root.current = "login"

                    MDButtonText:
                        text: "Sudah punya akun? Masuk"
                        theme_text_color: "Custom"
                        text_color: 62/255, 42/255, 30/255, 1
                        halign: "center"

# =========================================================
# 3. MAIN SCREEN (HOME)
# =========================================================
<MainScreen>:
    name: "main"
    md_bg_color: 213/255, 206/255, 189/255, 1

    MDBoxLayout:
        orientation: "vertical"

        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: "84dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: ["16dp", "10dp", "16dp", "8dp"]
            spacing: "4dp"

            MDBoxLayout:
                size_hint_y: None
                height: "26dp"
                spacing: "8dp"
                MDIcon:
                    icon: "face-man-profile"
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                    pos_hint: {"center_y": .5}
                    font_size: "22sp"
                    size: "26dp", "26dp"
                    size_hint: None, None
                MDLabel:
                    text: app.current_user_nama
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body"
                    role: "medium"
                    pos_hint: {"center_y": .5}

            MDBoxLayout:
                size_hint_y: None
                height: "32dp"
                spacing: "8dp"
                MDLabel:
                    text: "[b]PENTOL[/b] [color=FCBA03]MAMA RETA[/color]"
                    markup: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Title"
                    role: "medium"
                    adaptive_width: True
                    pos_hint: {"center_y": .5}
                MDLabel:
                    text: "[color=FCBA03][b]Home[/b][/color]    Menu    Profile"
                    markup: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Label"
                    role: "large"
                    halign: "right"
                    pos_hint: {"center_y": .5}

        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True

                MDRelativeLayout:
                    size_hint_y: None
                    height: "380dp"

                    FitImage:
                        source: 'kelas.jpeg'

                    MDBoxLayout:
                        md_bg_color: 0, 0, 0, 0.78

                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "28dp"
                        spacing: "12dp"
                        pos_hint: {"center_x": .5, "center_y": .5}
                        adaptive_height: True

                        MDLabel:
                            text: "Sensasi Pedas\\n[color=FCBA03]Pentol Lumer[/color] Keju"
                            markup: True
                            font_style: "Headline"
                            role: "small"
                            bold: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            adaptive_height: True
                            text_size: self.width, None

                        MDLabel:
                            text: "Nikmati bakso premium dengan isian keju lumer melimpah dibalut sambal jawara pedas membara."
                            halign: "center"
                            font_style: "Body"
                            role: "small"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 0.9
                            adaptive_height: True
                            text_size: self.width, None

                        MDButton:
                            style: "filled"
                            theme_bg_color: "Custom"
                            md_bg_color: 62/255, 42/255, 30/255, 1
                            pos_hint: {"center_x": .5}
                            on_release: app.root.current = "menu"

                            MDButtonText:
                                text: "Lihat Menu"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1

        # --- BOTTOM NAV ---
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: ["10dp", "10dp"]
            
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                MDIcon:
                    icon: "home"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                MDLabel:
                    text: "Home"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                    
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "menu"
                MDIcon:
                    icon: "format-list-bulleted"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Menu"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                    
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "profile"
                MDIcon:
                    icon: "account-outline"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Profil"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1

# =========================================================
# 4. MENU SCREEN (DENGAN TAMBAH & HAPUS MENU BEBAS)
# =========================================================
<MenuScreen>:
    name: "menu"
    md_bg_color: 213/255, 206/255, 189/255, 1

    MDBoxLayout:
        orientation: "vertical"

        # HEADER
        MDBoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: "84dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: ["16dp", "10dp", "16dp", "8dp"]
            spacing: "4dp"

            MDBoxLayout:
                size_hint_y: None
                height: "26dp"
                spacing: "8dp"
                MDIcon:
                    icon: "face-man-profile"
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                    pos_hint: {"center_y": .5}
                    font_size: "22sp"
                    size: "26dp", "26dp"
                    size_hint: None, None
                MDLabel:
                    text: app.current_user_nama
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Body"
                    role: "medium"
                    pos_hint: {"center_y": .5}

            MDBoxLayout:
                size_hint_y: None
                height: "32dp"
                spacing: "8dp"
                MDLabel:
                    text: "[b]PENTOL[/b] [color=FCBA03]MAMA RETA[/color]"
                    markup: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Title"
                    role: "medium"
                    adaptive_width: True
                    pos_hint: {"center_y": .5}
                MDLabel:
                    text: "Home    [color=FCBA03][b]Menu[/b][/color]    Profile"
                    markup: True
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    font_style: "Label"
                    role: "large"
                    halign: "right"
                    pos_hint: {"center_y": .5}

        MDFloatLayout:
            MDScrollView:
                MDBoxLayout:
                    id: container_menu
                    orientation: "vertical"
                    adaptive_height: True
                    padding: ["15dp", "20dp", "15dp", "120dp"]
                    spacing: "20dp"

                    # TOMBOL TAMBAH MENU
                    MDButton:
                        style: "filled"
                        theme_bg_color: "Custom"
                        md_bg_color: 192/255, 57/255, 43/255, 1
                        size_hint_x: 1
                        height: "48dp"
                        on_release: app.buka_dialog_tambah_menu()
                        
                        MDButtonText:
                            text: "+ Tambah Menu Lainnya (Soto, Es Teh, dll)"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            pos_hint: {"center_x": .5, "center_y": .5}

            # CART SUMMARY BAR
            MDCard:
                size_hint_y: None
                size_hint_x: None
                width: root.width - dp(30)
                height: "65dp"
                pos_hint: {"center_x": .5, "y": .03}
                radius: [30]
                theme_bg_color: "Custom"
                md_bg_color: 235/255, 235/255, 235/255, 1
                padding: ["25dp", "0dp", "15dp", "0dp"]
                elevation: 2
                
                MDLabel:
                    text: app.total_harga_str
                    markup: True
                    theme_text_color: "Custom"
                    text_color: 0, 0, 0, 1
                    font_style: "Title"
                    pos_hint: {"center_y": .5}
                    
                MDBoxLayout:
                    adaptive_width: True
                    spacing: "15dp"
                    pos_hint: {"center_y": .5}
                    
                    MDLabel:
                        text: "Total Item: " + str(app.total_item)
                        bold: True
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1
                        adaptive_width: True
                        pos_hint: {"center_y": .5}

                    MDButton:
                        style: "filled"
                        theme_bg_color: "Custom"
                        md_bg_color: 192/255, 57/255, 43/255, 1
                        radius: [20]
                        pos_hint: {"center_y": .5}
                        on_release: app.checkout_pesanan()

                        MDButtonText:
                            text: "Checkout"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1

        # --- BOTTOM NAV ---
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: ["10dp", "10dp"]
            
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "main"
                MDIcon:
                    icon: "home"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Home"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                    
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "menu"
                MDIcon:
                    icon: "format-list-bulleted"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                MDLabel:
                    text: "Menu"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                    
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "profile"
                MDIcon:
                    icon: "account-outline"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Profil"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1

# =========================================================
# PROFILE & SETTING SCREENS
# =========================================================
<ProfileScreen>:
    name: "profile"
    md_bg_color: 213/255, 206/255, 189/255, 1 
    MDBoxLayout:
        orientation: "vertical"
        MDFloatLayout:
            MDBoxLayout:
                size_hint_y: None
                height: "300dp"
                md_bg_color: 62/255, 42/255, 30/255, 1
                pos_hint: {"top": 1}
            MDScrollView:
                MDBoxLayout:
                    orientation: "vertical"
                    adaptive_height: True
                    padding: ["0dp", "40dp", "0dp", "60dp"]
                    spacing: "25dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        adaptive_height: True
                        spacing: "8dp"
                        MDBoxLayout:
                            size_hint: None, None
                            size: "90dp", "90dp"
                            pos_hint: {"center_x": .5}
                            radius: [45]
                            md_bg_color: 90/255, 150/255, 225/255, 1 
                            MDIcon:
                                icon: "face-man-profile"
                                font_size: "60sp"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                pos_hint: {"center_x": .5, "center_y": .5}
                        MDLabel:
                            text: "[b]" + app.current_user_nama + "[/b]"
                            markup: True
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            font_style: "Title"
                            adaptive_height: True
                        MDLabel:
                            text: app.current_user_email
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 0.8
                            font_style: "Body"
                            role: "small"
                            adaptive_height: True
                    MDCard:
                        size_hint_y: None
                        height: "75dp"
                        size_hint_x: None
                        width: root.width - dp(60)
                        pos_hint: {"center_x": .5}
                        radius: [15]
                        theme_bg_color: "Custom"
                        md_bg_color: 140/255, 120/255, 105/255, 1 
                        elevation: 0
                        padding: "10dp"
                        MDBoxLayout:
                            orientation: "horizontal"
                            MDBoxLayout:
                                orientation: "vertical"
                                pos_hint: {"center_y": .5}
                                adaptive_height: True
                                MDLabel:
                                    text: "[b]10[/b]"
                                    markup: True
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 252/255, 186/255, 3/255, 1
                                    adaptive_height: True
                                MDLabel:
                                    text: "Pesanan"
                                    halign: "center"
                                    font_style: "Label"
                                    role: "small"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    adaptive_height: True
                            MDBoxLayout:
                                orientation: "vertical"
                                pos_hint: {"center_y": .5}
                                adaptive_height: True
                                MDLabel:
                                    text: "[b]4.9[/b]" 
                                    markup: True
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 252/255, 186/255, 3/255, 1
                                    adaptive_height: True
                                MDLabel:
                                    text: "Rating"
                                    halign: "center"
                                    font_style: "Label"
                                    role: "small"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    adaptive_height: True
                            MDBoxLayout:
                                orientation: "vertical"
                                pos_hint: {"center_y": .5}
                                adaptive_height: True
                                MDLabel:
                                    text: "[b]1th[/b]"
                                    markup: True
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 252/255, 186/255, 3/255, 1
                                    adaptive_height: True
                                MDLabel:
                                    text: "Bergabung"
                                    halign: "center"
                                    font_style: "Label"
                                    role: "small"
                                    theme_text_color: "Custom"
                                    text_color: 1, 1, 1, 1
                                    adaptive_height: True
                    MDCard:
                        orientation: "vertical"
                        size_hint_y: None
                        height: self.minimum_height
                        size_hint_x: None
                        width: root.width - dp(40)
                        pos_hint: {"center_x": .5}
                        radius: [15]
                        theme_bg_color: "Custom"
                        md_bg_color: 85/255, 60/255, 45/255, 1 
                        elevation: 0
                        padding: ["15dp", "10dp", "15dp", "10dp"]
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "55dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0 
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "riwayat"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Riwayat Pesanan[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                            MDLabel:
                                text: "10 pesanan selesai"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.7
                                font_style: "Label"
                                role: "small"
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1 
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "55dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "alamat"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Alamat Pengiriman[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                            MDLabel:
                                text: "Kediri, Jawa Timur"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.7
                                font_style: "Label"
                                role: "small"
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "55dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "pembayaran"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Metode Pembayaran[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                            MDLabel:
                                text: "Kediri, Jawa Timur"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.7
                                font_style: "Label"
                                role: "small"
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "55dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "notifikasi"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Notifikasi[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                            MDLabel:
                                text: "Aktif"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.7
                                font_style: "Label"
                                role: "small"
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "55dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "tema"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Tema Aplikasi[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                            MDLabel:
                                text: "Terang"
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 0.7
                                font_style: "Label"
                                role: "small"
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "45dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "bantuan"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Bantuan & FAQ[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                                pos_hint: {"center_y": .5}
                        MDBoxLayout:
                            size_hint_y: None
                            height: "1dp"
                            md_bg_color: 1, 1, 1, 0.1
                        MDCard:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "45dp"
                            theme_bg_color: "Custom"
                            md_bg_color: 0, 0, 0, 0
                            elevation: 0
                            ripple_behavior: True
                            on_release: app.root.current = "ulasan"
                            padding: ["5dp", "5dp", "5dp", "5dp"]
                            MDLabel:
                                text: "[b]Beri Ulasan Aplikasi[/b]"
                                markup: True
                                theme_text_color: "Custom"
                                text_color: 1, 1, 1, 1
                                font_style: "Body"
                                role: "small"
                                pos_hint: {"center_y": .5}
        # BOTTOM NAV
        MDBoxLayout:
            size_hint_y: None
            height: "70dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: ["10dp", "10dp"]
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "main"
                MDIcon:
                    icon: "home"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Home"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "menu"
                MDIcon:
                    icon: "format-list-bulleted"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
                MDLabel:
                    text: "Menu"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 0.6, 0.6, 0.6, 1
            MDCard:
                orientation: "vertical"
                theme_bg_color: "Custom"
                md_bg_color: 0, 0, 0, 0
                elevation: 0
                ripple_behavior: True
                on_release: app.root.current = "profile"
                MDIcon:
                    icon: "account-outline"
                    pos_hint: {"center_x": .5}
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1
                MDLabel:
                    text: "Profil"
                    halign: "center"
                    font_style: "Label"
                    role: "small"
                    theme_text_color: "Custom"
                    text_color: 252/255, 186/255, 3/255, 1

# KUMPULAN LAYAR Pengaturan
<RiwayatScreen>:
    name: "riwayat"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Riwayat Pesanan"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                id: container_riwayat
                orientation: "vertical"
                padding: "16dp"
                spacing: "10dp"
                adaptive_height: True

<AlamatScreen>:
    name: "alamat"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Alamat Saya"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                adaptive_height: True
                MDCard:
                    orientation: "vertical"
                    size_hint_y: None
                    height: "120dp"
                    padding: "15dp"
                    theme_bg_color: "Custom"
                    md_bg_color: 255/255, 255/255, 255/255, 1
                    radius: [10]
                    MDLabel:
                        text: "[b]Kelas bro[/b] | (+62) 819-5703-5348"
                        markup: True
                    MDLabel:
                        text: "Jl. Kediri Raya No. 12, Jawa Timur\\n[color=E8A33D][Utama][/color]"
                        markup: True
                        theme_text_color: "Custom"
                        text_color: 0.4, 0.4, 0.4, 1

<PembayaranScreen>:
    name: "pembayaran"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Metode Pembayaran"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                spacing: "10dp"
                adaptive_height: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    padding: "15dp"
                    theme_bg_color: "Custom"
                    md_bg_color: 255/255, 255/255, 255/255, 1
                    radius: [10]
                    MDLabel:
                        text: "Bayar di Tempat (COD)"
                        pos_hint: {"center_y": .5}
                    MDIcon:
                        icon: "check-circle"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                        pos_hint: {"center_y": .5}

<NotifikasiScreen>:
    name: "notifikasi"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Pengaturan Notifikasi"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                spacing: "10dp"
                adaptive_height: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    padding: "15dp"
                    theme_bg_color: "Custom"
                    md_bg_color: 255/255, 255/255, 255/255, 1
                    radius: [10]
                    MDLabel:
                        text: "Notifikasi Promo & Diskon"
                        pos_hint: {"center_y": .5}
                    MDIcon:
                        icon: "toggle-switch"
                        font_size: "40sp"
                        theme_text_color: "Custom"
                        text_color: 111/255, 190/255, 68/255, 1
                        pos_hint: {"center_y": .5}

<TemaScreen>:
    name: "tema"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Tema Aplikasi"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                spacing: "10dp"
                adaptive_height: True
                MDCard:
                    size_hint_y: None
                    height: "60dp"
                    padding: "15dp"
                    theme_bg_color: "Custom"
                    md_bg_color: 255/255, 255/255, 255/255, 1
                    radius: [10]
                    MDLabel:
                        text: "Tema Terang (Light)"
                        pos_hint: {"center_y": .5}
                    MDIcon:
                        icon: "check-circle"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                        pos_hint: {"center_y": .5}

<BantuanScreen>:
    name: "bantuan"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Pusat Bantuan"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "16dp"
                spacing: "10dp"
                adaptive_height: True
                MDCard:
                    orientation: "vertical"
                    size_hint_y: None
                    height: "100dp"
                    padding: "15dp"
                    theme_bg_color: "Custom"
                    md_bg_color: 255/255, 255/255, 255/255, 1
                    radius: [10]
                    MDLabel:
                        text: "[b]Bagaimana cara pesan?[/b]"
                        markup: True
                    MDLabel:
                        text: "Buka menu, pilih pentol, lalu tekan tombol checkout atau lanjut via WhatsApp."
                        theme_text_color: "Custom"
                        text_color: 0.4, 0.4, 0.4, 1

<UlasanScreen>:
    name: "ulasan"
    md_bg_color: 213/255, 206/255, 189/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y: None
            height: "56dp"
            md_bg_color: 62/255, 42/255, 30/255, 1
            padding: "8dp"
            MDIconButton:
                icon: "arrow-left"
                theme_icon_color: "Custom"
                icon_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
                on_release: app.root.current = "profile"
            MDLabel:
                text: "Beri Ulasan"
                font_style: "Title"
                role: "medium"
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos_hint: {"center_y": .5}
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                padding: "20dp"
                spacing: "15dp"
                adaptive_height: True
                MDLabel:
                    text: "Bagaimana pengalamanmu?"
                    halign: "center"
                    bold: True
                MDBoxLayout:
                    adaptive_width: True
                    pos_hint: {"center_x": .5}
                    MDIcon:
                        icon: "star"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                    MDIcon:
                        icon: "star"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                    MDIcon:
                        icon: "star"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                    MDIcon:
                        icon: "star"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                    MDIcon:
                        icon: "star-outline"
                        theme_text_color: "Custom"
                        text_color: 252/255, 186/255, 3/255, 1
                MDButton:
                    style: "filled"
                    theme_bg_color: "Custom"
                    md_bg_color: 192/255, 57/255, 43/255, 1
                    pos_hint: {"center_x": .5}
                    MDButtonText:
                        text: "Kirim Ulasan"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
'''


class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    def cek_login(self):
        email = self.ids.email_field.text.strip()
        password = self.ids.password_field.text.strip()

        if not email or not password:
            self.ids.form_error_label.text = "Email dan password tidak boleh kosong!"
            return

        user = db.login_user(email, password)
        if user is None:
            self.ids.form_error_label.text = "Email atau password salah!"
            return

        app = MDApp.get_running_app()
        app.current_user_id = user["id"]
        app.current_user_nama = user["nama"]
        app.current_user_email = user["email"]

        self.ids.form_error_label.text = ""
        self.ids.email_field.text = ""
        self.ids.password_field.text = ""
        self.manager.current = "main"

    def lanjut_whatsapp(self):
        pesan = "Halo, saya ingin memesan Pentol Mama Reta."
        url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(pesan)}"
        try:
            webbrowser.open(url)
        except Exception:
            pass


class RegisterScreen(MDScreen):
    def daftar_akun(self):
        nama = self.ids.reg_nama.text.strip()
        email = self.ids.reg_email.text.strip()
        password = self.ids.reg_password.text.strip()
        confirm = self.ids.reg_confirm.text.strip()

        if not nama or not email or not password or not confirm:
            self.ids.reg_error_label.text = "Semua kolom wajib diisi!"
            return

        if password != confirm:
            self.ids.reg_error_label.text = "Password dan konfirmasi tidak sama!"
            return

        sukses, pesan = db.daftar_user(nama, email, password)
        if not sukses:
            self.ids.reg_error_label.text = pesan
            return

        # Bersihkan form & beri notifikasi
        self.ids.reg_error_label.text = ""
        self.ids.reg_nama.text = ""
        self.ids.reg_email.text = ""
        self.ids.reg_password.text = ""
        self.ids.reg_confirm.text = ""

        MDSnackbar(
            MDSnackbarText(text=pesan),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()
        self.manager.current = "login"


class MainScreen(MDScreen):
    pass
    
class ProfileScreen(MDScreen):
    pass

class RiwayatScreen(MDScreen):
    def on_enter(self, *args):
        app = MDApp.get_running_app()
        container = self.ids.container_riwayat
        container.clear_widgets()

        daftar = db.get_riwayat_by_user(app.current_user_id)

        if not daftar:
            container.add_widget(
                MDLabel(
                    text="Belum ada riwayat pesanan.",
                    halign="center",
                    adaptive_height=True,
                )
            )
            return

        for row in daftar:
            kartu = MDCard(
                orientation="vertical",
                size_hint_y=None,
                height="100dp",
                padding="15dp",
                theme_bg_color="Custom",
                md_bg_color=(1, 1, 1, 1),
                radius=[10],
            )
            kartu.add_widget(
                MDLabel(
                    text=f"[b]Pesanan Selesai[/b] - #{row['kode_transaksi']}",
                    markup=True,
                    adaptive_height=True,
                )
            )
            kartu.add_widget(
                MDLabel(
                    text=f"{row['detail_item']}  |  {row['tanggal']}",
                    theme_text_color="Custom",
                    text_color=(0.5, 0.5, 0.5, 1),
                    adaptive_height=True,
                )
            )
            kartu.add_widget(
                MDLabel(
                    text=f"[color=E8A33D][b]Rp {row['total_harga']:,}[/b][/color]",
                    markup=True,
                    adaptive_height=True,
                )
            )
            container.add_widget(kartu)

class AlamatScreen(MDScreen):
    pass

class PembayaranScreen(MDScreen):
    pass

class NotifikasiScreen(MDScreen):
    pass

class TemaScreen(MDScreen):
    pass

class BantuanScreen(MDScreen):
    pass

class UlasanScreen(MDScreen):
    pass


class ProductCard(MDCard):
    produk_id = NumericProperty(0)
    nama = StringProperty("")
    harga = NumericProperty(0)
    deskripsi = StringProperty("")
    jumlah = NumericProperty(0)
    gambar = StringProperty("")

    def tambah_qty(self):
        self.jumlah += 1
        MDApp.get_running_app().hitung_total()

    def kurang_qty(self):
        if self.jumlah > 0:
            self.jumlah -= 1
            MDApp.get_running_app().hitung_total()

    def hapus_menu(self):
        app = MDApp.get_running_app()
        # Hapus produk dari database berdasarkan id
        db.hapus_produk(self.produk_id)
        app.muat_daftar_menu()


class MenuScreen(MDScreen):
    def on_enter(self, *args):
        app = MDApp.get_running_app()
        app.muat_daftar_menu()


class PentolApp(MDApp):
    total_harga_str = StringProperty("[b]Rp. 0[/b]")
    total_item = NumericProperty(0)

    # Data user yang sedang login (diisi setelah cek_login berhasil)
    current_user_id = NumericProperty(0)
    current_user_nama = StringProperty("Pengguna")
    current_user_email = StringProperty("")

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"
        db.init_db()  # siapkan tabel & data menu awal di database
        return Builder.load_string(KV)

    def on_start(self):
        self.muat_daftar_menu()

    def muat_daftar_menu(self):
        try:
            menu_screen = self.root.get_screen("menu")
            container = menu_screen.ids.container_menu
            
            tombol_tambah = None
            for child in list(container.children):
                if isinstance(child, MDButton):
                    tombol_tambah = child
                container.remove_widget(child)

            for produk in db.get_all_produk():
                produk_id = produk["id"]
                nama = produk["nama"]
                harga = produk["harga"]
                desk = produk["deskripsi"] or ""
                img = produk["gambar"] or "tugas2.jpeg"
                qty = 1  # jumlah pesanan selalu mulai dari 1 setiap menu dimuat

                card = ProductCard(
                    produk_id=produk_id,
                    nama=nama,
                    harga=harga,
                    deskripsi=desk,
                    gambar=img,
                    jumlah=qty,
                    size_hint_y=None,
                    height="170dp",
                    padding="10dp",
                    spacing="15dp",
                    radius=[30],
                    md_bg_color=(62/255, 42/255, 30/255, 1),
                    elevation=0
                )
                
                from kivymd.uix.fitimage import FitImage
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.label import MDLabel
                from kivymd.uix.button import MDIconButton
                from kivy.uix.widget import Widget

                # Gambar Produk
                img_widget = FitImage(source=img if img else "tugas2.jpeg", size_hint=(None, None), size=("120dp", "120dp"), radius=[60], pos_hint={"center_y": .5})
                card.add_widget(img_widget)

                vbox = MDBoxLayout(orientation="vertical", spacing="3dp")
                
                # Baris Atas Kartu (Nama Menu & Tombol Hapus X)
                hbox_atas = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="26dp")
                lbl_nama = MDLabel(text=f"[b]{nama}[/b]", markup=True, theme_text_color="Custom", text_color=(1,1,1,1), font_style="Body", role="large", pos_hint={"center_y": .5})
                
                btn_hapus = MDIconButton(icon="delete", theme_bg_color="Custom", md_bg_color=(192/255, 57/255, 43/255, 1), theme_icon_color="Custom", icon_color=(1,1,1,1), size_hint=(None, None), size=("24dp", "24dp"), pos_hint={"center_y": .5})
                btn_hapus.bind(on_release=lambda x, c=card: c.hapus_menu())

                hbox_atas.add_widget(lbl_nama)
                hbox_atas.add_widget(btn_hapus)

                # Deskripsi
                lbl_desc = MDLabel(text=desk, theme_text_color="Custom", text_color=(1,1,1,0.7), font_style="Label", role="small")
                
                # Baris Bawah (Harga & Counter)
                hbox_bawah = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp", spacing="5dp")
                lbl_harga = MDLabel(text=f"[color=E8A33D][b]Rp {harga:,}[/b][/color] [size=10](pcs)[/size]", markup=True, theme_text_color="Custom", text_color=(1,1,1,1), font_style="Body", role="small", pos_hint={"center_y": .5}, size_hint_x=None, width="90dp")
                
                hbox_bawah.add_widget(lbl_harga)
                hbox_bawah.add_widget(Widget())

                hbox_counter = MDBoxLayout(adaptive_width=True, spacing="6dp", pos_hint={"center_y": .5})
                
                btn_min = MDIconButton(icon="minus", theme_bg_color="Custom", md_bg_color=(0.4, 0.4, 0.4, 1), theme_icon_color="Custom", icon_color=(1,1,1,1), size_hint=(None, None), size=("24dp", "24dp"), pos_hint={"center_y": .5})
                btn_min.bind(on_release=lambda x, c=card: c.kurang_qty())

                lbl_qty = MDLabel(text=str(qty), theme_text_color="Custom", text_color=(1,1,1,1), adaptive_width=True, pos_hint={"center_y": .5})
                card.bind(jumlah=lambda instance, value, l=lbl_qty: setattr(l, 'text', str(value)))

                btn_plus = MDIconButton(icon="plus", theme_bg_color="Custom", md_bg_color=(192/255, 57/255, 43/255, 1), theme_icon_color="Custom", icon_color=(1,1,1,1), size_hint=(None, None), size=("24dp", "24dp"), pos_hint={"center_y": .5})
                btn_plus.bind(on_release=lambda x, c=card: c.tambah_qty())

                hbox_counter.add_widget(btn_min)
                hbox_counter.add_widget(lbl_qty)
                hbox_counter.add_widget(btn_plus)

                hbox_bawah.add_widget(hbox_counter)

                vbox.add_widget(hbox_atas)
                vbox.add_widget(lbl_desc)
                vbox.add_widget(hbox_bawah)

                card.add_widget(vbox)
                container.add_widget(card)

            if tombol_tambah:
                container.add_widget(tombol_tambah)
            
            self.hitung_total()
        except Exception as e:
            print("Error saat memuat menu:", e)

    def buka_dialog_tambah_menu(self):
        # Buat Input Text untuk Nama, Harga, dan Deskripsi Menu Baru
        self.input_nama_menu = MDTextField(
            MDTextFieldHintText(text="Nama Menu (Contoh: Es Teh / Soto)"),
            mode="filled",
            size_hint_y=None,
            height="50dp"
        )
        self.input_harga_menu = MDTextField(
            MDTextFieldHintText(text="Harga (Contoh: 5000)"),
            mode="filled",
            size_hint_y=None,
            height="50dp"
        )
        self.input_desk_menu = MDTextField(
            MDTextFieldHintText(text="Deskripsi Singkat"),
            mode="filled",
            size_hint_y=None,
            height="50dp"
        )

        content_box = MDDialogContentContainer(
            orientation="vertical",
            spacing="12dp",
            size_hint_y=None,
            height="180dp"
        )
        content_box.add_widget(self.input_nama_menu)
        content_box.add_widget(self.input_harga_menu)
        content_box.add_widget(self.input_desk_menu)

        self.dialog_menu = MDDialog(
            MDDialogHeadlineText(text="Tambah Menu Baru"),
            content_box,
            MDDialogButtonContainer(
                Widget(),
                MDButton(
                    MDButtonText(text="Batal"),
                    style="text",
                    on_release=lambda x: self.dialog_menu.dismiss()
                ),
                MDButton(
                    MDButtonText(text="Simpan"),
                    style="filled",
                    on_release=self.simpan_menu_baru
                ),
            )
        )
        self.dialog_menu.open()

    def simpan_menu_baru(self, *args):
        nama = self.input_nama_menu.text.strip()
        harga_str = self.input_harga_menu.text.strip()
        desk = self.input_desk_menu.text.strip()

        if not nama or not harga_str:
            return

        try:
            harga = int(harga_str)
        except ValueError:
            harga = 10000

        if not desk:
            desk = "Menu pilihan spesial."

        # Simpan menu baru ke database
        db.tambah_produk(nama, harga, desk, "tugas2.jpeg")
        self.dialog_menu.dismiss()
        self.muat_daftar_menu()

    def hitung_total(self):
        try:
            menu_screen = self.root.get_screen("menu")
            container = menu_screen.ids.container_menu
            total = 0
            item_count = 0
            for child in container.children:
                if isinstance(child, ProductCard):
                    total += child.harga * child.jumlah
                    item_count += child.jumlah
            
            self.total_item = item_count
            self.total_harga_str = f"[b]Rp {total:,}[/b]"
        except Exception:
            pass

    def checkout_pesanan(self):
        """Membuat pesanan dari isi keranjang lalu menyimpannya ke tabel riwayat."""
        try:
            menu_screen = self.root.get_screen("menu")
            container = menu_screen.ids.container_menu
        except Exception:
            return

        item_terpilih = []
        total = 0
        for child in container.children:
            if isinstance(child, ProductCard) and child.jumlah > 0:
                item_terpilih.append(f"{child.jumlah}x {child.nama}")
                total += child.harga * child.jumlah

        if self.current_user_id == 0:
            MDSnackbar(
                MDSnackbarText(text="Silakan masuk (login) terlebih dahulu!"),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return

        if not item_terpilih:
            MDSnackbar(
                MDSnackbarText(text="Keranjang masih kosong!"),
                y=dp(24),
                pos_hint={"center_x": 0.5},
                size_hint_x=0.5,
            ).open()
            return

        kode_transaksi = "TRX" + str(random.randint(1000, 9999))
        detail_item = ", ".join(item_terpilih)
        tanggal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

        db.tambah_riwayat(self.current_user_id, kode_transaksi, detail_item, total, tanggal)

        # Kosongkan kembali keranjang setelah checkout
        for child in container.children:
            if isinstance(child, ProductCard):
                child.jumlah = 0
        self.hitung_total()

        MDSnackbar(
            MDSnackbarText(text=f"Pesanan {kode_transaksi} berhasil dibuat!"),
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()
        self.root.current = "riwayat"


if __name__ == "__main__":
    PentolApp().run()