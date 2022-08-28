import os
import sys
def format(name,spath):


    os.system(f'ffmpeg -i {name}.mp4 {name}.wav')
    os.system(r"C:\Users\piyan\OpenFace\FeatureExtraction.exe -f {}.mp4".format(name))

    os.system(f'python emotion.py {name}.mp4 {spath}')
    os.system(f'python hands.py {name}.mp4 {spath}')