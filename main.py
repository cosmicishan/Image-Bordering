import cv2
from rembg import remove

def crop():

    """ A. Speicifying Input Image"""

    image_path = 'TEST IMAGES/4' \
                 '.jpg'

    """ B. Read and Display Image"""

    input_image = cv2.imread(image_path)

    """ C. Drawing Rectangle"""

    cv2.namedWindow("Application", cv2.WINDOW_NORMAL)

    cropped = cv2.selectROI("Application", input_image)

    """ D. Cropping the Selected Region"""

    cropped_image = input_image[int(cropped[1]):int(cropped[1]+cropped[3]), int(cropped[0]):int(cropped[0]+cropped[2])]

    """E. Removing the Background of Image"""

    no_bg = remove(cropped_image)

    cv2.imwrite('No_bg.jpg', no_bg)

    """ F. Drawing an outline over an object since it doesn't have any background, G. Overlay the object outline to original image
    
    n this example, we find the contours of each blob using cv2.findContours() then draw the outline onto a mask using cv2.drawContours(). 
    In your case, instead of drawing it onto a mask, you can draw it onto your desired image.
    
    Source: https://stackoverflow.com/questions/58530261/how-to-create-an-outline-with-controllable-thickness-from-a-mask-segmentation
    """

    image = cv2.imread('No_bg.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    h, w = image.shape[:2]

    top, left = (cropped[1], cropped[0])

    cnts = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(input_image[top:top + h, left:left + w], [c], -2, (36, 255, 12), thickness=5)

    cv2.namedWindow("Application", cv2.WINDOW_NORMAL)
    cv2.imshow('Application', input_image)

    """ H, I. It will return false if user press Q so the loop will break,
              else it will return True which will call the function again and ask for another outline.
    """


    if cv2.waitKey() == ord('q'):
        return False

    elif cv2.waitKey() == ord('c'):
        return True


while True:

    """Run the loop until press q."""

    run = crop()

    if not run:

        cv2.destroyAllWindows()
        break


