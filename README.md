## 🛠️ Product Helper Chat App
A Streamlit-powered AI assistant that helps users solve problems related to products, powered by Hugging Face language models and LangChain.

## 📌 Features
🔍 Problem Understanding — Users input a problem and product details.

🧠 AI Assistance — The app generates a helpful solution or explanation.

🌍 Multilingual Support — Choose your preferred language for the response.

🧩 Modular Codebase — Organized into core logic and UI layers.

⚙️ Powered by Hugging Face Transformers + LangChain

## 📸 Demo

![screenshot](/images/Screenshot%201.png)
![](/images/Screenshot%202.png)

## 🚀 Quick Start
✅ Clone the Repo
git clone https://github.com/Naveenbalajis81/GenAI_project_.git
cd GenAI_project_/product_helper

✅ Install Dependencies
use this commend to install requirements
"pip install -r requirements.txt"

✅ Set Up Environment Variables
Create a .env file in the root:
my_key=your_huggingface_api_key
MODEL_NAME=model_name eg:"HuggingFaceH4/zephyr-7b-alpha"

✅ Run the App
use this commend make sure env is activate or not 
"streamlit run app.py"

## 🗂️ Project Structure
<pre>
product_helper/
│
├── chat_bot and streamlitapp/
│   ├── StreamlitApps.py        # Main Streamlit app 
│   └── Genai_many_inputs.py    # Hugging Face + LangChain logic
├── .env                        # API keys (ignored by git)
├── requirements.txt            # All Python dependencies
└── README.md                   # You're reading it!
</pre>

## 🧠 Tech Stack
Streamlit – Fast interactive apps

LangChain – Prompt handling and chains

Hugging Face – LLMs via API

Python + dotenv – Clean modular environment

## 🧪 Example Input
<pre>
Field	                   Example
Problem	  The app crashes when I click the "Submit" button.
Product   Name	MyFinanceApp
Product   Nature personal finance management software
Language  English
</pre>