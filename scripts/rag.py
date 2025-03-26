from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain import utils
import os
from pydantic import BaseModel
from typing import List, Dict
import getpass
import json
import sys
import bs4
from langchain import hub
from langchain.graphs import START,StateGraph
from typing_extensions import List, TypedDict



def load_document(path:str):
    pass

def indexing():
    pass

def split_doc():
    pass

def embed_doc():
    pass