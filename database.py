import psycopg2
from psycopg2 import sql
from contrato import Vendas
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST=os.getenv("DB_HOST")
DB_NAME=os.getenv("DB_NAME")
DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")

def salvar_no_postgres(dados: Vendas):
    try:
        st.write(os.getenv("DB_HOST"))
        st.write(os.getenv("DB_NAME"))
        st.write(os.getenv("DB_USER"))
        st.write(os.getenv("DB_PASS"))
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            port="5432"
        )
        cursor = conn.cursor()
        
        insert_query = sql.SQL('''
            INSERT INTO vendas (email, data, valor, quantidade, produto) VALUES (
                %s, %s, %s, %s, %s)
                '''
        )
        
        cursor.execute(insert_query, (
            dados.email,
            dados.data,
            dados.valor,
            dados.quantidade,
            dados.produto.value
            )
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"Erro na conexao: {e}")