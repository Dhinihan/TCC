import connection
import matplotlib.pyplot as plt
from tcc_plots import utils

def _make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '{p:.1f}% ({v:d})'.format(p=pct, v=val)
    return my_autopct

def _transform_data(results):
    labels = []
    data = []

    for result in results:
        labels.append(result[0])
        data.append(result[1])

    return labels, data

def _build_plot(fig, ax, data, labels, title):

    ax.pie(data, labels=labels, autopct=_make_autopct(data), shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title('Total: %d' % sum(data), y=1.05)

    fig.suptitle(title, fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.85)

def plot(sql, title):
    connection.run_sql(sql)
    results = connection.results()

    labels, data = _transform_data(results)

    fig1, ax1 = plt.subplots()

    _build_plot(fig1, ax1, data, labels, title)

    plt.savefig('../plots/' + utils.filename_from_title(title, 'png'))
    plt.clf()
