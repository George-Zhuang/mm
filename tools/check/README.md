# Check Pose Annotations

## Step 1️⃣: find bad ones from results
First use ```check_res.py``` to check the pose results and mark bad results.
```bash
Usage: python check_res.py --input_dir data/pose --output_dir data/pose_bad
'm' to mark the image as bad
'n' to skip the image
'b' to go back to the previous image
'q' to quit
```

## Step 2️⃣: recover OK ones from bad ones
Recover some OK results from ones that were labeled as 'bad'. This step is to save efforts.
```bash
Usage: python check_bad.py --input_dir data/pose --output_dir data/pose_bad
  'd' to delete the image
  'n' to skip the image
  'r' to recover the deleted image
  'b' to go back to the previous image
  'q' to quit
```

## Step 3️⃣: Repeat 1️⃣ and 2️⃣ until you are satisfied
Based on my experience, twice is OK.

## Step 4️⃣: Add new labels to bad results
Remind that there are generally 21 points on a hand, except for cases that some points are not in the view.
```bash
Usage: python label_points.py --input_dir data/pose_bad --output_dir data/pose_finetune
  'n' to skip the image
  'b' to go back to the previous image
  'q' to quit
```