# Power2UP API

##Install
___
**pip install py_pr2up**

##Docs
___
###Functions

**get_services()** - get services

Return JSON object
```json
{
    "service": 1,
    "name": "Живые Подписчики Ру",
    "type": "subscribe",
    "category": "Russian profiles. Adds views and small activity.",
    "rate": "100.00",
    "min": 10,
    "max": 15000,
    "refill": false
}
```

**create_order(service_id, link, quantity)** - Create order

+ service_id - service id
+ link - post url
+ quantity - count

Return JSON object
```json
{
  "order": 1
}
```

**check_status(order_id)**  - check_status

+ order_id - order id

Return JSON object
```json
{
  "charge": "0.27819",
  "start_count": "3572",
  "status": "Partial",
  "remains": "157",
  "currency": "USD"
}
```

**create_refill(order_id)** - Create Refill

+ order_id - order id

Return JSON object
```json
{
  "refill": 1
}
```

**get_balance()** - get balance

Return JSON object
```json
{
  "balance": "99.80",
  "currency": "USD"
}
```

**cancel_order(order_id)** - Cancel order

+ order_id - your order id

Return JSON object
```json
{
  "ok": "true"
}
```

---
####In case of an error, it will return a JSON response:
```json
{
  "error": "Error Example"
}
```

###Example
___
```python
from pr2up import Power2Up

pr2up = Power2Up("API_TOKEN")

order = pr2up.get_services()

for i in order:
    print(i)
```
##Plans
___
✅ Create Project

✅ Developing sync API

🔲 Developing async API
##Author
___
Developed by GFNPRO

Telegram - https://t.me/gfnpro
