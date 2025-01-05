import pandas as pd
from ta.momentum import RSIIndicator

def IndicateWithRSI(bars):
    # Configuration
    rsi_period = 14
    rsi_overbought = 70
    rsi_oversold = 30

    # Convert to DataFrame
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Calculate RSI
    rsi_indicator = RSIIndicator(close=df['close'], window=rsi_period)

    # Insert RSI into dataframe
    df['rsi'] = rsi_indicator.rsi()

    # Determine buy or sell signal
    latest_rsi = df['rsi'].iloc[-1]
    if latest_rsi > rsi_overbought:
        return 'buy'
    elif latest_rsi < rsi_oversold:
        return 'sell'
    else:
        return 'neutral'