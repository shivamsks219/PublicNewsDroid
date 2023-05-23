import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentiments = SentimentIntensityAnalyzer()
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os

def check(comment):
    sentiment_dict = sentiments.polarity_scores(comment)
    #print(sentiment_dict['compound'])
    if sentiment_dict['compound'] >= 0.05 :
        return ("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        return ("Negative")
    else :
        return ("Neutral")

def checkimg(p):
    print("test")
    path = 'static\\'
    filename = str(p)
    imgloc = path + filename
    xmlloc = r"D:\DjangoProjects\publicNews\app\haarcascade_frontalface_default.xml"

    img=cv2.imread(imgloc)

    predictions=DeepFace.analyze(img, actions = ['emotion'])
    print(predictions)
    type(predictions)
    faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
        break

    font=cv2.FONT_HERSHEY_SIMPLEX

    imageSentiment = predictions[0]['dominant_emotion']

    sentiment = {'angry' : -1 , 'disgust': -1 , 'fear': -1 , 'sad': -1 , 'neutral' : 0 , 'surprise': 1 , 'happy': 1 }


    if(sentiment[imageSentiment] == -1):
         imageSentiment='Negative'
    elif(sentiment[imageSentiment] == 1):
         imageSentiment='Positive'
    else:
         imageSentiment= 'Neutral'
    
    
    cv2.putText(img, imageSentiment,(0,25),font,1,(0,0,255),3)


    cv2.imshow('img' , img)
    output_dir = "static"
    cv2.imwrite(os.path.join(output_dir, filename+"Result.jpg"), img)
    cv2.destroyAllWindows()
    return imageSentiment