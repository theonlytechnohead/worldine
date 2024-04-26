import requests

data = {
  "payerId": "0220100894",
  "merchantId": "e53519b4-460f-4687-8133-4c9b95209331",
  "callbackUrl": "http://paymark.co.nz/hobsonTakeaway",
  "amount": 6750,
  "currency": "NZD",
  "description": "RIGHTO",
  "merchantUrl": "www.paymark.co.nz",
  "merchantOrderId": "111123",
  "userAgent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US)",
  "userIpAddress": "127.0.0.1",
  "status": "NEW",
  "merchantIdCode": 300000114,
  "bankId": "ASB",
  "transactionType": "REGULAR"
}

response = requests.post(
    "http://localhost:8000/",
    json=data
)
print(response.text)