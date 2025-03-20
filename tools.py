from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
# from datetime import datetime
# import os

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="search",
    func = search.run,
    description="Search the web for information.",
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

# def read_files_from_bible_directory():
#     directory_path = os.path.join(os.path.dirname(__file__), '../bible')
#     files_content = []
#     for filename in os.listdir(directory_path):
#         file_path = os.path.join(directory_path, filename)
#         if os.path.isfile(file_path):
#             try:
#                 with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
#                     files_content.append(file.read())
#             except Exception as e:
#                 print(f"Skipping file {filename} due to error: {e}")
#     return files_content

# bible_tool = read_files_from_bible_directory()
