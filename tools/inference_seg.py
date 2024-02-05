import os
import mmcv
from glob import glob

from mmseg.apis import inference_model, init_model, show_result_pyplot


# configs
config_file = 'configs/segformer/segformer_mit-b5_8xb1-160k_cityscapes-1024x1024.py'
checkpoint_file = './weights/segformer_mit-b5_8x1_1024x1024_160k_cityscapes_20211206_072934-87a052ec.pth'
model = init_model(config_file, checkpoint_file, device='cuda:0')

# Image-based inference
# seq
data_dir = 'data/results_NEC_sim_exp_1'
exp_name = 'results_NEC_sim_exp_1'
methods = os.listdir(data_dir)
for method in methods:
    method_dir = os.path.join(data_dir, method) 
    imgs = glob(os.path.join(method_dir, '*.png'))
    for img in imgs:
        img_name = img.split('/')[-1]
        result = inference_model(model, img)
        show_result_pyplot(model, img, result, show=False, out_file=f'work_dirs/vis_data/{exp_name}/segmentation/{method}/{img_name}', opacity=0.5, with_labels=False)


