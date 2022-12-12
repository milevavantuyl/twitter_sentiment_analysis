# Hate Speech Detection with Sentiment Analysis

In this project we evaluate whether sentiment analysis classifiers are able to detect the negative polarity of offensive messages and, thus, if they constitute a good approach to identify hate speech. The project includes three main tasks:

1. <b>Data Exploration and Preprocessing:</b> In this section the following datasets from Kaggle are explored and cleaned:
    - Sentiment140 Dataset: https://www.kaggle.com/datasets/kazanova/sentiment140
    - Hate Speech and Offensive Language Dataset: https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset
<br></br>
2. <b>Sentiment Classification Models:</b> In this section we build and train two models to classify sentiment data into the categories Negative and Positive
    - Naive Bayes
    - LSTM
<br></br>
3. <b>Application of Sentiment Classification Models on Hate Speech Data:</b> In this section we apply the previously trained models on hate speech data to determine if they perform well in identifying a predominant negative sentiment. Additionally, we apply a pretrained model called VADER, which was trained for Hate Speech detection.


## How to run the code

The main code is written within a jupyter notebook. An additional .py file is provided with some helper functions. 
To successfully run the code perform the following steps: 
1. Clone the folder from GitHub. 
2. Navigate to the folder from within your terminal. 
3. Download the [Sentiment140 dataset](https://www.kaggle.com/datasets/kazanova/sentiment140), [Hate Speech and Offensive Language dataset](https://www.kaggle.com/datasets/mrmorj/hate-speech-and-offensive-language-dataset), and 
[glove.twitter.27B embeddings](https://nlp.stanford.edu/projects/glove/). Then store them in a subdirectory titled "data".
4. Create and activate a Conda environemnt with packages including sklearn, tensorflow, vaderSentiment, nltk, pandas, numpy, and matplotlib.
5. Open up an editor including Jupyter Lab or Visual Studio Code that allows for execution of jupyter notebooks. 
6. Run the cells of the notebook sequentially.

## Contents

The project contains one jupyter notebook and one python file 
- <b>HateSpeechAnalysis.ipynb:</b> Main functionality. Contains the data cleaning, the models training and the evaluation, as stated above.
- <b>helper_functions.py:</b> Library including some transversal functions needed along the code.
- <b>SampleIO.mp4:</b> A description of the sample input and output
- <b>Sentiment Analysis On Hate Speech Presentation.pptx:</b> PowerPoint presentation.

The associated presentation is not included in this repository as it was presented on December 8, 2022. 
