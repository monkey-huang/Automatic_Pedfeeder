import cv2
import os
from keras.models import load_model
import numpy as np

class pretrain_model:
    def __init__(self, model):
        self.model=load_model('my_model_detection.h5')
    def preprocess(self, pet_path):
        
        IMG_SIZE=50
        label=[1,0]
        training_data=[]
        img = cv2.imread(pet_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (IMG_SIZE,IMG_SIZE))
        training_data.append([np.array([img]),np.array(label)])
        
        pre_x_data = np.array([i[0] for i in training_data]).reshape(-1, IMG_SIZE, IMG_SIZE,1)
        return pre_x_data
    def my_predict(self, PET_PATH):
        
        x_data = self.preprocess(PET_PATH)
        x = self.model.predict(x_data)
        return x
        