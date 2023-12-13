from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from .models import *

import logging
logger = logging.getLogger(__name__)

#This function renders the home.html file when called.
def home(request): #The request argument is created whenever a page loads, it contains metadata

    return render(request,'home/home.html',{})



import pandas as pd
import random
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvas

#This function returns a list of tuples of RGB values.
#I used it to colour all of my plots.
def randomRGB(length):
    colourList = []
    if length == 1:  #If length is 1 return a single tuple.
        return (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))
    else:  #If length is greater than 1:
        for i in range(length): #Loop for given range
            rgbtup = (random.uniform(0,1),random.uniform(0,1),random.uniform(0,1))#For each iteration create a tuple...
            colourList.append(rgbtup) #...and add it to the list
        return(colourList) #return the final list

def plots(request): #The request argument is created whenever a page loads, it contains metadata
    
    #Fetch all data from database
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,maker FROM ad_table")
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    # logger.warning(df.head())

    #Create home visual
    matplotlib.use("agg")
    fig, ax = plt.subplots()
    home_visual_df = df.groupby("maker", as_index=False).count().sort_values(by="id", ascending=False)[:20]
    # logger.warning(home_visual_df.sort_values(by="id"))
    # logger.warning("---------")
    # logger.warning(home_visual_df.columns)
    ax.bar(home_visual_df["maker"], home_visual_df["id"], color=randomRGB(20))
    ax.set_title("Manufacturers")
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.3)

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response