# label points on images
# Usage: python label_points.py --input_dir data/pose_bad --output_dir data/pose_finetune
#   'n' to skip the image
#   'b' to go back to the previous image
#   'q' to quit

import cv2
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Label points on images')
    parser.add_argument('--input_dir', type=str, default='data/pose_bad',
                        help='Path to image directory')
    parser.add_argument('--output_dir', type=str, default='data/pose_finetune',
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

    # label points
    img_id = 0
    while img_id < len(img_list):
        img_name = img_list[img_id]
        img_path = os.path.join(input_dir, img_name)
        output_path = os.path.join(output_dir, img_name)
        img = cv2.imread(img_path)
        cv2.imshow('img', img)
        # add points using mouse
        points = []
        def add_point(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                points.append((x, y))
                cv2.circle(img, (x, y), 5, (0, 255, 0), -1)
                cv2.imshow('img', img)
        cv2.setMouseCallback('img', add_point)
        key = cv2.waitKey(0)
        if key == ord('n'):
            pass
        elif key == ord('b'):
            img_id -= 2
        elif key == ord('q'):
            break
        else:
            print('Invalid key:', key)
        # save points
        with open(output_path.replace('.png', '.json'), 'w') as f:
            f.write('[\n  {\n    "keypoints":[\n')
            for i, point in enumerate(points):
                x, y = point
                f.write('      [\n        {},\n        {}\n      ],\n'.format(x, y))
            # remove the last comma
            f.seek(f.tell() - 2)
            f.write('\n    ]\n  }\n]')
        img_id += 1
        print('Progress: {}/{}, {}%'.format(img_id, len(img_list), img_id / len(img_list) * 100))

if __name__ == '__main__':
    main()