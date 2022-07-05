account = {
     "name": "Ace black",
     "user name": "unlikeace",
     "sex": "male",
     "is_verified": True,
     "about": "gentle and honest",
     "followers": "1234",
     "followings": "32"
 }

print(account["name"])
print(account.get("followers"))
account["birthday"] = "Jan 1 1997"
print(account.get("birthday"))
print(account)