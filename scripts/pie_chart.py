import connection
import matplotlib.pyplot as plt

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.1f}% ({v:d})'.format(p=pct,v=val)
    return my_autopct

def plot(what, title, where):
    sql_first = """
        SELECT <placeholder>.description,
               count(*)
        FROM post
        LEFT JOIN <placeholder> ON <placeholder>.id = post.<placeholder>
    """
    sql_middle = where

    sql_last = """
        GROUP BY <placeholder>.description, <placeholder>.id
        ORDER BY <placeholder>.id
    """

    sql = sql_first + sql_middle + sql_last
    sql = sql.replace('<placeholder>', what)

    connection.run_sql(sql)
    results = connection.results()

    labels = []
    data = []

    for result in results:
        labels.append(result[0])
        data.append(result[1])

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=labels, autopct=make_autopct(data), shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    fig1.suptitle(title, fontsize=14, fontweight='bold')
    ax1.set_title('Total: %d' % sum(data), y = 1.05)
    fig1.subplots_adjust(top=0.85)

    filename = title.lower().replace(' ', '_') + '.png'

    plt.savefig('../plots/' + filename)
