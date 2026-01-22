'''from fastapi import FastAPI

# import routers
from backend.app.api import ingest, evaluate, history, simulate, risk

# import startup logic
from backend.app.core.startup import initialize_system


app = FastAPI(
    title="Map-Based Risk & Crisis Monitoring System",
    version="0.1.0"
)

app.include_router(ingest.router, prefix="/api")
app.include_router(evaluate.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(simulate.router, prefix="/api")
app.include_router(risk.router, prefix="/api")

@app.on_event("startup")
def startup_event():
    initialize_system()

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "System running"
    }'''

 from fastapi import FastAPI

# import routers (RELATIVE to backend/app)
from app.api import ingest, evaluate, history, simulate, risk

# import startup logic
from app.core.startup import initialize_system


app = FastAPI(
    title="Map-Based Risk & Crisis Monitoring System",
    version="0.1.0"
)

app.include_router(ingest.router, prefix="/api")
app.include_router(evaluate.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(simulate.router, prefix="/api")
app.include_router(risk.router, prefix="/api")


@app.on_event("startup")
def startup_event():
    initialize_system()


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "System running"
    }
   
