from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen

# KV Language (mirip HTML/CSS untuk mengatur UI)
KV = '''
ScreenManager:
    SplashScreen:
    LoginScreen:
    MainScreen:

# --- HALAMAN AWAL (SPLASH SCREEN) ---
<SplashScreen>:
    name: 'splash'
    md_bg_color: 214/255, 206/255, 189/255, 1  # Warna background krem
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: "40dp"
        spacing: "30dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        adaptive_height: True
        
        MDLabel:
            text: "PENTOL MAMA RETA"
            halign: "center"
            font_style: "H4"
            theme_text_color: "Custom"
            text_color: 82/255, 54/255, 34/255, 1
            bold: True
            
        MDLabel:
            text: "SELAMAT DATANG DI PENTOL MAMA RETA"
            halign: "center"
            theme_text_color: "Secondary"
            
        MDRaisedButton:
            text: "Tekan disini"
            pos_hint: {"center_x": .5}
            md_bg_color: 82/255, 54/255, 34/255, 1 # Warna coklat tua
            # Perintah untuk pindah ke halaman login
            on_release: app.root.current = 'login'

# --- HALAMAN LOGIN ---
<LoginScreen>:
    name: 'login'
    md_bg_color: 214/255, 206/255, 189/255, 1
    
    MDBoxLayout:
        orientation: 'vertical'
        padding: "30dp"
        spacing: "20dp"
        pos_hint: {"center_x": .5, "center_y": .6}
        adaptive_height: True
        
        MDLabel:
            text: "Selamat Datang!"
            font_style: "H5"
            bold: True
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            
        MDLabel:
            text: "Masuk untuk menikmati pengalaman pesan lebih mudah."
            theme_text_color: "Custom"
            text_color: 0.8, 0.8, 0.8, 1
            font_size: "14sp"
            
        MDTextField:
            hint_text: "Alamat Email"
            mode: "round"
            fill_color_normal: 1, 1, 1, 1
            
        MDTextField:
            hint_text: "Password"
            password: True
            mode: "round"
            fill_color_normal: 1, 1, 1, 1
            
        MDRaisedButton:
            text: "Masuk Sekarang"
            size_hint_x: 1
            md_bg_color: 211/255, 47/255, 47/255, 1 # Merah
            on_release: app.root.current = 'main'
            
        MDFlatButton:
            text: "Lanjut Via WhatsApp"
            size_hint_x: 1
            md_bg_color: 139/255, 195/255, 74/255, 1 # Hijau
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1

# --- HALAMAN UTAMA (BOTTOM NAVIGATION) ---
<MainScreen>:
    name: 'main'
    
    MDBottomNavigation:
        panel_color: 82/255, 54/255, 34/255, 1 # Coklat tua untuk navbar
        text_color_active: 1, 0.8, 0, 1 # Warna kuning saat menu aktif
        
        MDBottomNavigationItem:
            name: 'nav_home'
            text: 'Home'
            icon: 'home'
            
            MDBoxLayout:
                md_bg_color: 214/255, 206/255, 189/255, 1
                MDLabel:
                    text: 'Halaman Home (Katalog Promo)'
                    halign: 'center'
                    
        MDBottomNavigationItem:
            name: 'nav_menu'
            text: 'Menu'
            icon: 'format-list-bulleted'
            
            MDBoxLayout:
                md_bg_color: 214/255, 206/255, 189/255, 1
                MDLabel:
                    text: 'Halaman Menu & Keranjang'
                    halign: 'center'
                    
        MDBottomNavigationItem:
            name: 'nav_profile'
            text: 'Profil'
            icon: 'account'
            
            MDBoxLayout:
                md_bg_color: 214/255, 206/255, 189/255, 1
                MDLabel:
                    text: 'Halaman Profil Pengguna'
                    halign: 'center'
'''

# --- KELAS LAYAR ---
class SplashScreen(MDScreen):
    pass

class LoginScreen(MDScreen):
    pass

class MainScreen(MDScreen):
    pass

# --- KELAS UTAMA APLIKASI ---
class PentolApp(MDApp):
    def build(self):
        # Mengatur tema utama aplikasi
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Brown"
        
        # Memuat UI dari string KV
        return Builder.load_string(KV)

if __name__ == '__main__':
    PentolApp().run()