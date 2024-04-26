from fastapi import FastAPI
import pydantic
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import uuid

from datetime import datetime

FRAUD_AMOUNT_THRESHOLD = 5000  # NZD
FRAUD_FREQUENCY_THRESHOLD = 10  # more than this per minute is suspicious

def connect():
    database =  psycopg2.connect(
    database="postgres",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
)
    database.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    return database

class TransactionData(pydantic.BaseModel):
    payerId: str
    merchantId: str
    callbackUrl: str
    amount: float
    currency: str
    description: str
    merchantUrl: str
    merchantOrderId: str
    userAgent: str
    userIpAddress: str
    status: str
    merchantIdCode: int
    bankId: str
    transactionType: str

app = FastAPI()

@app.get("/")
async def transactions():
    with connect().cursor() as cursor:
        cursor.execute("select * from transactions;")
        return cursor.fetchall()

@app.post("/")
async def root(transactionData: TransactionData):
    transactionId = uuid.uuid4()
    if FRAUD_AMOUNT_THRESHOLD <= transactionData.amount:
        transactionData.status = "PENDING REVIEW"
    else:
        # fetch transactions within last minute
        # count number
        # arouse suspicion if over threshold
        pass
    with connect().cursor() as cursor:
        cursor.execute(f"""
                       insert into transactions (
                       transactionId,
                       transactionTime,
                       payerId,
                       merchantId,
                       callbackUrl,
                       amount,
                       currency,
                       description,
                       merchantUrl,
                       merchantOrderId,
                       userAgent,
                       userIpAddress,
                       status,
                       merchantIdCode,
                       bankId,
                       transactionType
                       )
                       values
                       (
                       '{transactionId}',
                       '{datetime.now()}',
                       '{transactionData.payerId}',
                       '{transactionData.merchantId}',
                       '{transactionData.callbackUrl}',
                       {transactionData.amount},
                       '{transactionData.currency}',
                       '{transactionData.description}',
                       '{transactionData.merchantUrl}',
                       '{transactionData.merchantOrderId}',
                       '{transactionData.userAgent}',
                       '{transactionData.userIpAddress}',
                       '{transactionData.status}',
                       '{transactionData.merchantIdCode}',
                       '{transactionData.bankId}',
                       '{transactionData.transactionType}'
                       );""")
    return {"result": transactionData.status}
