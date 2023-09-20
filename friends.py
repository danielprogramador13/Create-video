import os
import cv2

imagens = "./Imagens"

armaz_imgs = []

for file in os.listdir(imagens):
    name, ext = os.path.splitext(file)
    if ext in [".gif", ".png", ".jpg", ".jpeg"]:
        fileName = imagens + "/" + file 
        print('Nome do arquivo: ', fileName)
        armaz_imgs.append(fileName)

print("Tamanho: ", len(armaz_imgs))

tamanho = len(armaz_imgs)
frame = cv2.imread(armaz_imgs[0])
heigth, width, channels = frame.shape

size = (width, heigth)
print("Tamanho do vídeo: ", size)

animation = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 5, size)

for i in range(0, tamanho):
    frame = cv2.imread(armaz_imgs[i])  # Use 'i' para acessar cada imagem
    animation.write(frame)

animation.release()

print("Vídeo feito")
