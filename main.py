import cv2
import numpy as np
import datetime



def crop_photo(image, time):
    crop = image[10:1000, 10:1000]

    cv2.imshow('image.{0}.jpg'.format(time), crop)
    cv2.imwrite('image.{0}.jpg'.format(time), crop)
    cv2.waitKey(0)


def rotate_photo(image, time):
    degrees = int(input('На сколько градусов развернуть фото: '))

    (h, w) = image.shape[:2]
    center = (w / 2, h / 2)

    prepObj = cv2.getRotationMatrix2D(center, degrees, 1.0)

    rotated = cv2.warpAffine(image, prepObj, (w, h))

    cv2.imshow('image.{0}.jpg'.format(time), rotated)
    cv2.imwrite('image.{0}.jpg'.format(time), rotated)
    cv2.waitKey(0)


def change_scale(image, time):
    wide = int(input('Введите масштаб:  '))

    f = float(wide) / image.shape[1]

    new_size = (wide, int(image.shape[0] * f))

    res = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

    cv2.imshow('image.{0}.jpg'.format(time), res)
    cv2.imwrite('image.{0}.jpg'.format(time), res)
    cv2.waitKey(0)


def flipped_photo(image, time):
    flipped = cv2.flip(image, 1)

    cv2.imshow('image.{0}.jpg'.format(time), flipped)
    cv2.imwrite('image.{0}.jpg'.format(time), flipped)
    cv2.waitKey(0)


def blur_photo(image, time):
    blurred_img = cv2.GaussianBlur(image, ksize=(11, 11), sigmaX=0, sigmaY=0)

    cv2.imshow('image.{0}.jpg'.format(time), blurred_img)
    cv2.imwrite('image.{0}.jpg'.format(time), blurred_img)
    cv2.waitKey(0)


def sharpening(image, time):
    matrix = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]

    sharp_filter = np.array(matrix)

    sharpen_img = cv2.filter2D(image, ddepth=-1, kernel=sharp_filter)
    cv2.imshow('image.{0}.jpg'.format(time), sharpen_img)
    cv2.imwrite('image.{0}.jpg'.format(time), sharpen_img)
    cv2.waitKey(0)


input_photo = input('Введите имя файла: ')

today = datetime.date.today()
photo = cv2.imread(input_photo)
choice_of_actions = int(input(
    'Выберете действие: 1 - обрезать фото; 2 - повернуть фото; 3 - изменить масштаб; 4 - отзеркаливание; 5 - размытие; 6 - увеличение резкости; 0 - выйти из меню.\n'))

if choice_of_actions == 1:
    crop_photo(photo, today)

elif choice_of_actions == 2:
    rotate_photo(photo, today)

elif choice_of_actions == 3:
    change_scale(photo, today)

elif choice_of_actions == 4:
    flipped_photo(photo, today)

elif choice_of_actions == 5:
    blur_photo(photo, today)

elif choice_of_actions == 6:
    sharpening(photo, today)

else:
    print('Действие не найдено')


