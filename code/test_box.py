import cv2
import pandas as pd
import os
import math


save_folder = './test/'
label_file = './data/train.csv'
img_path = './images/'
df = pd.read_csv(label_file,header = 0)

df = df.values
for i in range(20):
    (filename,image_width,image_height,class_,x1,y1,x2,y2) = df[i,:]
    
    filepath = os.path.join(img_path,filename)

    img = cv2.imread(filepath) 

    img_reg = cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 4)
    img_reg = cv2.putText(img_reg, class_, (x1,y1), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 1)
#    cv2.imwrite('./test/{}.png'.format(i),img_reg) 
    cv2.imwrite('./test/' + class_ + '_'+str(i) + '.png',img_reg)