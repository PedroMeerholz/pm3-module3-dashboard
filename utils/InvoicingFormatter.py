from pandas import Series
from utils.ColumnValueReplacer import ColumnValueReplacer
from utils.date.DateFormatter import DateFormatter


class InvoicingFormatter:
    replacer = ColumnValueReplacer()
    date_formatter = DateFormatter()

    def format_date_column(self, month_list: Series, remove_day: bool):
        new_month_column = []
        if remove_day:
            new_month_column = self.date_formatter.remove_day_of_month_from_date(month_list)
        return self.date_formatter.format_date_column(month_list) if len(new_month_column) == 0 \
            else self.date_formatter.format_date_column(new_month_column)

    def format_invoicing_column(self, invoicing_list: Series):
        new_invoicing_column = self.replacer.replace_value_from_column(invoicing_list, 'R$ ', '')
        new_invoicing_column = self.replacer.replace_value_from_column(new_invoicing_column, '.', '')
        new_invoicing_column = self.replacer.replace_value_from_column(new_invoicing_column, ',', '.')
        new_invoicing_column = new_invoicing_column.apply(lambda x: float(x))
        return new_invoicing_column

    def format_ticket_column(self, ticket_column: Series):
        new_ticket_column = self.replacer.replace_value_from_column(ticket_column, 'R$ ', '')
        new_ticket_column = self.replacer.replace_value_from_column(new_ticket_column, ',', '.')
        new_ticket_column = new_ticket_column.apply(lambda x: float(x))
        return new_ticket_column
