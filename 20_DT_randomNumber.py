import random

for i in range(100):
    print(random.randrange(1, 100))

    """
    अगर Repeat नहीं चाहिए

तब random.sample() का उपयोग करें।

import random

    """

print("Random but  dont want re occurrence ... ")
for i in range(100):
    number = random.sample(range(1, 101), 100)

print(number)