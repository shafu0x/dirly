from dirly import img_dirly
from dirly import video_dirly
import cv2
from pathlib import Path
from PIL import Image

IN_DIR = Path('/home/sharif/Documents/Action-Recognition-Gold-Standard/Videos')
OUT_DIR = Path('/home/sharif/Desktop/out')

@video_dirly(IN_DIR, video_to_frames=True)
def to_frames(_f):
    print(_f)
    imgs = []
    cap = cv2.VideoCapture(_f)
    i = 0
    while(cap.isOpened()):
        print(i)
        i += 1
        ret, frame = cap.read()
        if frame is not None: imgs.append(Image.fromarray(frame))
    return imgs

if __name__ == '__main__':
    to_frames()
