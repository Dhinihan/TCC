import connection
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from tcc_plots import utils

colors = ['r', 'g', 'b', 'y']


def label_top(rects, ax):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
            '%dk' % int(height/1000),
            ha='center', va='bottom')

def label_middle(rects, ax):
    previous_height = []
    for i in range(len(rects[0])):
        previous_height.append(0)
    for rect in rects:
        for i, bar in enumerate(rect):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width()/2.,
                height/2 + previous_height[i] - 0.035,
                ('%.1f' % float(height*100)) + '%',
                ha='center',
                va='bottom'
            )
            previous_height[i] += height

def _separate(results):
    x = []
    y = []
    total = []

    number_bars = len(results[0]) - 1
    for i in range(number_bars):
        y.append([])

    for result in results:
        x.append(result[0])
        total.append(0)
        for i in range(number_bars):
            total[len(total)-1] += result[i+1]
            y[i].append(result[i+1])

    return x, y, total

def plot(sql, title, legend = False):
    connection.run_sql(sql)
    results = connection.results()

    x, y, total = _separate(results)

    N = len(x)
    ind = range(N)  # the x locations for the groups
    width = 0.50       # the width of the bars

    fig, ax = plt.subplots()
    rects = []
    bottom = [0 for element in y[0]]
    for i, data in enumerate(y):
        rects.append(ax.bar(ind, data, width, color=colors[i], bottom=bottom))
        bottom = [element+y[i][j] for j, element in enumerate(bottom)]

    # add some text for labels, title and axes ticks
    ax.set_title(title)
    ax.set_xticks([i + width/2 for i in ind])
    ax.set_xticklabels([label for label in x])

    if (legend != False):
        plt.legend(rects, legend)

    # ax.legend(rects1[0], ('Men'))

    if (len(rects) == 1):
        label_top(rects[0], ax)
    else:
        label_middle(rects, ax)



    plt.axis([0 - width, len(x), 0, float(max(total))*1.618])

    plt.savefig(utils.filename_from_title(title, 'png'))
    plt.clf()