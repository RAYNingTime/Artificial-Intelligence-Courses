# This file is going to contain all the question that Andrej Karpathy asked regarding Nearest Neighbor Classifier and my personal answers on them.

### How does the speed depend on the size of the training data?
- As larger training data set is, as longer it'll take to predict the image. 
- This fact occures beacuse for Nearest Neighbor method we are required to compare each of the test images to **every single training image**, 
so it will become linearly slower as we add images.
