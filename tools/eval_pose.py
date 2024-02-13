# An example to evaluate the pose estimation results.
import json
import numpy as np

from mmpose.evaluation import AUC

res_path = 'data/pose/1706690543648969.json'
gt_path = 'data/pose/1706690543794125.json'

# initialize AUC metric
auc_metric = AUC()

# pre-process data
data_sample = {'pred_instances':{},
               'gt_instances':{},}

with open(res_path, 'r') as f:
    res = json.load(f)
data_sample['pred_instances']['keypoints'] = np.array([res[0]['keypoints']])

with open(gt_path, 'r') as f:
    gt = json.load(f)
data_sample['gt_instances']['keypoints'] = np.array([gt[0]['keypoints']])
data_sample['gt_instances']['keypoints_visible'] = np.ones((1, 21, 1))

data_samples = [data_sample]
# process data and evaluate
auc_metric.process(data_batch=None,
                   data_samples=data_samples)
metrics = auc_metric.compute_metrics(auc_metric.results)
print(metrics)

