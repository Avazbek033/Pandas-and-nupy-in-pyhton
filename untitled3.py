# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PwiYhVG3w45CrvpfwPxu3nPcjLbp9FKf
"""

pip install opencv-python

from google.colab.patches import cv2_imshow
import cv2
rasm=cv2.imread("rasm.jpg")
cv2_imshow(rasm)

oqqora=cv2.cvtColor(rasm,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm1=cv2.imread("rasm1.jpg")
cv2_imshow(rasm1)

oqqora=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm2=cv2.imread("rasm2.jpg")
cv2_imshow(rasm2)

oqqora=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm3=cv2.imread("rasm3.jpg")
cv2_imshow(rasm3)

oqqora=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)

from google.colab.patches import cv2_imshow
import cv2
rasm4=cv2.imread("rasm4.jpg")
cv2_imshow(rasm4)

oqqora=cv2.cvtColor(rasm4,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)