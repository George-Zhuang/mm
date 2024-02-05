import os
import mmcv
from glob import glob

from mmdet.apis import DetInferencer

# configs
inferencer = DetInferencer(
    model='configs/mm_grounding_dino/grounding_dino_swin-t_finetune_8xb4_50e_cityscapes.py', 
    weights='weights/grounding_dino_swin-t_pretrain_obj365_goldg_grit9m_v3det_20231204_095047-b448804b.pth',
    device='cuda:1')

# # Image-based inference
# img_path = 'data/results_NEC_sim_exp_0/EGAE/HDR/27011193.hdr'
# inferencer(
#     img_path,
#     texts='person . car . truck .',  
#     show=False, 
#     out_dir='work_dirs/vis_data/vis_hdr',
#     )

# Seq-based inference
data_dir = 'data/results_NEC_sim_exp_1'
exp_name = 'results_NEC_sim_exp_1'
methods = os.listdir(data_dir)
for method in methods:
    method_dir = os.path.join(data_dir, method) 
    imgs = glob(os.path.join(method_dir, '*.png'))
    for img in imgs:
        img_name = img.split('/')[-1]
        inferencer(
            img,
            texts='person . car . truck .',  
            show=False,
            pred_score_thr=0.4,
            out_dir=f'work_dirs/vis_data/{exp_name}/detection/{method}',
            )


