# evaluate panoramic segmentation with mmseg
# image-level evaluation
# input: segmentation result, label
# output: mIoU
# Usage: python eval_seg.py --img_dir /path/to/your/seg_res --gt_dir /path/to/your/label --exp_name your_exp_name
import os
import argparse
import mmcv
from glob import glob
from mmseg.evaluation import CityscapesMetric

def parse_args():
    parser = argparse.ArgumentParser(description='Evaluate segmentation results')
    parser.add_argument('--img_dir', default='work_dirs/vis_data/results_NEC_sim_exp_1/segmentation', help='input directory')
    parser.add_argument('--gt_dir', default='data/results_NEC_sim_exp_1/EGAE/label', help='ground truth directory')
    parser.add_argument('--method', default='EGAE', help='eval method')
    parser.add_argument('--exp_name', default='results_NEC_sim_exp_1', help='experiment name')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    img_dir = args.img_dir
    gt_dir = args.gt_dir
    exp_name = args.exp_name
    if not os.path.exists(f'work_dirs/vis_data/{exp_name}/eval'):
        os.makedirs(f'work_dirs/vis_data/{exp_name}/eval')
    method_dir = os.path.join(img_dir, args.method)
    imgs = glob(os.path.join(method_dir, '*.png'))
    imgs.sort()
    gt_imgs = glob(os.path.join(gt_dir, '*.npz'))
    gt_imgs.sort()
    assert len(imgs) == len(gt_imgs)
    metric = CityscapesMetric(output_dir=f'work_dirs/vis_data/{exp_name}/eval')
    res_batch = []
    label_batch = []
    for i in range(len(imgs)):
        img = mmcv.imread(imgs[i], flag='unchanged')
        gt_img = mmcv.imread(gt_imgs[i], flag='unchanged')
        res_batch.append(img)
        label_batch.append(gt_img)
    metric.process(res_batch, label_batch)
    result = metric.evaluate(size=len(imgs))
    print(result)

if __name__ == '__main__':
    main()