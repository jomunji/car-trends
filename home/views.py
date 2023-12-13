from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from .models import *
from django.template import loader

import logging
logger = logging.getLogger(__name__)

#This function renders the home.html file when called.
def home(request): #The request argument is created whenever a page loads, it contains metadata
    #Fetch query from database
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ad_table")
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    # logger.warning(df.summary())
    mean_price = round(df["price"].mean(),2)
    std_dev_price = round(df["price"].std(),2)
    mean_mileage = int(round(df["mileage"].mean(),0))
    std_dev_mileage = int(round(df["mileage"].std(),0))
    common_body_type = df["bodytype"].value_counts().idxmax()
    common_manufacturer = df["maker"].value_counts().idxmax()
    common_colour = df["colour"].value_counts().idxmax()
    mean_engine_size = round(df["engine_size"].mean(),1)
    
    # logger.warning(df.info())
    context = {
        'mean_price': mean_price,
        'std_dev_price': std_dev_price,
        'mean_mileage': mean_mileage,
        'std_dev_mileage': std_dev_mileage,
        'common_body_type': common_body_type,
        'common_manufacturer': common_manufacturer,
        'common_colour': common_colour,
        'mean_engine_size': mean_engine_size,
    }

    # std_dev_price }}</b></div>
    # <div class="stat">Mean mileage:<b>£{{ mean_mileage }}</b></div>
    # <div class="stat">Mileage standard deviation:<b>£{{ std_dev_mileage }}</b></div>
    # <div class="stat">Most common body type:<b>£{{ common_body_type }}</b></div>
    # <div class="stat">Most common manufacturer:<b>£{{ common_manufacturer }}</b></div>
    # <div class="stat">Most common colour:<b>£{{ common_colour }}</b></div>
    # <div class="stat">Average engine size:<b>£{{ mean_engine_size }}</b></div>
    return render(request,'home/home.html',context)



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
    
    #Fetch query from database
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,maker FROM ad_table")
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    # logger.warning(df.head())

    #Create home visual
    matplotlib.use("agg")
    fig, ax = plt.subplots()
    home_visual_df = df.groupby("maker", as_index=False).count().sort_values(by="id", ascending=False)[:10]
    # logger.warning(home_visual_df.sort_values(by="id"))
    # logger.warning("---------")
    # logger.warning(home_visual_df.columns)
    ax.barh(home_visual_df["maker"], home_visual_df["id"], color=[("#6163fd"),("#aeaffe")], edgecolor = "none")
    title=plt.title("Cars per manufacturer")
    title.set_position([0.4,1])
    # plt.xticks(rotation=90)
    plt.subplots_adjust(left=0.2, bottom=0.1,top=0.9, right=1)
    ax.set_frame_on(False)
    # ax.set_yticks([])
    # ax.spines["top"].set_visible(False)
    # ax.spines["right"].set_visible(False)
    #plt.tick_params(axis='x', which='major', pad=-15)#Move x ticks up or down

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response