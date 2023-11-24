from pandas import Series


class InvoicingFormatter:
    @staticmethod
    def format_date_column(month_list: Series):
        new_month_column = []
        for month in month_list:
            text_month = month[:2]
            text_year = month[3:]
            new_month_value = text_year + '/' + text_month
            new_month_column.append(new_month_value)
        return new_month_column

    @staticmethod
    def format_invoicing_column(invoicing_list: Series):
        new_invoicing_column = invoicing_list.apply(lambda x: x.replace('R$ ', ''))
        new_invoicing_column = new_invoicing_column.apply(lambda x: x.replace('.', ''))
        new_invoicing_column = new_invoicing_column.apply(lambda x: x.replace(',', '.'))
        new_invoicing_column = new_invoicing_column.apply(lambda x: float(x))
        # new_invoicing_column = new_invoicing_column.apply(lambda x: 'R$ ' + str(x))
        return new_invoicing_column

    @staticmethod
    def format_ticket_column(ticket_column: Series):
        new_ticket_column = ticket_column.apply(lambda x: x.replace('R$ ', ''))
        new_ticket_column = new_ticket_column.apply(lambda x: x.replace(',', '.'))
        new_ticket_column = new_ticket_column.apply(lambda x: float(x))
        return new_ticket_column
