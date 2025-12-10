# PurrceptronCV
PurrceptronCV is a tiny ML project designed to automatically fill a pet's food bowl using computer vision

## 1. Abstract

An issue busy pet owners might face is refilling their pet's food bowl, especially on days where the owner may be away for an extended period of time for vacation or work trips. In this project, we introduce PurrceptronCV, a **TinyML** project that utilizes a C**onvolutional Neural Network (CNN)** to detect when a pet's food bowl is empty. This model sends its predictions to an **Arduino UNO**, a microcontroller, in order to activate a servo motor connected to a rack and pinion system in order to dispense the food into the bowl. Detection is done via a **Nicla Vision**, a microcontroller with a built-in camera and the capability of running **MicroPython** programs. Considerations have to be made about the amount of parameters for our model, as the nicla vision's onboard memory is limited. We use **TFLite** to compress our model so that it fits within the limitations of the Nicla Vision. The dispenser itself is built with the **GoBilda robotics build system**

## 2. Data Collection and Preprocessing

## 3. Model Creation and Compression

## 4. Hardware Programming 

## 5. Building the Dispenser
