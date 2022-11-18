import cv2

captura = cv2.VideoCapture(0)

# Guardar-grabar video
# nombre del video - code de video - numero de imagenes por segundo - tamaño de la imagen
salida = cv2.VideoWriter('videoSalida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))


# mientras la camara esté activa
while(captura.isOpened()):
    # lee imagen por imagen
    # ret es un valor boolenano (true = hay imagen / false = no hay imagen)
    ret, image = captura.read()
    if ret == True : 
        # si hay imagen las muestra una por una
        cv2.imshow('video', image)
        # guarda la imagen
        salida.write(image)
        # si se presiona la letra "s" se termina el bucle
        if cv2.waitKey(30) & 0xFF == ord('s'):
            break
    else:
        break


# finaliza el video
captura.release()
salida.release()
# cierra todas la ventanas
cv2.destroyAllWindows()