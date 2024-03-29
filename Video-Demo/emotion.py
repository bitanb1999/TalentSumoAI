import os
import cv2
import sys

from deepface import DeepFace

models = {}
models['emotion'] = DeepFace.build_model('Emotion')
def get_smile_vector_img(img):
    smile = 0
    emo_dict = DeepFace.analyze(img, actions=['emotion'], models=models, enforce_detection=False)
    if 'emotion' in emo_dict:
        smile = (int(emo_dict['emotion']['happy']))
    else:
        smile = -1
    # assert len(smile_vect)==len(img_arr)
    return smile

def main(fpath, spath):
    smile_vec = []
    i = 0
    cap = cv2.VideoCapture(fpath)
    while True:
        ret, frame = cap.read()
        if ret:
            smile_vec.append(get_smile_vector_img(frame))
        else:
            break
        print(len(smile_vec))

    smile_vec = ','.join([str(i) for i in smile_vec])
    with open(spath + '.txt', 'w+') as g:
        g.write(smile_vec)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])