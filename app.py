import streamlit as st
from datetime import datetime, time
from contrato import Vendas
from pydantic import ValidationError
from database import salvar_no_postgres

def main():
    
    st.title('Sistema de CRM e Vendas - FrontEnd Simples')
    email = st.text_input("Campo de texto para inserção do e-mail do vendedor")
    data = st.date_input("Campo para selecionar a data em que a venda foi realizada", datetime.now())
    hora = st.time_input("Campo para selecionar a hora em que a venda foi realizada", value=time(9,0))
    valor = st.number_input("Campo numérico para inserir o valor monetário da venda realizada", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Campo numérico para inserir a quantidade de produtos vendidos.", min_value=1, step=1)
    produto = st.selectbox("Campo de seleção para escolher o produto vendido.", options=["Gemini", "ChatGTP", "Llamma"])
    
    try:
        if st.button("Salvar"):
            data_hora = datetime.combine(data, hora)
            
            venda = Vendas(
                email = email,
                data = data,
                valor = valor,
                quantidade = quantidade,
                produto = produto,
            )
            
            st.write("**Dados da Venda:**")
            st.write(f"Email do Vendedor: {email}")
            st.write(f"Dados da Venda:{data_hora}")
            st.write(f"Dados da Venda:{valor:.2f}")
            st.write(f"Dados da Venda:{quantidade}")
            st.write(f"Dados da Venda:{produto}")
            
            st.write(venda)
            salvar_no_postgres(venda)
    except Exception as e:
        st.error(f"{e}")
    
if __name__=="__main__":
    main()