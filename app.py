import streamlit as st
import pandas as pd
import plotly.express as px
from ColumnValueReplacer import ColumnValueReplacer

st.set_page_config(layout='wide')

st.title('Análise Amazon')
buys_by_user = pd.read_csv('D:/Projects/pm3-module3-dashboard/data/Vendas Amazon - Compras por usuário.csv')
buys_by_user = buys_by_user[['ID Usuário', 'Nome', 'Valor Gasto', 'Número de compras ', 'Estado', 'Assinantes', 'Idade']]
buys_by_user['Valor Gasto'] = ColumnValueReplacer.replace_value_from_column(buys_by_user['Valor Gasto'], 'R$ ', '')
buys_by_user['Valor Gasto'] = ColumnValueReplacer.replace_value_from_column(buys_by_user['Valor Gasto'], '.', '')
buys_by_user['Valor Gasto'] = ColumnValueReplacer.replace_value_from_column(buys_by_user['Valor Gasto'], ',', '.').astype(float)

subscribers_buys = buys_by_user[buys_by_user['Assinantes'] == 'Sim']
not_subscribers_buys = buys_by_user[buys_by_user['Assinantes'] == 'Não']

spent_value_by_user_category = pd.DataFrame(data={
    'Categoria Cliente': ['Assinante', 'Não Assinante'],
    'Valor Gasto': [subscribers_buys['Valor Gasto'].sum(), not_subscribers_buys['Valor Gasto'].sum()]
})

total_buys_by_user_category = pd.DataFrame(data={
    'Categoria Cliente': ['Assinante', 'Não Assinante'],
    'Número de Compras': [subscribers_buys['Número de compras '].sum(), not_subscribers_buys['Número de compras '].sum()]
})

left_column, right_column = st.columns(2)

spent_value_by_user_category_bar_plot = px.bar(spent_value_by_user_category, x='Categoria Cliente', y='Valor Gasto', title='Valor total gasto (R$)')
left_column.plotly_chart(spent_value_by_user_category_bar_plot)

total_buys_by_user_category_bar_plot = px.bar(total_buys_by_user_category, x='Categoria Cliente', y='Número de Compras', title='Quantidade de compras')
right_column.plotly_chart(total_buys_by_user_category_bar_plot)
