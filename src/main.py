from fastapi import FastAPI
from vrouter.src.domain.models.vrouter import config_Router
from vrouter.src.adapters.in_process.vrouter_api import router as vr_router
import uvicorn

app = FastAPI()

app.include_router(vr_router, prefix="/api")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

