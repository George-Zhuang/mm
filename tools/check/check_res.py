# Use OpenCV to check annotation results and mark bad results
# Usage: python check_res.py --input_dir data/pose --output_dir data/pose_bad
#   'm' to mark the image as bad
#   'n' to skip the image
#   'b' to go back to the previous image
#   'q' to quit
# For double check:
#   If bad image is already in output path, it will be skipped

import cv2
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Check annotation results')
    parser.add_argument('--input_dir', type=str, default='data/pose',
                        help='Path to image directory')
    parser.add_argument('--output_dir', type=str, default='data/pose_bad',
                        help='Path to output directory')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    # prepare input images with png, jpg, etc.
    img_list = []
    for img_name in os.listdir(input_dir):
        if img_name.endswith('.png') or img_name.endswith('.jpg'):
            img_list.append(img_name)
    img_list.sort()

    # prepare output
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # check images
    img_id = 0
    while img_id < len(img_list):
        img_name = img_list[img_id]
        img_path = os.path.join(input_dir, img_name)
        bad_img_path = os.path.join(output_dir, img_name)
        if os.path.exists(bad_img_path):
            img_id += 1
            continue
        img = cv2.imread(img_path)
        cv2.imshow('img', img)
        # input:
        #   'm' to mark the image as bad
        #   'n' to skip the image
        #   'b' to go back to the previous image
        #   'q' to quit
        key = cv2.waitKey(0)
        if key == ord('m'):
            cv2.imwrite(bad_img_path, img)
        elif key == ord('n'):
            pass
        elif key == ord('b'):
            img_id -= 2
        elif key == ord('q'):
            break
        else:
            print('Invalid key:', key)
        img_id += 1
        print('Progress: {}/{}, {}%'.format(img_id, len(img_list), img_id / len(img_list) * 100))

if __name__ == '__main__':
    main()
