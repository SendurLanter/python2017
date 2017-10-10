import sys
from PIL import Image

def argument_parser(argv):
    """ 
    Description: This function will parse the argument passed from the terminal.

    TODO: You have to parse the argument and perform the corresponding operation.

    Args:
        argv: input argument passed from the terminal
    """

    ########## Write your code in below ##########
    if sys.argv[3]=='HPF':
        save_image(list_to_image(high_pass_filter(image_to_list(read_image(sys.argv[1])),read_image(sys.argv[1]),int(sys.argv[4])),read_image(sys.argv[1])),sys.argv[2])
    elif sys.argv[3] == 'LPF':
        save_image(list_to_image(low_pass_filter(image_to_list(read_image(sys.argv[1])),read_image(sys.argv[1]),int(sys.argv[4])),read_image(sys.argv[1])),sys.argv[2])
    elif sys.argv[3]=='BPF':
        save_image(list_to_image(band_pass_filter(image_to_list(read_image(sys.argv[1])),read_image(sys.argv[1]),int(sys.argv[4]),int(sys.argv[5])),read_image(sys.argv[1])),sys.argv[2])
    else:
        print 'erro'

def read_image(filename):
    """ 
    Description: This function will read the image according to the filename 
        and return the image.

    TODO: You have to read the image according to the filename and return 
        the image.

    Args:
        filename: file name of the image
        img: the image
    """

    ########## Write your code in below ##########
    img = Image.open(filename)

    return img

def image_to_list(img):
    """
    Description: This function will transform an image to a high dimensional list.

    TODO: You have to transform the given image and return the result.

    Args:
        img: an input image 
        result: high dimensional list
    """

    ########## Write your code in below ##########
    
    result=[]
    for i in  range(img.size[0]):
        for j in range(img.size[1]):
            result.append(list(img.getpixel((i,j))))

    return result


def high_pass_filter(result,img, threshold):
    """
    Description: This function acts as a high pass filter 
        according to the given threshold and apply the filter to the image.
    
    TODO: You have to apply a high pass filter to the image according to the 
        given threshold and return the processed result.

    Args:
        img: an input image (high dimensional list)
        threshold: a threshold for a high pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in  range(img.size[0]):
        for j in range(img.size[1]):
            if img.getpixel((i,j))[0]<threshold:
                result[i*img.size[0]+j][0]=0
            if img.getpixel((i,j))[1]<threshold:
                result[i*img.size[0]+j][1]=0
            if img.getpixel((i,j))[2]<threshold:
                result[i*img.size[0]+j][2]=0

    return result


def band_pass_filter(result,img, low_threshold, high_threshold):
    """
    Description: This function acts as a band pass filter 
        according to the two given thresholds and apply the filter to the image.
    
    TODO: You have to apply a band pass filter to the image according to the two
        given thresholds and return the processed result.

    Args:
        img: an input image (high dimensional list)
        low_threshold: low threshold for a band pass filter
        high_threshold: high threshold for a band pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in  range(img.size[0]):
        for j in range(img.size[1]):
            if (img.getpixel((i,j)))[0]<low_threshold or (img.getpixel((i,j)))[0]>high_threshold:
                result[i*img.size[0]+j][0]=0
            if (img.getpixel((i,j)))[1]<low_threshold or (img.getpixel((i,j)))[1]>high_threshold:
                result[i*img.size[0]+j][1]=0
            if (img.getpixel((i,j)))[2]<low_threshold or (img.getpixel((i,j)))[2]>high_threshold:
                result[i*img.size[0]+j][2]=0


    return result


def low_pass_filter(result,img, threshold):
    """
    Description: This function acts as a low pass filter 
        according to the given threshold and apply the filter to the image.
    
    TODO: You have to apply a low pass filter to the image according to the 
        given threshold and return the processed result.

    Args:
        img: an input image (high dimensional list)
        threshold: a threshold for a low pass filter
        result: the result (processed high dimensional list)
    """

    ########## Write your code in below ##########
    for i in  range(img.size[0]):
        for j in range(img.size[1]):
            if (img.getpixel((i,j)))[0]>threshold:
                result[i*img.size[0]+j][0]=0
            if (img.getpixel((i,j)))[1]>threshold:
                result[i*img.size[0]+j][1]=0
            if (img.getpixel((i,j)))[2]>threshold:
                result[i*img.size[0]+j][2]=0

    return result


def list_to_image(img_list,imgr):
    """
    Description: This function will transform the high dimensional list to an image.

    TODO: You have to transform the given list and return the result.

    Args:
        img_list: a high dimensional list
        img: an image
    """

    ########## Write your code in below ##########
    img =Image.new("RGB",(imgr.size[0],imgr.size[1]))
    for i in  range(imgr.size[0]):
        for j in range(imgr.size[1]):
            img.putpixel([i,j],(img_list[i*imgr.size[1]+j][0],img_list[i*imgr.size[1]+j][1],img_list[i*imgr.size[1]+j][2]))

    return img


def save_image(img, filename):
    """ 
    Description: This function will save the image as filename.

    TODO: You have to save the image according to the given filename.

    Args:
        img: the image
        filename: file name of the image
    """

    ########## Write your code in below ##########
    img.save(filename)

if __name__ == '__main__':
	argument_parser(sys.argv)