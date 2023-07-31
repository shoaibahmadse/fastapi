from fastapi import FastAPI, Form
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

app = FastAPI()

@app.post('/openapi/jd')
@app.get('/openapi/jd')
async def jd(job_title: str = Form(...), vacancy: str = Form(...), gender: str = Form(...), job_experience: str = Form(...)):
    # Here, we use the decorator @Form to parse the form data from the request.

    # Print the values just for debugging purposes (you can remove this if you don't need it).
    print(job_title, job_experience, vacancy, gender)
    jd=job_description(job_title, job_experience, vacancy, gender)

    # You can perform any processing logic here if required.
    # For now, we'll simply return "Hello, World!" as the response.
    return {'Job Description':jd}


def job_description(job_title,vacancy,gender,exprience):
    llm = OpenAI(temperature=0, max_tokens=1000, openai_api_key="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")
    template = """i have vacancy of {vacancy} person for a job {job_title} which is a {gender} vanacy and required job exprience is {exprience}. Give me a proper description of this which include : Description of the job , Responsibilites, Requirements.Note: Does not include any of the additional text. 
                """
    prompt_template = PromptTemplate(input_variables=["job_title","vacancy","gender","exprience"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run({'job_title': job_title, 'vacancy': vacancy,'exprience':exprience,'gender':gender})
    return answer
