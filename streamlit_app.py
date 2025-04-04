from rag_agent import AgenticRAGWorkflow
import streamlit as st

# Streamlit UI
workflow = AgenticRAGWorkflow()
st.title("Agentic Corrective Workflow with LangChain Memory")
query = st.text_input("Enter your query:")
if st.button("Get Answer"):
    if query:
        response, source = workflow.process_query(query)
        st.write("### Answer:")
        st.write(response)
        st.write("### Data Source:")
        st.write(source)
    else:
        st.warning("Please enter a query.")
