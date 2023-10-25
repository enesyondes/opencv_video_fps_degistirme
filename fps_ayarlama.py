import cv2

# Giriş video dosyasının adı ve FPS değeri
input_video = 'giris video ismi.mp4'
output_video = 'cikis video ismi.mp4'
target_fps = 5   # Hedef FPS değeri

# Giriş videoyu aç
cap = cv2.VideoCapture(input_video)

# Giriş video özelliklerini al
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_count = int(cap.get(7))
frame_rate = int(cap.get(5))

# Çıkış videoyu oluştur
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, target_fps, (frame_width, frame_height))

# Videoyu oku ve yeniden yaz
while True:
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)

# Videoyu kapat
cap.release()
out.release()

print("Video dönüştürme tamamlandi.")
