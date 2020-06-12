from PIL import Image
import numpy

#This function imports image and turns it into grayscale
#The user can choose if they want a lower resolution
def image_grayscale(image):
    #Converts it into grayscale
    gray_img = numpy.array(Image.open('saturn.png', 'r').convert('L'))

    #We might now want a 3#2 bit resolution for the image
    print('Would you like to chage the grayscale resolution of the picture? (y or n)')
    res = input()

    if res == 'y':
        print('Please type the resolution. (16, 8, 2)')
        res_value = input()
        scalar = (int(res_value) - 1) / int(gray_img.max())

        #This normalizes the image so we can scale it by the desired resolution
        down_img = gray_img * scalar

        #We have to put it back in the range [0..255]
        second_scalar = 255 / int(down_img.max())
        scaled_img = down_img * second_scalar

        return scaled_img

    else:
        return gray_img

#This funtion will allow us to view the new array as an image
def view_Image(pix_vals):
    new_image = Image.fromarray(pix_vals)
    new_image.show()

#we will now encrypt the text in the image.
def encrypt_text(img_vals, text_msg):
    #The size of the file will be 32 bits so the limit will be 2^32
    #take the input text and turn it into binary
    bin_msg = ''.join(map(bin, bytearray(text_msg, 'utf8')))

    #Reshape the image so we have just one column with of all the numbers
    #represented as bits
    img_shape = img_vals.shape
    img_vals = img_vals.ravel()
    bin_img = []

    #We only convert the indeces that will be used for the message
    for i in range(32 + len(bin_msg) - len(text_msg)):
        bin_img.append(bin(int(img_vals[i])).zfill(9))

    #We need to know when stop reading bits, we know we have 2^32
    bits_read = bin(len(bin_msg) - len(text_msg)).zfill(33).replace('b', '')
    bin_msg = bin_msg.replace('b', '')

    #We will write how many bits we need to read in the image so we can decrypt.
    insert_bits(bits_read, bin_img)

    #check if the file is the string is too big or too small.
    size_file = 32
    if len(bin_msg) > 2 ** (size_file - 1):
        print('The string is too big. Try another one.')
    elif len(bin_msg) + len(bits_read) > img_shape[0]:
        print('The image is too small')

    #Now that we know how many bits we need to read, insert msg in image.
    for i in range(len(bin_msg)):
        temp = bin_img[i + 32]
        bin_img[i + 32] = temp[:-1] + bin_msg[i]
        bin_img[i + 32] = int(bin_img[i + 32].replace('b', ''))

    img_vals[0:len(bin_img)] = bin_img
    img_vals = img_vals.reshape(img_shape)

    #Display image
    view_Image(img_vals)

    return img_vals

def insert_bits(bits_read, bin_img):
    for i in range(len(bits_read)):
        temp = bin_img[i]
        temp = temp[:-1] + bits_read[i]
        bin_img[i] = temp
        bin_img[i] = int(bin_img[i].replace('b', ''))

#This function decrypts the text message.
def decrypt_img(img_vals):
    #Convert img to 1D array so we can read the pixel vals.
    img_vals = img_vals.ravel()

    #Read the first 32 pixels
    read_pix = convert_bin(img_vals[0:32])

    #Check the LSB of each pixel
    lsb_read_bits = pix_to_str(read_pix)
    lsb_read_bits = int(lsb_read_bits, 2)

    #Check the pixels that contain the message.
    text_bin = convert_bin(img_vals[32:32 + lsb_read_bits])
    text_msg = pix_to_str(text_bin)

    binary_int = int(text_msg, 2)
    byte_num = binary_int.bit_length() + 7 // 8

    binary_array = binary_int.to_bytes(byte_num, "big")
    decrypted_text = binary_array.decode()

    print('Your decrypted message is: ', decrypted_text)

#This function converts what we need to binary
def convert_bin(img_vals):
    pixels_bin = []
    for i in range(len(img_vals)):
        pixels_bin.append(bin(int(img_vals[i])).zfill(9))

    return pixels_bin

#This function converts the lsb into a string and then an int.
def pix_to_str(str_bin):
    lsb_read = ''
    for i in range(len(str_bin)):
        lsb_read = lsb_read + str_bin[i][-1]

    return lsb_read
