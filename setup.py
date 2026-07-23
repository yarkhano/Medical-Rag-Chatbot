
#for importing packages from different files setup.py is required also it is like ID card of your project

from setuptools import setup, find_packages

setup(
    name="Medical Chatbot",
    version="1.0",
    author="Muhammad Yar Khan",
    author_email="muhammadyarkhan586@gmail.com",
    packages=find_packages(),
    install_requires=[
        "langchain==0.3.26",
        "langchain-community==0.3.26",
        "langchain-pinecone==0.2.8",
        "langchain-groq==0.3.6",
        "fastapi==0.115.14",
        "uvicorn==0.35.0",
        "sentence-transformers==4.1.0",
        "pypdf==5.6.1",
        "python-dotenv==1.1.0"
    ]
)