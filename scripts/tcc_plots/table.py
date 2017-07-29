import connection
import pdfkit
from tcc_plots import utils


def _start_html(title):
    return  """
    <head>
        <meta charset="UTF-8">
        <style>
        table {
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid black;
        }

        td, th {
            padding: 3px
        }
        </style>
    </head>
    <body>
    <h1>%s</h1>
    <table>
    """ % title

def _get_page_height(rows):
    return str(rows*5.55 + 30) + 'mm'

def _build_table(results, title, headers):

    html = _start_html(title)

    html += "<tr><th>%s</th><th>%s</th></tr>" % headers


    for result in results:
        html += "<tr><td>%s</td><td>%s</td></tr>" % result
    html += "</table></body>"

    return html

def _save_table(html, results, title):
    options = {
        'page-height': _get_page_height(len(results)),
        'page-width': '300mm',
    }

    pdfkit.from_string(html, utils.filename_from_title(title, 'pdf'), options=options)


def plot(sql, title, headers):

    connection.run_sql(sql)
    results = connection.results()

    html = _build_table(results, title, headers)

    _save_table(html, results, title)

def plot_transpose(sql, title, headers):

    connection.run_sql(sql)
    results = connection.results()
    columns = connection.columns()

    transposed = []
    for index, value in enumerate(results[0]):
        transposed.append((columns[index], str(value)))

    html = _build_table(transposed, title, headers)

    _save_table(html, transposed, title)