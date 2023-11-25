import streamlit as st
import pandas as pd
from utils.InvoicingFilter import InvoicingFilter
from utils.InvoicingFormatter import InvoicingFormatter
from utils.MonthSelectBox import MonthSelectBox

st.set_page_config(layout='wide', page_title='Clientes Amazon Prime')

formatter = InvoicingFormatter()
year_filter = InvoicingFilter()

prime_users = pd.read_csv('D:/Projects/pm3-module3-dashboard/data/Vendas Amazon - Clientes Amazon Prime.csv')
prime_users.columns = ['Mês/Ano', 'Novos Clientes', 'Clientes existentes', 'Clientes Ativos', 'Faturamento']
prime_users['Mês/Ano'] = formatter.format_date_column(month_list=prime_users['Mês/Ano'], remove_day=True)
prime_users['Faturamento'] = formatter.format_invoicing_column(invoicing_list=prime_users['Faturamento'])

st.title('Visão Geral Amazon Prime')

selected_year = MonthSelectBox.build(prime_users['Mês/Ano'])
filtered_users = year_filter.filter_invoicing_by_year(prime_users, selected_year) \
    if selected_year != 'Todo o período' else prime_users

users_chart, invoicing_chart = st.columns(2)

with users_chart:
    st.subheader('Evolução do Número de Clientes')
    st.bar_chart(data=filtered_users, x='Mês/Ano', y=['Clientes existentes', 'Novos Clientes', 'Clientes Ativos'])
with invoicing_chart:
    st.subheader('Faturamento')
    st.bar_chart(data=filtered_users, x='Mês/Ano', y='Faturamento')
