
import os

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "chats.txt"), "r") as data:
        fs = data.readlines()
        users = {}
        for message in fs:
            if message.strip():
                user = message[message.find("<")+1:message.find(">")]
                user_count = users.setdefault(user,0)
                user_count +=1
                users[user] = user_count
        users = sorted(users.items(), key=lambda x:x[1], reverse=True)
        print(users[0:3])

        