import pandas as pd

def generate_sma_signals(bars):
    # Configuration
    sma_period = 14

    # Convert bars to DataFrame
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Calculate the SMA (Simple Moving Average)
    df['SMA'] = df['close'].rolling(window=sma_period).mean()

    # Check if the last two candles are both green and above the SMA
    if len(df) < 2:  # Ensure there's enough data
        return None

    # Last two candles
    last_candle = df.iloc[-1]
    prev_candle = df.iloc[-2]

    # Conditions:

    # Buy Check:
    # Green candles (Gain at close)
    if (last_candle['close'] > last_candle['open']) and (prev_candle['close'] > prev_candle['open']):  
        # Reversal with confirmation
        if (last_candle['close'] > last_candle['SMA']) and (prev_candle['close'] > prev_candle['SMA']): 
            return 'buy'
        else:
            return 'neutral'
    
    # Sell Check:
    # Red candles (Loss at close)
    if (last_candle['close'] < last_candle['open']) and (prev_candle['close'] < prev_candle['open']):  
        # Weakness with validation
        if (last_candle['close'] <= last_candle['SMA']) and (prev_candle['close'] <= prev_candle['SMA']): 
            return 'sell'
        else:
            return 'neutral'