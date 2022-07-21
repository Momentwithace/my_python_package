import pickle
twitter_user = [
    {"user_name": "ace", "is_married": True, "Age": 45},
    {"user_name": "tman", "is_married": False, "Age": 45},
    {"user_name": "Joe", "is_married": False, "Age": 25}
]

pickled_object = pickle.dumps(twitter_user)
print(pickled_object)
print(type(twitter_user))