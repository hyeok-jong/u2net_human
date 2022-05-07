import os
import numpy as np
import cv2
from tqdm import tqdm



seg_list = os.listdir("test_human_images_results")
seg_list.sort()
raw_list = os.listdir("test_human_images")
raw_list.sort()

cnt = 0
for seg, raw in zip(seg_list, raw_list):
    if seg[:2] == raw[:2]:
        cnt += 1
if cnt != len(seg_list):
    print("something wrong !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

if os.path.exists("apply") is False:
    os.mkdir('./apply')


for seg, raw in tqdm(zip(seg_list, raw_list)):

    mask = cv2.imread("test_human_images_results/" + seg)
    raw_np = cv2.imread("test_human_images/" + raw)




    print(seg)
    mask_inv = cv2.bitwise_not(mask)
    AND_result = cv2.bitwise_and(raw_np, mask)
    result = cv2.add(mask_inv, AND_result)

    cv2.imwrite("apply/" + seg, result)


