import cv2
import argparse
import time

def sketch(img):
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	negative=255-gray
	img_blur=cv2.GaussianBlur(negative,ksize=(31,31),sigmaX=0,sigmaY=0)
	img_blend=cv2.divide(gray, 255-img_blur, scale=256)
	return img_blend

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='input image')
    parser.add_argument('output', help='pencil sketch image')
    args = parser.parse_args()
    image = cv2.imread(args.input)
    start_time = time.time()
    output = sketch(image)
    end_time = time.time()
    t = end_time-start_time
    print('time: {0}s'.format(t))
    cv2.imwrite(args.output, output)