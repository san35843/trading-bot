print("Trading Bot Started")

balance = 1000
risk_per_trade = 0.02

def calculate_lot(balance, risk):
    return balance * risk

lot = calculate_lot(balance, risk_per_trade)
print("Lot size:", lot)
