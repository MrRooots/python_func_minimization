import matplotlib.pyplot as plt
import matplotlib as mplt
import pandas

HEADERS = ('Iterations', 'Limit Reached', 'Minimum', 'Point')


class TableBuilder:
  _data: list[list[int, bool, float, tuple[float, float]]] = []

  @staticmethod
  def _color_last_row(table: mplt.table.Table,
                      df: pandas.DataFrame) -> None:
    """ Set background color for all cells in last row """
    rows = len(df.values)

    for i in range(len(df.columns)):
      table.get_celld()[rows, i].set_facecolor('#a1c935')

  def add_data(self, data: list[int | str, bool, float, tuple[float, float]]) -> None:
    self._data.append(data)

  def build_table(self, headers: tuple[str, ...] = HEADERS) -> None:
    """ Draw table from given values """
    fig, ax = plt.subplots()
    df = pandas.DataFrame(self._data, columns=list(headers))

    ax.axis('off')
    ax.axis('tight')
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center')

    self._color_last_row(table, df)

    plt.show()
