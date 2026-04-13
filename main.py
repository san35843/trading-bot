print("Bot Started")

price = 100
support = 95
resistance = 105

if price > resistance:
    print("SELL signal")
elif price < support:
    print("BUY signal")
else:
    print("NO TRADE")
