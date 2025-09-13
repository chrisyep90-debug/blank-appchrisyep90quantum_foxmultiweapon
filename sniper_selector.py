
def calc_quantum_score(data):
    return data.get("forecast", 0) * data.get("confidence", 0)

def select_top_trades(signals):
    scored = [(ticker, calc_quantum_score(data)) for ticker, data in signals.items()]
    top3 = sorted(scored, key=lambda x: x[1], reverse=True)[:3]
    return top3
