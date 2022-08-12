
import nltk

#Activation of text2emotion package

nltk.download('omw-1.4')

import tkinter as tk

#Used for new Window creation

import pandas as pd

# Used for converting dict into Series

import matplotlib.pyplot as mat

#pie plot and graph plot

import text2emotion as te

# emotion analyzer

# Frame is created

frame = tk.Tk()

# Frame title is given 

frame.title("Emotion Analysis")

# Size of the frame

frame.geometry('600x400')

def printOP():

    # text input window opening

    # given text accepantance

    # taking the given input in the tkinter created box

    inp = inputtxt.get(1.0, "end-1c")
    
    # Just  a common statement
    print("The emotions in the text are:")

    # Emotion analysis

    # All the emotions are stored into a dictionary x

    # x contains emotions like Happy,Angry,Surprise,Sad,Fear

    # in terms of floating point numbers less than 1 and more than 0

    # i.e the values are between 0 and 1
    x=te.get_emotion(inp)

    # printing the emotion dictionary

    print(x)

    df=pd.Series(x,index=("Happy","Angry","Surprise","Sad","Fear"))

    # Converting the dictionary into Series

    # This is done user viewing friendly nature

    print(df)

    # Pie plotting of emotions


    mat.pie(df,labels=x.keys(),autopct='%1.1f%%')

    # showing the pie chart

    mat.show()

    # plottting the values on the graph

    mat.plot(df,'o')

    # showing the plotted graph
    mat.show()

# input text window opening
inputtxt=tk.Text(frame,height=15,width=40)

inputtxt.pack()

# print button creation

# command assigning to the button
printButton=tk.Button(frame,text="Print",command=printOP)

# the command assigned is printOP

printButton.pack()





