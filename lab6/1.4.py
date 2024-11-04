programming_keys = {
    10.75 : "FB",
    37.2  : "HPQ",
    45.23 : "ACME",
    205.55 : "IBM",
    612.78 :  "AAPL"
}
sort_items = sorted (programming_keys)
for price, key in programming_keys.items():
    print (f" {price} {key}")