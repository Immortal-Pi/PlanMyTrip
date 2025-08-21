
# AI Travel Planner

A lightweight, full-stack agent that builds personalized travel itineraries with live context (weather, activities, hotels, currency rates), calculates total trip costs, and returns a concise summary.
Frontend is a static HTML/JS chat; backend is FastAPI with an agentic workflow.

## Architecture
![Architecture](/assets/diagram.png)

## UI
![AI Travel Planner graph](/assets/demo.gif)

## Agent Tasks:

1. Real-time weather info – fetch current/forecast weather for destination & dates.
2. Attractions & activities – suggest sights, experiences, and local picks.
3. Hotel cost estimates – budget/mid/luxury nightly ranges and totals.
4. Currency conversion – convert budgets/quotes to the user’s currency.
5. Itinerary generation – day-by-day plan (travel, activities, meals).
6. Total expenses – roll-up of transport, stay, food, tickets, extras.
7. Trip summary – short, readable recap of the plan and key costs.



## Setup
prerequisites
- python 3.10+ 
install dependencies
```
uv pip install -r requirements.txt 
```
- environment variables 
get these API keys in .env file
```
AZURE_OPENAI_GPT_4O_TARGET_URI=
AZURE_OPENAI_GPT_4O_API_KEY=
AZURE_OPENAI_GPT_4O_API_VERSION=
AZURE_OPENAI_GPT_4O_API_ENDPOINT=
GROQ_API_KEY=
TAVILY_API_KEY=
LANGSMITH_API_KEY=
VANTAGE_API_KEY=
GPLACES_API_KEY=
FOURSQUARE_API_KEY=
OPENWEATHERMAP_API_KEY=
EXCHANGE_RATE_API_KEY=
LANGCHAIN_API_KEY=
```

## Run Locally

backend FastAPI
```
uvicorn main:app --reload --port 8000
```
Endpoint: POST /query

Request body: { "question": "Plan a trip to Goa for 5 days" }

Response: { "answer": "<markdown string>" }

## Frontend 

```
py -m http.server 5500
```
streamlit 
```
streamlit run streamlit_app.py
```


## Conclusion
This project delivers a lightweight, end-to-end AI Travel Planner that couples a FastAPI agent backend with a clean, static HTML chat frontend. It orchestrates modular tools for real-time weather, attractions, hotel cost ranges, currency conversion, and composes them into a day-by-day itinerary, total expenses, and a concise summary. The design emphasizes simplicity, modularity, and extensibility—you can swap providers, add tools, or change the UI without reworking the core flow. Future enhancements like streaming responses, markdown rendering, persistence, and auth can turn this prototype into a production-ready assistant.
