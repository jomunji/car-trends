from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
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

def make_plot(request, col: str) -> HttpResponse:
    """
    This function takes in a string called col, and makes a trend graph.
    It first queries the database using the passed column name, before using the groupby to aggregate the data per year, based on what input the column is.
    This will average the passed column over the year.
    It then creates a trend plot and returns a HttpResponse object, using the image of the plot just made.
    """
    with connection.cursor() as cursor:
            cursor.execute("SELECT reg_year,"+col+" FROM ad_table")
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
    df = pd.DataFrame(data, columns=columns)

    fig, ax = plt.subplots()
    trendsdf = df.groupby("reg_year", as_index=False).mean()
    ax.plot(trendsdf["reg_year"], trendsdf[col], color="mediumaquamarine")
    plt.title("Cars per manufacturer")
    plt.subplots_adjust(left=0.15)
    plt.ylabel("Average "+col+" per year")
    plt.xlabel("Time")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    messages.success(request, "Plot loaded")
    return response


def trends_plots(request, col_input: str) -> HttpResponse:
    """
    Takes column input and makes plot using make_plot function
    """
    logger.warning("Column input: "+col_input)
    if col_input == '1':
        #Average price
        logger.warning("Average price")
        #Fetch all data from database
        response = make_plot(request,"price")
        return response
    elif col_input == '2':
        #Average mileage
        logger.warning("Average mileage please")
        #Fetch all data from database
        response = make_plot(request, "mileage")
        return response
    elif col_input == '3':
        #Frequency
        logger.warning("Frequency")
    else:
        #Fetch all data from database
        with connection.cursor() as cursor:
            cursor.execute("SELECT reg_year,price FROM ad_table")
            columns = [col[0] for col in cursor.description]
            data = cursor.fetchall()
        df = pd.DataFrame(data, columns=columns)

        fig, ax = plt.subplots()
        trendsdf = df.groupby("reg_year", as_index=False).mean()
        ax.plot(trendsdf["reg_year"], trendsdf["price"], color="mediumaquamarine")
        plt.title("Cars per manufacturer")
        plt.subplots_adjust(left=0.15)
        plt.ylabel("Average price per year")
        plt.xlabel("Time")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        messages.success(request, "Plot loaded")
        return response

