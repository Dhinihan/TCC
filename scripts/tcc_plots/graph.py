import connection
import matplotlib.pyplot as plt
from tcc_plots import utils

def _separate(results):
    x = []
    y = []

    for result in results:
        x.append(result[0])
        y.append(result[1])

    return x, y

def plot(sql, title):
    connection.run_sql(sql)
    results = connection.results()

    x, y = _separate(results)

    N = len(x)
    ind = range(N)  # the x locations for the groups
    width = 0.50       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, y, width, color='r')

    # add some text for labels, title and axes ticks
    ax.set_title(title)
    ax.set_xticks([i + width/2 for i in ind])
    ax.set_xticklabels([date.strftime("%Y") for date in x])

    # ax.legend(rects1[0], ('Men'))


    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    autolabel(rects1)

    plt.axis([0 - width, len(x), 0, max(y)*1.618])

    plt.savefig('../plots/' + utils.filename_from_title(title, 'png'))
    plt.clf()