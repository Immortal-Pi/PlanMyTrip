from fastapi import FastAPI 
from pydantic import BaseModel 
from dotenv import load_dotenv 
from agent.agentic_workflow import Graphbuilder
from fastapi.responses import JSONResponse 
import os 

load_dotenv() 

app=FastAPI()


class QueryRequest(BaseModel):
    query:str 

@app.post('/query')
async def query_travel_agent(query:QueryRequest):
    """ 
    query from the user end
    """
    try:
        print(query)
        graph=Graphbuilder(model_provider='open_ai')
        react_app=graph()

        png_graph=react_app.get_graph().draw_mermaid_png()
        with open('my_graph.png','wb') as f:
            f.write(png_graph)
        print(f'Graph saved as my_graph.png in {os.getcwd()}')

        # Assuming request is a pydantic object like {question: 'your text'}
        messages={'messages':[query.question]}
        output=react_app.invoke(messages)

        # if result is dict with messages
        if isinstance(output,dict) and 'messages' in output:
            final_output=output['messages'][-1].content # Last AI response 

        else:
            final_output=str(output)
        return {'answer':final_output}
    except Exception as e:
        return JSONResponse(status_code=500,content={'error':str(e)})
    
