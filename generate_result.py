from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def generate_llm(query,context):
    # LLM model to generate the final result
    llm=init_chat_model("gpt-3.5-turbo")

    prompt=[{"role":"system",
             "content":"You are a Rag assistant helping in generating results based on the query and context"},
            {"role":"user",
             "content":f"""
                    Generate the response only based on the given query ad context
                    Query:{query}
                    Context:{context}
                instruction:
                -Do not generate the content which is not related to query and context
                -Do not mention about context and query in the result
                -Result should be in points
                -Result should be short and crisp

                """}]
    response=llm.invoke(prompt)
    return response.content
    