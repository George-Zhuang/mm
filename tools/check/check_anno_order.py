# check the point order of predictions
import json
import cv2
import os

res_path = 'data/pose/1706690545289370.json'
img_path = 'data/pose/1706690545289370.png'

# load data
with open(res_path, 'r') as f:
    res = json.load(f)
    points = res[0]['keypoints']

# write the order of points
img = cv2.imread(img_path)
for i, point in enumerate(points):
    x, y = int(point[0]), int(point[1]) 
    cv2.putText(img, str(i), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
# save image
os.makedirs('output', exist_ok=True)
cv2.imwrite('order.jpg', img)
