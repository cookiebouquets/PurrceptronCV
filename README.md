# PurrceptronCV
PurrceptronCV is a tiny ML project designed to automatically fill a pet's food bowl using computer vision.

## 1. Abstract

An issue busy pet owners might face is refilling their pet's food bowl, especially on days where the owner may be away for an extended period of time for vacation or work trips. In this project, we introduce PurrceptronCV, a **TinyML** project that utilizes a C**onvolutional Neural Network (CNN)** to detect when a pet's food bowl is empty. This model sends its predictions to an **Arduino UNO**, a microcontroller, in order to activate a servo motor connected to a rack and pinion system in order to dispense the food into the bowl. Detection is done via a **Nicla Vision**, a microcontroller with a built-in camera and the capability of running **MicroPython** programs. Considerations have to be made about the amount of parameters for our model, as the nicla vision's onboard memory is limited. We use **TFLite** to compress our model so that it fits within the limitations of the Nicla Vision. The dispenser itself is built with the **GoBilda robotics build system**

## 2. Data Collection and Preprocessing

We needed to collect a ton of data to train our neural network. In order to do this, we recorded a bunch of 10-20 second clips of our food bowl entirely in entwo binary states: "full" and "empty". Then, we wrote a python script (([datagen.py](https://github.com/cookiebouquets/PurrceptronCV/blob/main/data%20processing/datagen.py)) that iterates through a specified video frame by frame and save each frame into a directory called Raws. After that, we split the data set into a 70/20/10 split of Train/Validation/Test sets based on the whether the frame is full or empty [split.py](https://github.com/cookiebouquets/PurrceptronCV/blob/main/data%20processing/split.py). These files are thrn moved into a specific directory called data with subdirectories for the train set, validation set, and test set. This directory structure is required for Keras/Tensorflow.

Before specifying and training our model, we then augment our dataset for generalizability's sake. We randomly jitter the zoom, rotation, brightness, and contrast of the train/validation/test set so that our model can learn the different binary states in various conditions. See [cell 2](https://github.com/cookiebouquets/PurrceptronCV/blob/main/model/catclassifier.ipynb). 

## 3. Model Creation and Compression

In this section, we train our neural network. Our network is a simplified CNN with max pooling interspersed. Each convolutional layer extracts features from the image (texture/color of food present), then downsamples these feature maps using max pooling to prevent overfitting. We then use global average pooling to reduce the size of the tensor. Finally, we use two dense layers with a sigmoid activation function in order to produce probabilities for our binary classification. We make the global average pooling -> dense layer approach rather than a flatten approach because this model has stringent parameter bounds due to the microcontroller's limited RAM. See the diagram below for a visualizaiton of the model:

<p align = "center"><img src="https://github.com/cookiebouquets/PurrceptronCV/blob/main/model/model.png" width="700"></p>

We then use TFLite for its int8 quantization abilities. This allows us to get the model to a shocking 28.3 kb.

## 4. Hardware Programming 

In this section, we demonstrate our MicroPython code that runs on our nicla vision [main.py](https://github.com/cookiebouquets/PurrceptronCV/blob/main/model/main.py). In our setup, we establish a UART serial connection with a baud rate of 9600. In our MicroPython code, we tune our threshold. We only want the servo arm to open when the model is confident that the bowl is empty. Our model makes a prediction, then writes 1 for open and 0 for close over UART. 

## 5. Building the Dispenser

## 6. Demonstration 
