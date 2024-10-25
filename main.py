from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from fastapi_project.db import SessionLocal
from fastapi_project.gemini import GeminiClient
from fastapi_project.models import QueryResponse

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/query")
async def query_gemini(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    query = data.get("query")

    if not query:
        raise HTTPException(status_code=400, detail="Query is required")

    async def stream_response():
        response_text = ""
        try:
            async for chunk in GeminiClient.generate_content(query):
                response_text += chunk
                yield chunk

            db_query_response = QueryResponse(query=query, response=response_text)
            db.add(db_query_response)
            db.commit()
            db.refresh(db_query_response)

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return StreamingResponse(stream_response(), media_type="application/json")
