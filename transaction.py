import pydantic

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
