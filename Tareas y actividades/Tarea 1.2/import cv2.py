import cv2
import numpy as np
import collections

class VideoBuffer:
    def __init__(self, size=30):
        self.buffer = collections.deque(maxlen=size)  # Cola con tamaño fijo
        self.size = size

    def generate_frames(self):
        """Genera 30 imágenes aleatorias en escala de grises (256x256)."""
        for _ in range(self.size):
            frame = np.random.randint(0, 256, (256, 256), dtype=np.uint8)  # Imagen aleatoria en blanco y negro
            self.buffer.append(frame)

    def play_video(self):
        """Muestra los frames almacenados en el buffer, avanzando con una tecla."""
        while self.buffer:
            frame = self.buffer.popleft()  # Obtener el siguiente frame
            cv2.imshow("Buffer de Video", frame)
            
            key = cv2.waitKey(0)  # Esperar a que el usuario presione una tecla
            
            if key == ord('q'):  # Salir si presiona 'q'
                print("Cerrando video.")
                break

        cv2.destroyAllWindows()  


# 🔥 Simulación del buffer de vídeo
buffer = VideoBuffer(size=30)
buffer.generate_frames()
buffer.play_video()