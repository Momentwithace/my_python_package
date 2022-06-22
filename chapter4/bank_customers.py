customers = [
         {
             "name": "Omomtola fashola",
             "acct_num": "001",
             "age": 24,
             "balance": 10_000,
             "type": "saving",
             "gender": "female",
             "is_married": False
         },
         {
             "name": "Tman Grace",
             "acct_num": "030",
             "age": 31,
             "balance": 100_000,
             "type": "saving",
             "gender": "female",
             "is_married": True
         },
         {
             "name": "David Tony",
             "acct_num": "031",
             "age": 27,
             "balance": 200_000,
             "type": "saving",
             "gender": "Male",
             "is_married": False
         },
         {
             "name": "John Ken",
             "acct_num": "032",
             "age": 26,
             "balance": 50_000,
             "type": "saving",
             "gender": "Male",
             "is_married": True
         },
         {
             "name": "Ace Black",
             "acct_num": "033",
             "age": 22,
             "balance": 500_000,
             "type": "saving",
             "gender": "female",
             "is_married": False
         },
         {
             "name": "Sandra Paul",
             "acct_num": "034",
             "age": 16,
             "balance": 60_000,
             "type": "saving",
             "gender": "female",
             "is_married": True
         },
         {
             "name": "Zeddy Ruth",
             "acct_num": "035",
             "age": 22,
             "balance": 30_000,
             "type": "saving",
             "gender": "Male",
             "is_married": False
         },
         {
             "name": "Precious Precious",
             "acct_num": "036",
             "age": 36,
             "balance": 500_000,
             "type": "saving",
             "gender": "Female",
             "is_married": True
         },
         {
             "name": "Elon Blessing",
             "acct_num": "037",
             "age": 24,
             "balance": 500_000,
             "type": "saving",
             "gender": "Male",
             "is_married": False
         }

     ]
print(len(customers))
name = [d["name"] for d in customers]
print(name)
names = [customer["name"] for customer in customers]
print(names)
account_balance = [customer["balance"] for customer in customers]
print(account_balance)
avg_age = sum(customer["age"] for customer in customers) / len(customers)
print(names)
print(avg_age)
savings_acct_balance = [dict(name=c["name"], balance=c["balance"])
                        for c in customers if c["type"] == "saving"
                        ]
print(name)
print(names)
print(savings_acct_balance)

def get_balance(dict_: dict) -> int:
    return dict_["balance"]


customers.sort(key=get_balance, reverse=True)

print(max(customers, key=get_balance))

print(min(customers, key=get_balance))

print(customers)