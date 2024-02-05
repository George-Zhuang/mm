# transfer image sequences to videos
# Usage: python seq2video.py --input_dir /path/to/your/seq --output_dir /path/to/your/video --fps 30
import os
import argparse
import cv2
from glob import glob

def parse_args():
    parser = argparse.ArgumentParser(description='Convert image sequences to videos')
    parser.add_argument('--input_dir', default='work_dirs/vis_data/results_NEC_sim_exp_1/segmentation', help='input directory')
    parser.add_argument('--output_dir', default='work_dirs/vis_data/results_NEC_sim_exp_1/segmentation', help='output directory')
    parser.add_argument('--fps', type=int, default=30, help='frames per second')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    fps = args.fps
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    methods = os.listdir(input_dir)
    for method in methods:
        method_dir = os.path.join(input_dir, method)
        imgs = glob(os.path.join(method_dir, '*.png'))
        imgs.sort()
        img = cv2.imread(imgs[0])
        height, width, layers = img.shape
        size = (width, height)
        video_name = method + '.avi'
        video_path = os.path.join(output_dir, video_name)
        video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for img in imgs:
            video.write(cv2.imread(img))
        cv2.destroyAllWindows()
        video.release()

if __name__ == '__main__':
    main()