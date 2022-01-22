import numpy as np
import requests
from datetime import date, timedelta
import matplotlib.pyplot as plt

#
def PolyCoefficients(x, coeffs):
    """ Returns a polynomial for ``x`` values for the ``coeffs`` provided.

    The coefficients must be in ascending order (``x**0`` to ``x**o``).
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y
#

def covid_graph():
    reference_indices = []
    daily_totals = []

    start_date = date(2021, 11, 29)
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

    for i in range(len(daily_totals)):
        print(reference_indices[i], daily_totals[i])

    # polynomial fit with degree = 3
    model = np.poly1d(np.polyfit(reference_indices, daily_totals, 3))
    print(model)
    cf = [float(i) for i in model.c]
    print("this is the model", cf)

    #
    polyline = np.linspace(1, 60, 50)
    plt.scatter(reference_indices, daily_totals)
    plt.plot(polyline, model(polyline))
    plt.show()
    #

    # cf.reverse()
    
    #
    x = np.linspace(0, 60, 50)
    plt.plot(x, PolyCoefficients(x, cf))
    plt.show()
    #

    return cf