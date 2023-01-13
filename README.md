# Image-Bordering
Drawing the border in selected area of the image

This code is used to crop and draw an outline onto an object in an image. It starts by specifying the input image and reading and displaying it in a window. The user can then draw a rectangle around the desired object to be cropped. This region is then cropped and the background is removed from the image. 

An outline is then drawn around the object using cv2.findContours() and cv2.drawContours(). This outline is then overlayed onto the original image. This loop runs until the user presses the 'q' key, at which point the program terminates and all windows are closed.

This code is useful for creating a mask of an object in an image, which can then be used for various applications such as object detection and recognition. The code is also useful for creating an outline of an object, which can be used to highlight an object in an image.

The code is written using the OpenCV library, which is a library of programming functions mainly used for real-time computer vision. The code can be easily modified to fit the application needs. For example, the outline thickness can be adjusted by changing the thickness argument in the cv2.drawContours() function. Additionally, the code can be modified to draw a variety of shapes onto an image instead of an outline.
