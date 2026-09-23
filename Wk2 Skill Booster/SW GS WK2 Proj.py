import cv2
import numpy as np

img = cv2.imread('img2.jpg')

# convert to HSV -- makes it much easier to threshold by color than BGR
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


# ---------- RED ----------
# red wraps around both ends of the hue scale, so it needs two ranges
lower_red_1 = np.array([0, 100, 60])
upper_red_1 = np.array([10, 255, 255])
lower_red_2 = np.array([170, 100, 60])
upper_red_2 = np.array([179, 255, 255])

mask_red_1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
mask_red_2 = cv2.inRange(hsv, lower_red_2, upper_red_2)
mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

if cv2.countNonZero(mask_red) > 0:
    isolated_red = cv2.bitwise_and(img, img, mask=mask_red)
    M = cv2.moments(mask_red)

    #cx = M['m10'] / M['m00']
    #cy = M['m01'] / M['m00']
    #print("red: center=(" + str(round(cx, 1)) + ", " + str(round(cy, 1)) + ")")

    cv2.imshow('red', isolated_red)
    cv2.waitKey(0)


# ---------- GREEN ----------
lower_green = np.array([35, 60, 60])
upper_green = np.array([85, 255, 255])

mask_green = cv2.inRange(hsv, lower_green, upper_green)

if cv2.countNonZero(mask_green) > 0:
    isolated_green = cv2.bitwise_and(img, img, mask=mask_green)
    M = cv2.moments(mask_green)
    cx = M['m10'] / M['m00']
    cy = M['m01'] / M['m00']
    print("green: center=(" + str(round(cx, 1)) + ", " + str(round(cy, 1)) + ")")
    cv2.imshow('green', isolated_green)
    cv2.waitKey(0)


# ---------- BLUE ----------
lower_blue = np.array([86, 60, 60])
upper_blue = np.array([130, 255, 255])

mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

if cv2.countNonZero(mask_blue) > 0:
    isolated_blue = cv2.bitwise_and(img, img, mask=mask_blue)
    M = cv2.moments(mask_blue)
    cx = M['m10'] / M['m00']
    cy = M['m01'] / M['m00']
    print("blue: center=(" + str(round(cx, 1)) + ", " + str(round(cy, 1)) + ")")
    cv2.imshow('blue', isolated_blue)
    cv2.waitKey(0)


# ---------- WHITE ----------
lower_white = np.array([0, 0, 200])
upper_white = np.array([179, 40, 255])

mask_white = cv2.inRange(hsv, lower_white, upper_white)

if cv2.countNonZero(mask_white) > 0:
    isolated_white = cv2.bitwise_and(img, img, mask=mask_white)
    M = cv2.moments(mask_white)
    cx = M['m10'] / M['m00']
    cy = M['m01'] / M['m00']
    print("white: center=(" + str(round(cx, 1)) + ", " + str(round(cy, 1)) + ")")
    cv2.imshow('white', isolated_white)
    cv2.waitKey(0)


# ---------- BLACK ----------
lower_black = np.array([0, 0, 0])
upper_black = np.array([179, 255, 40])

mask_black = cv2.inRange(hsv, lower_black, upper_black)

if cv2.countNonZero(mask_black) > 0:
    isolated_black = cv2.bitwise_and(img, img, mask=mask_black)
    M = cv2.moments(mask_black)
    cx = M['m10'] / M['m00']
    cy = M['m01'] / M['m00']
    print("black: center=(" + str(round(cx, 1)) + ", " + str(round(cy, 1)) + ")")
    cv2.imshow('black', isolated_black)
    cv2.waitKey(0)


cv2.destroyAllWindows()