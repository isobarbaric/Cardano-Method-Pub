import numpy as np
import requests
from datetime import date, timedelta
import matplotlib.pyplot as plt

def covid_graph():
    reference_indices = []
    daily_totals = []

    start_date = date(2021, 11, 26)
    end_date = date.today()
    delta = timedelta(days=1)
    html_file = requests.get('https://health-infobase.canada.ca/src/data/covidLive/covid19.json').json()
    
    while start_date <= end_date:
        for i in html_file:
            if i['prname'] == 'Canada' and i['date'] == start_date.strftime("%d-%m-%Y"):
                daily_totals.append(int(i['numtoday']))
                break
        start_date += delta
    
    for i in range(1, len(daily_totals)+1):
        reference_indices.append(i)

    # polynomial fit with degree = 3
    best_fit = np.poly1d(np.polyfit(reference_indices, daily_totals, 3))
    cf = [float(i) for i in best_fit.c]

    polyline = np.linspace(1, 60, 50)
    plt.scatter(reference_indices, daily_totals)
    plt.plot(polyline, best_fit(polyline))
    plt.show()

    return cf