import os
import yt_dlp

# Foydalanuvchidan video havolasini olish
havola = input("YouTube video havolasini kiriting: ").strip()

# Videoni saqlash joyi (C:\videolar)
saqlash_joyi = "C:\\videolar"

# Agar saqlash papkasi mavjud bo'lmasa, uni yaratamiz
if not os.path.exists(saqlash_joyi):
    os.makedirs(saqlash_joyi)

# Yuklab olish sozlamalari
ydl_opts = {
    'outtmpl': os.path.join(saqlash_joyi, '%(title)s.%(ext)s'),  # Fayl nomi va joylashuvi
    'format': '18',  # 360p format (MP4)
}

# Yuklab olish jarayoni
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("\n⏳ Yuklab olish boshlandi...")
        ydl.download([havola])  # Havolani yuklab olish
    print(f"✅ Yuklab olish yakunlandi! Video shu joyda saqlandi: {saqlash_joyi}")
except yt_dlp.utils.DownloadError as xato:
    print(f"❌ Yuklab olishda xato yuz berdi: {xato}")
except Exception as xato:
    print(f"❌ Kutilmagan xato yuz berdi: {xato}")
