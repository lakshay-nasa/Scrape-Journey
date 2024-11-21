import streamlit as st
from utils.database import query_books, loadMy_data_into_db
from utils.rag_pipeline import run_rag_chain
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# sqLite Db
DB_PATH = "./data/books.db"

# load books.json into SQLite (It will run once during setup)
if not os.path.exists(DB_PATH):
    loadMy_data_into_db("data/books.json", DB_PATH)

st.title('Book Information Aggregator')

input_text = st.text_input("Search for books or ask a question")

if input_text:

    search_results = query_books(input_text, DB_PATH)
    
    if search_results:
        book_data = "\n".join([f"Title: {title}, Price: ${price}, Rating: {rating}, Availability: {availability}" for title, price, rating, availability in search_results])
    else:
        book_data = "No relevant books found."
    
    response = run_rag_chain(input_text, book_data)
    
    # Display Relevant Books Results
    st.subheader("Relevant Books")
    if search_results:
        for title, price, rating, availability in search_results:
            st.write(f"**Title:** {title}\n- **Price:** ${price}\n- **Rating:** {rating}\n- **Availability:** {availability}")
    else:
        st.write("No books matched your query.")
    
    # st.subheader("Response from LLAMA3.2")
    # st.write(response)
