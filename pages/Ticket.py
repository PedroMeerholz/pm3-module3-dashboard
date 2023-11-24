import streamlit as st
import pandas as pd
from utils.InvoicingFilter import InvoicingFilter
from utils.InvoicingFormatter import InvoicingFormatter
from utils.MonthSelectBox import MonthSelectBox

PAGE_TITLE = 'Ticket Médio'
st.set_page_config(layout='wide', page_title=PAGE_TITLE)
st.title(PAGE_TITLE)

invoicing = pd.read_csv('D:/Projects/pm3-module3-dashboard/data/Vendas Amazon - Faturamento Amazon.csv')
invoicing['Mês'] = InvoicingFormatter.format_date_column(invoicing['Mês'].unique())
invoicing['Tickét Médio'] = InvoicingFormatter.format_ticket_column(invoicing['Tickét Médio'])

selected_year = MonthSelectBox.build(invoicing['Mês'])
filtered_invoicing = InvoicingFilter.filter_invoicing_by_year(invoicing, selected_year) \
    if selected_year != 'Todo o período' else invoicing

st.line_chart(data=filtered_invoicing, x='Mês', y='Tickét Médio', height=400)
