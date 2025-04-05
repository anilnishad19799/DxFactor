from rag_agent import RAGWorkflow
import streamlit as st

# Streamlit UI
workflow = RAGWorkflow()
st.title("DxFactor Chat Agent")
query = st.text_input("Enter your question : ")
if st.button("Get Answer"):
    if query:
        response, source = workflow.process_query(query)
        st.write("### Answer:")
        st.write(response)
        st.write("### Data Source:")
        st.write(source)
    else:
        st.warning("Please enter a query.")
