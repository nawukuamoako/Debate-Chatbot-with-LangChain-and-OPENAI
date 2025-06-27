# Debate Chatbot with LangChain and OpenAI

A debate chatbot powered by LangChain and OpenAI's GPT-4o-mini model that engages users in logical, respectful debates on various topics. The bot defends the opposing stance to the user’s position, uses external tools like search and Wikipedia for factual support, and provides structured responses.

---

## Features

- Interactive debate on any user-provided topic
- Opposing stance argument generation based on user input
- Fact-checking and information retrieval via integrated search and Wikipedia tools
- Clear, structured chatbot responses wrapped in a Pydantic model
- Graceful handling of user input and exit commands

---

## Requirements

- Python 3.8+
- Dependencies listed includes `langchain`, `pydantic`, `python-dotenv`, `openai`
- OpenAI API key stored in a `.env` file as `OPENAI_API_KEY`

---

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/nawukuamoako/Debate-Chatbot-with-LangChain-and-OPENAI.git
   cd Debate-Chatbot-with-LangChain-and-OPENAI
   ```

2. Install dependencies

3. Create a .env file with your OpenAI API key

## Usage
Run the chatbot script:

```bash
python debate.py
```
Follow the prompts:
- Enter the topic of debate
- Indicate if you are “For” or “Against” the topic
- Enter your argument supporting your stance
- Chat interactively with the bot defending the opposing side
- Type exit to quit the conversation

---

## Project Structure
- debate.py — Main script to run the chatbot interaction
- tools.py — External tools like search and Wikipedia integrations
- .env — Environment variables (not included in repo)

---

### Notes
- Ensure your OpenAI API key is valid and has sufficient quota.
- The chatbot is designed to maintain respectful and logical debate tone.
- Parsing errors may occur if the model output does not match the expected format; in such cases, try again or review logs.

