import streamlit as st
from Genai_many_inputs import get_solution as gs


st.set_page_config(page_title="Product Helper", page_icon="🛠️")
st.title("🛠️ Product Problem Solver")

with st.form("problem_form"):
    problem = st.text_area("Describe your problem", height=100)
    product_name = st.text_input("Product Name")
    product_nature = st.text_input("Product Nature")
    language = st.selectbox("Preferred Language", ["English","Tamil" , "French", "German", "Spanish", "Other"])

    submitted = st.form_submit_button("Get Solution")
    
    if submitted :
        inputs={"problem":problem,
                "product_name":product_name,
                "product_nature":product_nature,
                "language":language
                }
        
        with st.spinner("Generating solution ..."):
            try:
                result=gs(inputs)
                st.success("✅ Solution:")
                st.write(result)
            except Exception as e:
                st.error(f"❌ Error: {e}") 