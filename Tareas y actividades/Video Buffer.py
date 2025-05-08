import cv2
import numpy as np
import collections

class VideoBuffer:
    def __init__(self, buffer_size=30, frame_size=(256, 256)):
        self.buffer = collections.deque(maxlen=buffer_size)  
        self.frame_size = frame_size
        self.fill_buffer()
    
    def fill_buffer(self):
        for _ in range(30):  
            frame = np.random.randint(0, 256, self.frame_size, dtype=np.uint8)
            self.buffer.append(frame)
    
    def play(self):
        for frame in self.buffer:
            cv2.imshow('Video Buffer', frame)
            key = cv2.waitKey(0)  
            if key == 27:  
                break
        cv2.destroyAllWindows()

video_buffer = VideoBuffer()
video_buffer.play()
