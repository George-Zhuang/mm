# finetune annotated keypoints using opencv
# Function:
#   1. add new key points
#   2. (not completed) drag existing key points to a new position with mouse

import cv2
import os
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Finetune annotated keypoints')
    parser.add_argument('--input_dir', type=str, default='data/pose_bad',
                        help='Path to image directory')
    parser.add_argument('--anno_dir', type=str, default='data/pose',
                        help='Path to anno directory')
    parser.add_argument('--output_dir', type=str, default='data/pose_finetune',
                        help='Path to output directory')
    args = parser.parse_args()
    return args

def drag_point(event, x, y):
    global points, dragging, drag_id
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, point in enumerate(points):
            px, py = point
            if abs(x - px) < 5 and abs(y - py) < 5:
                dragging = True
                drag_id = i
                break
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging:
            points[drag_id] = (x, y)

def main():
    args = parse_args()
    input_dir = args.input_dir
    anno_dir = args.anno_dir
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
        anno_path = os.path.join(anno_dir, img_name.replace('.png', '.json'))
        output_path = os.path.join(output_dir, img_name)
        img = cv2.imread(img_path)
        with open(anno_path, 'r') as f:
            anno = json.load(f)
        for point in anno[0]['keypoints']:
            x, y = int(point[0]), int(point[1])
            cv2.circle(img, (x, y), 5, (255, 0, 0), -1)
            # cv2.putText(img, key, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 4)
        cv2.imshow('img', img)
        # input:
        #   'm' to mark the image as bad
        #   'n' to skip the image
        #   'b' to go back to the previous image
        #   'q' to quit
        key = cv2.waitKey(0)
        if key == ord('n'):
            pass
        elif key == ord('b'):
            img_id -= 2
        elif key == ord('q'):
            break
        img_id += 1
        print('Progress: {}/{}, {}%'.format(img_id, len(img_list), img_id / len(img_list) * 100))

if __name__ == '__main__':
    main()
