import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import cv2

# Load the dataset
data = pd.read_csv("C:\\Users\\ASUS\\Downloads\\Phishing_Legitimate_full.csv")

# Preprocess the text data
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    return " ".join(tokens)

X = data["Email_text"].apply(preprocess_text)
y = data["label"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = clf.predict(X_test_tfidf)
print("Phishing detection accuracy:", accuracy_score(y_test, y_pred))

# Use OpenCV for image analysis (e.g., logo detection)
img = cv2.imread("C:\\Users\\ASUS\\Downloads\\phishing.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
logo_detected = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
print("Logo detected:", logo_detected)