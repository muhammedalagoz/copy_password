import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import pyperclip
import time
import platform

class PasswordCopier:
    def __init__(self, root):
        self.root = root
        self.root.title("Kullanıcı Adı ve Şifre Yapıştırıcı")
        self.root.geometry("400x250")
        
        # İşletim sistemine göre kopyala-yapıştır tuşu
        self.modifier_key = 'ctrl' if platform.system() == 'Windows' else 'command'
        
        # Sabit kullanıcı adı ve şifre
        self.username = "muhammed"  # Buraya kullanıcı adınızı yazın
        self.password = "123456"    # Buraya şifrenizi yazın
        
        # Mouse pozisyonunu saklamak için
        self.click_position = None
        
        # Ana frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Pozisyon kaydetme butonu
        ttk.Button(main_frame, text="Şifreyi Yapıştır (3 saniye)", 
                  command=self.save_position).grid(row=0, column=0, pady=10, padx=10)
        
        # Durum mesajı
        self.status_var = tk.StringVar()
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=2, column=0, pady=10)
        
        # Kullanım talimatları
        ttk.Label(main_frame, 
                 text="Kullanım:\n1. 'Şifreyi Yapıştır' butonuna tıklayın\n"
                      "2. kullanıcı adı alanına tıklayın\n"
                      "3. Otomatik yapıştırılır",
                 justify=tk.CENTER).grid(row=3, column=0, pady=10)

    def save_position(self):
        self.status_var.set("kopyalandı")
        self.root.update()
        time.sleep(3)  # 3 saniye bekle
        self.click_position = pyautogui.position()
        self.status_var.set(f"işlem başladı! ({self.click_position.x}, {self.click_position.y})")
        self.auto_paste()

    def auto_paste(self):
        try:
            if self.click_position is None:
                messagebox.showwarning("Uyarı", "Lütfen önce pozisyonu kaydedin!")
                return
                
            # Kullanıcı adını yapıştır
            pyperclip.copy(self.username)
            pyautogui.click(self.click_position)
            time.sleep(0.1)
            pyautogui.hotkey(self.modifier_key, 'v')
            
            # Tab tuşuna bas
            time.sleep(0.1)
            pyautogui.press('tab')
            
            # Şifreyi yapıştır
            time.sleep(0.1)
            pyperclip.copy(self.password)
            pyautogui.hotkey(self.modifier_key, 'v')
            
            # Enter tuşuna bas
            time.sleep(0.1)
            pyautogui.press('enter')
            
            self.status_var.set("Kullanıcı adı ve şifre yapıştırıldı!")
            
        except Exception as e:
            error_msg = str(e)
            if "accessibility" in error_msg.lower():
                messagebox.showerror("Erişim Hatası", 
                    "Erişilebilirlik izni gerekli!\n\n"
                    "Lütfen şu adımları izleyin:\n"
                    "1. Apple menüsü > Sistem Ayarları\n"
                    "2. Gizlilik ve Güvenlik > Erişilebilirlik\n"
                    "3. Terminal/PyCharm'ı ekleyin ve izin verin")
            else:
                messagebox.showerror("Hata", f"Bir hata oluştu: {error_msg}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordCopier(root)
    root.mainloop() 