import streamlit as st
import pandas as pd
from utils.ColumnValueReplacer import ColumnValueReplacer

st.set_page_config(layout='wide', page_title='Vendas dos Clientes Amazon e Amazon Prime')

buys_by_user = pd.read_csv('./data/Vendas Amazon - Compras por usuário.csv')
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

st.title('Vendas')

total_spent_column, total_buys_column = st.columns(2)

with total_spent_column:
    st.bar_chart(data=spent_value_by_user_category, x='Categoria Cliente', y='Valor Gasto')
with total_buys_column:
    st.bar_chart(data=total_buys_by_user_category, x='Categoria Cliente', y='Número de Compras')
