from fastapi import APIRouter
import pandas as pd
from app.services.scraper import scrape_and_save_csv

router = APIRouter()

@router.get("/dados")
def get_dados():
    try:
        df = pd.read_csv("dados.csv")
        return df.to_dict(orient="records")
    except Exception as e:
        return {"erro": str(e)}

@router.post("/scrape")
def run_scraper():
    try:
        resultado = scrape_and_save_csv()
        return {"mensagem": resultado}
    except Exception as e:
        return {"erro": str(e)}
