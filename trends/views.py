from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.contrib import messages
from .models import *
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def trends(request):
    return render(request,'trends/trends.html',{})


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvas
from home.views import randomRGB

def trends_plots(request):
    #Fetch all data from database
    with connection.cursor() as cursor:
        cursor.execute("SELECT reg_year,price FROM ad_table")
        columns = [col[0] for col in cursor.description]
        data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)
    logger.warning(df.head())

    #Create trends visual
    matplotlib.use("agg")
    fig, ax = plt.subplots()
    trendsdf = df.groupby("reg_year", as_index=False).mean()
    ax.plot(trendsdf["reg_year"], trendsdf["price"], color="mediumaquamarine")
    plt.title("Cars per manufacturer")
    # title.set_position([0.4,1])
    # plt.xticks(rotation=90)
    plt.subplots_adjust(left=0.15)
    # ax.set_frame_on(False)
    # ax.set_yticks([])
    plt.ylabel("Average price per year")
    plt.xlabel("Time")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    #plt.tick_params(axis='x', which='major', pad=-15)#Move x ticks up or down

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    messages.success(request, "Plot loaded")
    return response