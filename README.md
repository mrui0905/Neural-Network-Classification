# Number-Detection

This project initally was focused on creating a neural network to detect handwritten numbers. Using the dataset from MNIST, recognition.ipynb contains a two-layered neural network 
which accurately determines the number (0-9) from 784 given pixels.

To accomplish this, we create implement forward propagation with two activation functions: ReLU (Rectified linear unit) and Softmax. We then reverse these functions using and update 
our weights and constants using backward propagation. After training over data for a few minutes, the model already returns accuracy of roughly 90%.

After creating this neural network, I was interested in how these program can be used to detect more than numbers. Creating three datasets (2 represent composers and notes of their
works and 1 represents notes and the musical key of a classical piece), we are able to apply this number detection neural network to determine composers or muical key based on the
notes of musical works. When applying these musical datasets to the neural network, our accuracy is lower than with number detection, however this can be largely attributed to
the substantially smaller musical datset (2-3000) values, compared to the MNIST number dataset (42000) values.

While none of the raw data is inlcuded in this Github, the four csv files directly used by the neural network are included as well as the code used to create the three musical csv files.
The original data for the musical datasets are linked in the respective .py files. The MNIST dataset was already available here. (https://www.kaggle.com/datasets/hojjatk/mnist-dataset)


start on 11, https://www.midiworld.com/search/10/?q=pop