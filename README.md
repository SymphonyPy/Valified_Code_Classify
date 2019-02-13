1. Run "python /Image_Disposal/Pic_Crawler.py" to download captchas and classify manually. (It was written long time ago, the website must change a lot, so I doubt if it can work.)

2. Run "python /Image_Disposal/Image_Disposal.py" to divide the captchas into single letters and make them monochrome(yes, I just googled this word hhh). The algorithm (actually, it doesn't deserve being called algorithm) is very simple so that sometimes we get 2 letters in 1 picture, but the rate is acceptable.

3. Run "python /Image_Disposal/Rename.py" to rename. I forget if it is necessary or just because they look nice after renaming.

4. Run "python /Network_training/" + "CNN.py" or "SNN.py" to train your model(s). Trained model(s) will be automatically saved.

5. Run "python /classified/Classified.py" to apply your model on new dataset. I was too lazy to finish it, the code now can only recogonize single letter, just like the pretreated dataset. However, You can use the code in Image_disposal to complete it. I will be really grateful.
