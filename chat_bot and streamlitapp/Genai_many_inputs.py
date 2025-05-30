import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate as PT
from langchain_huggingface import HuggingFaceEndpoint as HFE

load_dotenv()
hf_token=os.getenv("my_key")
module_name=os.getenv("MODEL_NAME")

template="""Can you help me or guide me to fix my problem: "{problem}"?
It is related to the product: "{product_name}", which is a {product_nature}.
I would like the explanation or solution in {language}. """

llm=HFE(
    huggingfacehub_api_token=hf_token,
    repo_id=module_name,
    task="text-generation",
    max_new_tokens=1024,
    provider="hf-inference"
)

prompt = PT(
    input_variables=["problem","product_name","product_nature","language"],
    template=template
)

solution_chain = prompt | llm

def get_solution(inputs:dict)-> str:
    return solution_chain.invoke(inputs)

# def solution(inputs):
#     sol=inputs
#     result = solution_chain.invoke(sol)
#     print(f"solution{result}")
    
# problem=str(input("Enter the problem"))    
# product_name=str(input("Enter a product name"))
# product_nature=str(input("Enter the product nature"))
# language=str(input("Enter a language"))
# inputs={"problem":problem,"product_name":product_name,"product_nature":product_nature,"language":language}

# solution(inputs)