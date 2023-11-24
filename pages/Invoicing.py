import streamlit as st
import pandas as pd
from utils.InvoicingFilter import InvoicingFilter
from utils.InvoicingFormatter import InvoicingFormatter
from utils.MonthSelectBox import MonthSelectBox

st.set_page_config(layout='wide', page_title='Faturamento e Tickét Médio')

formatter = InvoicingFormatter()
year_filter = InvoicingFilter()

invoicing = pd.read_csv('D:/Projects/pm3-module3-dashboard/data/Vendas Amazon - Faturamento Amazon.csv')
invoicing['Mês'] = formatter.format_date_column(invoicing['Mês'].unique(), remove_day=False)
invoicing['Faturamento'] = formatter.format_invoicing_column(invoicing_list=invoicing['Faturamento'])
invoicing['Tickét Médio'] = formatter.format_ticket_column(invoicing['Tickét Médio'])

invoicing_column, ticket_column = st.columns(2)

selected_year = MonthSelectBox.build(invoicing['Mês'])
filtered_invoicing = year_filter.filter_invoicing_by_year(invoicing, selected_year) \
    if selected_year != 'Todo o período' else invoicing

charts_size = 400
with invoicing_column:
    st.subheader('Faturamento')
    st.line_chart(data=filtered_invoicing, x='Mês', y='Faturamento', height=charts_size)
with ticket_column:
    st.subheader('Ticket Médio')
    st.line_chart(data=filtered_invoicing, x='Mês', y='Tickét Médio', height=charts_size)
