import cv2
import numpy as np
import webcolors
import color

# Load the image
img = cv2.imread('D:\\st\\test\\fn.jpg')

# Use the Haar Cascade Classifier to detect eyes in the image
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)

# Define a function to calculate the dominant color of a region
def dominant_color(image):
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Reshape the image to a list of pixels
    pixels = hsv_image.reshape((-1, 3))
    # Calculate the frequency of each color value
    counts = np.unique(pixels, axis=0, return_counts=True)[1]
    # Return the color with the highest frequency
    return pixels[np.argmax(counts)]

def find_color(requested_colour):            
 
        min_colours = {}
        for name, key in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(name)
            rd = (r_c - requested_colour[0]) ** 2
            gd = (g_c - requested_colour[1]) ** 2
            bd = (b_c - requested_colour[2]) ** 2
            min_colours[(rd + gd + bd)] = key
            closest_name = min_colours[min(min_colours.keys())]
        return closest_name

# Iterate over the eyes detected and crop each eye region
def colour(img):
    # Load the image

    # Use the Haar Cascade Classifier to detect eyes in the image
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in eyes:
        # Crop the eye region from the original image
        eye_img = img[y:y+h, x:x+w]
        # Calculate the dominant color of the eye region
        iris_color = dominant_color(eye_img)
        # Display the cropped eye region
        cv2.imshow('Eye', eye_img)
        cv2.waitKey(0)
        
        # Print the iris color in BGR and HSV format
        print('Iris color (BGR): {}'.format(iris_color))
        iris_color_rgb = cv2.cvtColor(np.uint8([[iris_color]]), cv2.COLOR_BGR2RGB)[0][0]
        print('Iris color (RGB): {}'.format(iris_color_rgb))
        print(find_color(iris_color))
        print(find_color(iris_color_rgb))
        ec=(find_color(iris_color_rgb))
        colour=color.switch(ec)
        print(colour)
        return find_color(iris_color_rgb)

        
    # Close all windows
    cv2.destroyAllWindows()
