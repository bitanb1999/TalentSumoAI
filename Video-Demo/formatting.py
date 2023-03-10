import os
import sys
def format(name,spath):


    os.system(f'ffmpeg -i {name}.mp4 {name}.wav')
    os.system(f"C:\Users\piyan\OpenFace\FeatureExtraction.exe -f {name}.mp4")

    os.system(f'python emotion.py {name}.mp4 {spath}')
    os.system(f'python hands.py {name}.mp4 {spath}')