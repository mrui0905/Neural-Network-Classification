# Neural Network Classification

This project contains four neural networks trained for classification.

The texts folder contains models trained to detect whether 20th century writings are from American author Thomas Wolfe. Two models are provided: the first is a simple sequential model and the seocnd is recurrent neural network (RNN). Text is cleaned to account for punctuation and other symbols, tokenized, and embedded based on its location before training. Each epoch's loss is calculated and the model automatically ends training when loss becomes sufficiently low to prevent overtraining.

The musical_keys folder contains a model trained to detect the musical key of a piece given its notes. It utilizes a multi-layer neural network with Keras's Adam Optimizer to train the model. Data is first converted from .midi and then cleaned before it is trained in the model.

The raw_classification folder contains a model trained without using open-souce packages such as Keras or Tensorflow. It implements an elementary multi-layered neural network. It is trained to digit pixels into numerical digits, as well as to classify classical music based on composers. For the musical data, midi files are cleaned and transformed into their numerical note representation before fed into the model.