from pandas import DataFrame


class InvoicingFilter:

    def filter_invoicing_by_year(self, invoicing_data: DataFrame, year: str):
        invoicing_data_copy = invoicing_data.copy()
        return self.select_year_data(invoicing_data, year, 'Mês') if 'Mês' in invoicing_data_copy.columns \
            else self.select_year_data(invoicing_data, year, 'Meses')

    @staticmethod
    def select_year_data(invoicing_data: DataFrame, year: str, column: str):
        invoicing_data_copy = invoicing_data.copy()
        index = 0
        for invoicing_month in invoicing_data_copy[column]:
            if invoicing_month.find(year) != 0:
                invoicing_data_copy.drop(index, axis=0, inplace=True)
            index = index + 1
        return invoicing_data_copy
