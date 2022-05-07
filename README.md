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

# 4. Test.  

## 4.1 Original output

Run `python custom_u2net_human_seg_test.py`  
One can get segmentation outputs in `test_data/test_human_images_results`  

## 4.2 Only for human  

Output is image which is only for ley you know where is the human not who is.  
(Means output is just black and white.)

What I really need is eliminate backgrounds.  

So go to `./test_data` and   
Run `python apply.py`  
Then the elminated background images will be in `test_data/apply`  

## 4.3 Transparent background.  

Doing 4.2 makes image's backgound to black. (or white)  
So go to `./test_data` and   
Run `python apply_transparent.py`  
Then the tranparented background images will be in `test_data/apply_transparent`  

I used alpha channel to transparency


