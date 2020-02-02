#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import numpy as np
from PIL import Image


def main():
    SRC_DIR = 'photo'

    if not os.path.isdir(SRC_DIR):
        print('No such directory exists')
        exit()

    images = [files for files in os.listdir(SRC_DIR) if os.path.isfile(os.path.join(SRC_DIR, files))]

    print(len(images))

    imagenp = np.zeros(len(images)*200*200*3).reshape(len(images),200,200,3)

    for index, image in enumerate(images):
        try:
            print('Resizing '+str(image)+' ...')

            imagePIL = Image.open(SRC_DIR+'\\'+image)
            imagePIL = imagePIL.resize((200,200))
            imagenp[index] = np.array(imagePIL)
        
        except Exception as e:
            print(e)

    print('Done!')


if __name__ == '__main__':
    main()



