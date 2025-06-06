from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from prompt import *
load_dotenv()

def GetllmMOdel() :
    api_key = os.getenv("GEMINI_API_KEY")
    try :

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            temperature=0,
            api_key = api_key,
        )

        return llm
    except Exception as e :
        print("error" , str(e))
        return None


class ResumeParserAI :
    def __init__(self , content):
        self.model = GetllmMOdel()
        self.extractText =  content
        if self.model is None :
            return None

    async def Resumeaparser(self) :
        try :
            prompt = PromptTemplate.from_template(prompt_for_ai)
            response = self.model.invoke(prompt.format(texts = str(self.extractText) , output = str(example_output))).content
            return response
        
        except Exception as e :
            return f"An Error Occured {str(e)}"
        
    


