import json
from collections import OrderedDict
import pprint

with open('direct-messages.js',encoding="utf-8_sig") as f:

    df = json.load(f)

s = len(df)
txt = []
print(s)
for i in range(1, s):
    for j in range(0,len(df[i]["dmConversation"]["messages"])):
        if df[i]["dmConversation"]["messages"][j]["messageCreate"]["senderId"] == "012345678910" or df[i]["dmConversation"]["messages"][j]["messageCreate"]["senderId"] == "109876543210":
            txt.append(df[i]["dmConversation"]["messages"][j]["messageCreate"]["text"])
            print(df[i]["dmConversation"]["messages"][j]["messageCreate"]["text"])

txt.reverse()
d = "\n".join(txt)

with open("DM.txt", mode='w',encoding="utf-8_sig") as f:
    f.write(d)