import cv2

cv2.namedWindow('Detected_Edges [Clr]')
#========== Canny Control parameters ====================
# 2a. kernel parametr for Sobel Edge Detector
kernel_size = 3
max_lowThreshold = 100
ratio = 2

# ===========Global containers=======================
gray = 0
frame_global = 0
detected_edges_clr = 0

def CannyThreshold(val):

    low_threshold = val
    # 2. Apply canny edge detection on grayscale
    detected_edges = cv2.Canny(gray, low_threshold, low_threshold*ratio, kernel_size)

    global detected_edges_clr
    # 3. Displaying the color regions detected by Canny
    mask = detected_edges != 0
    detected_edges_clr = frame_global * (mask[:,:,None].astype(frame_global.dtype))
    cv2.imshow('Detected_Edges [Clr]', detected_edges_clr)

def Segment_Edges(frame):

  global gray,frame_global
  frame_global = frame
  # 1. Converting frame to grayscale
  gray = cv2.cvtColor(frame_global, cv2.COLOR_BGR2GRAY)
  cv2.createTrackbar('Min Threshold:', 'Detected_Edges [Clr]' , 100, max_lowThreshold, CannyThreshold)
  CannyThreshold(100)
  edges = detected_edges_clr
  return edges

import os

def main():
    cap = cv2.VideoCapture(0)
    
    while(1):
        ret, img = cap.read()
        if not ret:
            print("vid Not found")
            break
        else:
            print("### Vid Found ###")

        minArea=500
        waitTime=10
        Segment_Edges(img)
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   TESTING   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        cv2.imshow("Frame",img)
        if cv2.waitKey(10) & 0xFF == ord('x') :
            break

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   TESTING   <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


if __name__ == '__main__':
	main()