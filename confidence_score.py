
def calculate_confidence(signal):
    return (
        0.4 * signal.get("model_accuracy", 0.5) +
        0.3 * signal.get("recent_success_rate", 0.5) +
        0.2 * (1 - signal.get("volatility_adjustment", 0.1)) +
        0.1 * signal.get("regime_filter", 1.0)
    )
