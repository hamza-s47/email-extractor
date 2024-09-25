import os
import mimetypes
import PyPDF2
import docx2txt
import pandas as pd
from docx import Document
from pptx import Presentation
import requests
from bs4 import BeautifulSoup

# Function to extract text from a webpage given its URL
def extract_url(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve the page: {response.status_code}")
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract and return all the visible text from the webpage
        return soup.get_text(separator=' ')
    
    except Exception as e:
        return f"Error extracting text from URL: {e}"
# Function to extract text from PDF
def extract_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

# Function to extract text from DOCX
def extract_docx(file_path):
    doc = Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

# Function to extract text from DOC (using docx2txt)
def extract_doc(file_path):
    return docx2txt.process(file_path)

# Function to extract text from PPTX
def extract_pptx(file_path):
    prs = Presentation(file_path)
    text = ''
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + '\n'
    return text

# Function to extract text from TXT
def extract_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to extract text from XLSX
def extract_excel(file_path):
    df = pd.read_excel(file_path)
    return df.to_string()

# Master function to handle file extraction based on type
def extract_text_from_file(file_path):
    file_type, _ = mimetypes.guess_type(file_path)
    
    if file_type == 'application/pdf':
        return extract_pdf(file_path)
    elif file_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return extract_docx(file_path)
    elif file_type == 'application/msword':
        return extract_doc(file_path)
    elif file_type == 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
        return extract_pptx(file_path)
    elif file_type == 'text/plain':
        return extract_txt(file_path)
    elif file_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        return extract_excel(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

# Example usage
if __name__ == '__main__':
    file_path = os.getcwd()  # Update with the path to your file
    try:
        extracted_text = extract_text_from_file(file_path)
        print("Extracted Text:\n", extracted_text)
    except Exception as e:
        print(f"Error extracting text: {e}")
