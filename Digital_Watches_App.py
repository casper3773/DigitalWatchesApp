# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 00:43:40 2025

@author: muham
"""

import tkinter as tk
from time import strftime

def zaman_guncelle():
    # Şu anki saat ve dakikayı al
    # %H: Saat (24 saat formatında), %M: Dakika, %S: Saniye
    string = strftime('%H:%M:%S %p') 
    
    # Etiketi yeni zamanla güncelle
    lbl.config(text=string)
    
    # Her 1000 milisaniyede (1 saniyede) bir zaman_guncelle fonksiyonunu tekrar çağır
    lbl.after(1000, zaman_guncelle)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Dijital Saat")

# Saat bilgisini gösterecek etiketi oluştur
lbl = tk.Label(
    root, 
    font=('calibri', 60, 'bold'), # Yazı tipi ve boyutu
    background='white',          # Arka plan rengi
    foreground="#90C90A"          # Yazı rengi
)

# Etiketi pencereye yerleştir
lbl.pack(anchor='center', expand=True)

# Saati güncelleme fonksiyonunu başlat
zaman_guncelle()

# Tkinter olay döngüsünü başlat
root.mainloop()