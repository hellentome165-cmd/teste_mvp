import streamlit as st
# biblioteca de interface grafica 


# função que cria o título 
st.title('Isso é um título')


# funções que adicionam um texto na tela 
# função que adiciona um número
nome  =  st.text_input('Nome:')
idade  =  st.number_input('Idade:')
curso = st.text_input('Curso: ')


st.image('SRC/img.png')
st.audio('SRC/msc.mp3')


if nome and idade:
    if st.button('Mostrar'):
        st.write(nome)
        st.write(idade)
        st.write(curso)


# ctrl + " -> teminal abre 
# streamlit run app.py        
        