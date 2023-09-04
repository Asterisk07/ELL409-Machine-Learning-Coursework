# Intro to Machine Learning

This directory contains the code and projects I've created while learning machine learning basics. It serves as a collection of my work during the introductory phase of my machine learning journey.

## Resources

During my learning journey, I used the following resources:

1. **Pytorch and Tensors : Conceptual Introduction**
   - [Link to Resource](https://www.kdnuggets.com/2020/06/fundamentals-pytorch.html)
   - "Tensors are generalizations of 2-dimensional matrices to N-dimensional space."

1. **"Introduction to PyTorch : Microsoft Learn"**
   - [Link to Resource](https://learn.microsoft.com/en-us/training/modules/intro-machine-learning-pytorch/)
   - Explore key PyTorch concepts for building machine learning models, including Tensor usage, dataset management, image recognition with neural networks, model optimization, and inference performance enhancement.

2. **"Important Tensor methods from official docs"**
   - [Link to Resource](https://pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html)
   - Covers some important tensor methods (including maths)
   - [My code (for tensor maths)](./code/a3_tensor_maths.ipynb)
 


2. **"Comprehensive Tensor methods from official docs"**
   - [Link to Resource](https://pytorch.org/docs/stable/torch.html)
   - Discover essential tensor methods and functionalities in PyTorch through the official documentation.
   - Review: Didnt finish it yet, too comprehensive

2. **"Important Tensor methods from official docs"**
   - [Link to Resource](https://pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html)
   - Covers some important tensor methods

3. **Jupyter keyboard shortcuts**
   - [Link to Resource](/code/a0_keyboard_shortcuts.ipynb)
  
These resources played a significant role in shaping my understanding of machine learning. I encourage you to explore them if you're on your own learning journey in this field.

## Requirements

To run the code and projects in this directory, you may need to install specific Python packages and dependencies. You can find a list of these requirements in the "requirements.txt" file provided in this directory. To install the required packages, you can use the following command:

```bash
pip install -r requirements.txt
```

## Choice of Dataset: MNIST vs CIFAR-10
   - In my machine learning journey, I decided to start with the MNIST dataset.
   - MNIST is a well-known dataset of hand-written digits, making it an ideal choice for beginners in machine learning and computer vision.
   - Given that this directory is named "intro," I opted for MNIST as it aligns with the introductory phase of my learning journey.
   - [Link to MNIST Dataset](mention the source or location of the dataset)

   - In my machine learning journey, I had the choice of starting with two popular datasets: MNIST and CIFAR-10.
   - MNIST is a relatively small dataset, with only 70,000 images. This makes it faster and easier to train models on, and it is often used as a benchmark for comparing the performance of different models.The images in MNIST are all grayscale and have a fixed size of 28x28 pixels, which makes it easier to process and analyze the data.The images in MNIST are also well-centered and have little variability in terms of scale and orientation, which can make it easier to build models that generalize well.
   - CIFAR-10 is a more diverse and challenging dataset than MNIST, with 10 classes of natural images (such as airplanes, cars, and animals) and a total of 60,000 images. This makes it more representative of real-world image recognition tasks.The images in CIFAR-10 are also larger (32x32 pixels) and are in color, which can provide more information for models to learn from.
   - I chose to work with MNIST because I am a beginner and would want faster training and testing times at the start.
   - [Link to Dataset](mention the source or location of the dataset)
