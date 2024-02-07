# Use OpenCV to check results that are marked as bad
# If the image is OK, it will be deleted
# Usage: python check_bad.py --input_dir data/pose --output_dir data/pose_bad
#   'd' to delete the image
#   'n' to skip the image
#   'r' to recover the deleted image
#   'b' to go back to the previous image
#   'q' to quit

import cv2
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Check bad results')
    parser.add_argument('--input_dir', type=str, default='data/pose_bad',
                        help='Path to image directory')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_dir = args.input_dir
    # prepare input images with png, jpg, etc.
    img_list = []
    for img_name in os.listdir(input_dir):
        if img_name.endswith('.png') or img_name.endswith('.jpg'):
            img_list.append(img_name)
    img_list.sort()

    # check images
    img_id = 0
    remove_list = []
    while img_id < len(img_list):
        img_name = img_list[img_id]
        img_path = os.path.join(input_dir, img_name)
        img = cv2.imread(img_path)
        cv2.imshow('img', img)
        # input:
        #   'd' to delete the image
        #   'n' to skip the image
        #   'b' to go back to the previous image
        #   'q' to quit
        key = cv2.waitKey(0)
        if key == ord('d'):
            remove_list.append(img_name)
        elif key == ord('n'):
            pass
        elif key == ord('r'):
            # remove the image from the list
            try:
                img_list.remove(img_name)
            except:
                print('Error: {} not in the list'.format(img_name))
        elif key == ord('b'):
            img_id -= 2
        elif key == ord('q'):
            break
        img_id += 1
        print('Progress: {}/{}, {}%'.format(img_id, len(img_list), img_id / len(img_list) * 100))
    # remove bad images
    for img_name in remove_list:
        img_path = os.path.join(input_dir, img_name)
        try:
            os.remove(img_path)
        except:
            continue

if __name__ == '__main__':
    main()
