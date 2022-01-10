# Frame Level Speech Recognition
## IDC 410 Assignment



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/MonitSharma/Machine-Learning/tree/main/Frame_Level_Speech_recognition)

## Question for the Assesment
In this coursework you will take your knowledge of feedforward neural networks and apply it to the task of speech recognition.

You are provided a dataset of audio recordings (utterances) and their phoneme state (subphoneme) labels. The data comes from articles published in the Wall Street Journal (WSJ) that are read aloud and labelled using the original text.


## Dataset
Feature File
[train|dev|test].npy contain a numpy object array of shape [utterances]. Each utterance is a float32 ndarray of shape [time, frequency], where time is the length of the utterance. Frequency dimension is always 40 but time dimension is of variable length.

Label Files
[train|dev]_labels.npy contain a numpy object array of shape [utterances]. Each element in the array is an int32 array of shape [time] and provides the phoneme state label for each frame. There are 138 distinct labels [0-137], one for each subphoneme.





### Check the Google Colab Version for the same I wrote:

- [Frame Level Speech Recognition](https://github.com/MonitSharma/Machine-Learning/blob/main/Frame_Level_Speech_Recoginition_Using_Neural_Networks.ipynb)
- [Frame Level Speech Reco](https://github.com/MonitSharma/Machine-Learning/blob/main/Frame_level_Speech_Recogintion_2.ipynb)
- [Frame Level Speech Recognition ALternative](https://github.com/MonitSharma/Machine-Learning/blob/main/Frame_Level_Speech_Reco4.ipynb)






## Libraries Used

This code requires few libraries:

- [PyTorch] - The ML library
- [Numpy] - Used for basic Matrix multiplication and other
- [DateTime] - Keep in touch with time.
- [Argparser] - To pass the argument from Command line
- [Pandas] - Datasets manipulation



## Installation
Create a Virtual Environment, It'll help in better management of your program and libraries.
```sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
You will see (venv) written in the terminal.

Clone the repository. Install all the requirements to run the program.


```sh
git clone <insert link here>
cd Frame_Level_Speech_Recognition


```
You can downlaoad the dataset from [here](https://www.kaggle.com/c/cmu-11785-deep-learning-hw1-p2/data)

Make a directory in the folder Frame_Level_Speech_Recognition by the name data, and paste the files there.

## Running the Neural Network
Go into the src folder and write this on the terminal
```sh
cd src
python train.py
```
After the model is trained type:

```sh
python test.py
```

