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
    print("something wrong ")


if os.path.exists("apply_transparent") is False:
    os.mkdir('./apply_transparent')

for seg, raw in tqdm(zip(seg_list, raw_list)):
    mask = cv2.imread("test_human_images_results/" + seg)
    raw_np = cv2.imread("test_human_images/" + raw)
    print(mask.shape,"dddddddddddddd")
    if raw[-3:] != "gif":

        print(seg)
        mask_inv = cv2.bitwise_not(mask)

        AND_result = cv2.bitwise_and(raw_np, mask)

        alpha_channel = (mask_inv != 255)*1
        result = cv2.add(mask_inv, AND_result)
        

        b_channel, g_channel, r_channel = cv2.split(result)

        result = cv2.merge((b_channel, g_channel, r_channel, alpha_channel[...,0].astype('uint8')*255 ))

        cv2.imwrite("apply_transparent/" + seg, result)

        