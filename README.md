# Objective
    

# Information  Gathering
  The collection of phishing URLs was gathered from PhishTank, an open-source tool. This site offers a collection of phishing URLs that are updated hourly and come in several formats, including csv and json. https://www.phishtank.com/developer_info.php is the link to download the data. To train, 5000 randomly selected phishing URLs are gathered from this dataset.

 The authentic URLs can be obtained from the University of New Brunswick's publicly available datasets at https://www.unb.ca/cic/datasets/url-2016.html. A variety of benign, spam, phishing, malware, and defacement URLs are included in this dataset. The benign url dataset is taken into consideration for this study out of all of these types. To train the ML models, 5000 randomly selected valid URLs are gathered from this dataset.

The datasets listed above have been uploaded to this repository's 'DataFiles' folder.

# Extraction Features
  The features in the category shown below were taken from the URL data:

Address Bar-based Functionalities
          Nine traits are extracted in this category.

Features based on Domains
          Four features have been retrieved in this category.
Features based on Javascript and HTML
          Four features have been retrieved in this category.
The URL Feature Extraction contains information on these features.ipynb.Open In Colab

Thus, a total of 17 features have been retrieved from the 10,000 URL dataset and are kept in the DataFiles folder's '5.urldata.csv' file.
The features are taken from the Phishing Websites dataset at https://archive.ics.uci.edu/ml.
# Models Used
The data is split into 80-20, or 8000 training samples and 2000 testing samples, prior to beginning the ML model training. This is obviously a supervised machine learning task based on the dataset. Classification and regression are the two main categories of supervised machine learning issues.

Since the input URL is categorized as either legitimate (0) or phishing (1), this data set falls under the classification difficulty category. The following supervised machine learning models (classification) were taken into consideration for this project's dataset training:


Random Forest Decision Tree Multilayer Perceptrons
XGBoost Autoencoder Support Vector Machines for Neural Networks
The test dataset is used to evaluate each model once it has been trained on the dataset. Phishing mentions the intricate details of the models and their training.
  
