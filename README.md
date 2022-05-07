## human iamge segmenatation by N2Net  

Origianl repo is [here](https://github.com/xuebinqin/U-2-Net)  


# 1. Trained model  

First download trained model(weights) from original repository.  
Then move to `./saved_models/u2net_human_seg/`  

# 2. Setting images.  

Put images to be segmented in folder `test_data/test_human_images`  

# 3. Preprocessing.  

Beacause I used this model with crawled data, some of them are .html or .gif and rarely there are images with none.  
So by running custom_apply.py.  

