import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Database Query Engine")
st.subheader("Embark on a Stylish SQL Adventure:")
st.write("Unleashing Database Insights with LLM !✨")
question = st.text_input("Ask a question about your Schema:")

if st.button("Submit"):
    if question:
        chain = get_few_shot_db_chain()
        response,sql_query = chain.run(question)

        # print(response)
        # st.header("Question:")
        # st.write(question)

        st.subheader("SQLQuery:")
        st.write(sql_query[1])

        st.subheader("Answer:")
        st.write(response)
    else:
        st.warning("Please enter a question about T-shirts before submitting.")
