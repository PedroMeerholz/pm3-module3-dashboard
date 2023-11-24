import pandas as pd


class InvoicingFilter:

    @staticmethod
    def filter_invoicing_by_year(invoicing_data: pd.DataFrame, year: str):
        invoicing_data_copy = invoicing_data.copy()
        index = 0
        for invoicing_month in invoicing_data_copy['Mês']:
            if invoicing_month.find(year) != 0:
                invoicing_data_copy.drop(index, axis=0, inplace=True)
            index = index + 1
        return invoicing_data_copy
