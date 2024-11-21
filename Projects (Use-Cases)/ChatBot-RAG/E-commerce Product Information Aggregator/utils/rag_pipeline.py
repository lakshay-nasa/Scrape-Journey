from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Use the following book data to respond to user queries: {book_data}"),
        ("user", "Question: {question}")
    ]
)

llm = Ollama(model="llama3.2")
output_parser = StrOutputParser()

def run_rag_chain(question, book_data):
    """Run the Retrieve and Generate (RAG) pipeline to get the response."""
    chain = prompt | llm | output_parser
    response = chain.invoke({"question": question, "book_data": book_data})
    return response
