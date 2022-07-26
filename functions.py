import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import re
import lxml
import numpy as np
import requests
from bs4 import BeautifulSoup


def scrape_column(obj):
    find = soup.select(obj)
    return [i.getText().strip() for i in find]
def scrape_column(obj):
    find = soup.select(obj)
    return [i.getText().strip() for i in find]
 overall, potential, wage, value
def generate_df(player, overall, potential, wage, value):
   
    fifa_stats = {'Player':player,
                  'Overall':overall,
                  'Potential':potential,
                  'Wage':wage,
                  'Value':value                     
}
    fifadf = pd.DataFrame(fifa_stats)
    return fifadf
def webscrape():
    fifa = 'https://sofifa.com/players?type=all&lg%5B%5D=13&pn%5B%5D=25&pn%5B%5D=27&pn%5B%5D=23'
    fifahtml = requests.get(fifa)
    soup = BeautifulSoup(html.content, 'html.parser')
    player = scrape_column('div.ellipsis')[::2]
    overall = scrape_column ('td.col.col-oa')
    potential = scrape_column('td.col.col-pt')
    wage = scrape_column ('td.col.col-wg')
    value = scrape_column ('td.col.col-vl')
​
   
    fifadf = generate_df(player,overall, potential, wage, value)
    return fifadf