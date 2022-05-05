import sys
import json


inp = """2 3
{"offers": [{"offer_id": "offer1", "market_sku": 10846332, "price": 1490}, {"offer_id": "offer2", "market_sku": 682644, "price": 499}]}
{"offers": [{"offer_id": "offer3", "market_sku": 832784, "price": 14000}, {"offer_id": "offer4", "market_sku": 3234, "price": 100}]}
"""

i = 1
n = None
m = None
rfeed = []
is_feed_full = False
for line in inp.splitlines():
    if not is_feed_full:
        if i == 1:
            _, m = line.split()
            m = int(m)
        else:
            offers = json.loads(line)["offers"]
            for offer in offers:
                if len(rfeed) < m:
                    rfeed.append(offer)
                else:
                    is_feed_full = True
                    break
        i += 1
    else:
        break

result = json.dumps({"offers": rfeed})
print(result)
