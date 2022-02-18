import numpy as np
import cv2

img = cv2.imread('input/find_waldo.jpeg')

search = False
pt_x, pt_y = None, None


def search_window(event, x, y, flags, param):
    global pt_x, pt_y, search

    if event == cv2.EVENT_LBUTTONDOWN:
        search = True
        pt_x, pt_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if search == True:
            pt_x, pt_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        search = False


while True:

    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.circle(mask, (pt_x, pt_y), 40, 255, -1)
    masked = cv2.bitwise_and(img, img, mask=mask)

    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('Image', search_window)
    cv2.imshow('Image', masked)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()