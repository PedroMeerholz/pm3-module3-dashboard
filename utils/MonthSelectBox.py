from pandas import Series
from streamlit import selectbox


class MonthSelectBox:
    @staticmethod
    def build(month_column: Series):
        select_box_options = list(month_column.apply(lambda x: x[:4]).unique())
        select_box_options.insert(0, 'Todo o período')
        return selectbox(label="Selecione o período desejado", options=select_box_options)
