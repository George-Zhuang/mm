# open an image and read corresponding points to test drag_point function
# Steps:
    # 1. Open an image
    # 2. Read corresponding points
    # 3. Click on a point
    # 4. Click on a new position
    # 5. Move the point to the new position
    # 6. Repeat 3-5
    # 7. Close the image and save the dragged points

import cv2
import os
import json
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Test drag points')
    parser.add_argument('--input_path', type=str, default='data/pose/1706690543648969.png',
                        help='Path to image directory')
    parser.add_argument('--anno_path', type=str, default='data/pose/1706690543648969.json',
                        help='Path to anno directory')
    parser.add_argument('--output_path', type=str, default='data/pose_finetune/1706690543648969.json',
                        help='Path to anno directory')
    args = parser.parse_args()
    return args

def drag_point(event, x, y, flags, param):
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
    input_path = args.input_path
    anno_path = args.anno_path
    output_path = args.output_path
    # read image
    img = cv2.imread(input_path)
    # read points
    with open(anno_path, 'r') as f:
        anno = json.load(f)
    points = anno[0]['keypoints']
    # prepare window
    cv2.namedWindow('img')
    cv2.setMouseCallback('img', drag_point)
    dragging = False
    drag_id = -1
    # show image
    while True:
        img_show = img.copy()
        for point in points:
            x, y = int(point[0]), int(point[1])
            cv2.circle(img_show, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('img', img_show)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    # save points
    anno['keypoints'] = points
    with open(output_path, 'w') as f:
        json.dump(anno, f)

if __name__ == '__main__':
    main()



