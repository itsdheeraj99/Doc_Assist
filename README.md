# Custom chatbot for your Data
This chatbot is built using LangChain and Streamlit.<br>
This application is using Pinecone as vectorstore.<br>
Also, for demonstration the data used for interaction is [GPT4 technical report.](https://arxiv.org/pdf/2303.08774.pdf)

![LOGO](https://github.com/itsdheeraj99/Doc_Assist/blob/main/demo/demo.gif) 

## Installations
- Clone the repository<br>
``` git clone https://github.com/itsdheeraj99/Doc_Assist.git```
- For the data, you can use your custom data PDF files, by entering the PDF URLs in the ```ingestion.py``` file.
- To install all the dependencies run <br> ```pip install -r requirements.txt```
- Make sure to add the environment variables such as `Pinecone_Environment_region`, `Pinecone` and `OpenAI` API keys to your virtual environment files. 

## Usage
- Start the local server by running <br>```streamlit run main.py```

## Limitations
- Currently, has only access to one data file.

## Future work
- To add more data for better interactions.