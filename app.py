from fastapi import FastAPI, Form

app = FastAPI()

@app.post('/openapi/jd')
@app.get('/openapi/jd')
async def jd(job_title: str = Form(...), vacancy: str = Form(...), gender: str = Form(...), job_experience: str = Form(...)):
    # Here, we use the decorator @Form to parse the form data from the request.

    # Print the values just for debugging purposes (you can remove this if you don't need it).
    print(job_title, job_experience, vacancy, gender)

    # You can perform any processing logic here if required.
    # For now, we'll simply return "Hello, World!" as the response.
    return {'Job Title':job_title,"Job Experience":job_experience,"Vacancy":vacancy,"Gender":gender}
