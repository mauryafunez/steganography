# steganography
Encrypts a text message in an image and decrypts it.

##Files

###steganography.py
This is the main file that runs all the functions in functions.py. The first step is to read the image and change it to grayscale so that it is easier to deal with. Then, we encrypt the desired text into the image. After it gets encrypted, the function to decrypt it gets called to show the user what they wrote into the image.

###functions.py
There are three main functions in the file. image_grayscale() receives and input image such at saturn.png. It makes sure to convert it to an grayscale image and determines the resolution. An RBG image is a consists of three 2D arrays (Red, Blue, Green). To convert it to grayscale, a mean is taken based on an equation so that we can have only one 2D array with the intensities. The intensity simply is how brigth the pixel is, and the value lies between 0 and 255.

Each value in each range is represented by bits. The user has the option to choose the resolution of the intensity. This is important because the less amount of bits each value is represented by, the more evident a change in the image becomes. This functionality still does not work as expected, so there is still room for improvement. 

The second function, encrypt_text(), encrypts a message in the image. The most common approach in steganography is to change the first bit of each pixel because it produces the least amount of change in intesity. Thus, the function sets a limit to how many bits we can write into the image. In our case, it is 2^32. To know how many bits our text message consists of, the function writes the amount in the first 32 pixels and writes the message in the following pixels. 

The second function, decrypt_text(), decrypts the text that the user encrypted. It first reads the first 32 pixels to know how many pixels it has to read to get the full message. The function can't decode spaces just yet, and it outputs an extra amount of spaces at the beginning of the text. Therefore, there is still room for improvement. 
