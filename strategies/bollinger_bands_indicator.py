import pandas as pd
from ta.volatility import BollingerBands

def generate_bollinger_signals(bars):
    # Configuration
    bollinger_period = 20
    bollinger_multiplier = 2
    volume_threshold = 1.5

    # Convert bars to DataFrame
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

     # Ensure there's enough data
    if len(df) < 21:  # Need at least 20 periods for the BB calculation
        return 'neutral'
    
    # Calculate Bollinger Bands
    bollinger = BollingerBands(close=df['close'], window=bollinger_period, window_dev=bollinger_multiplier)
    df['bb_mavg'] = bollinger.bollinger_mavg()  # Middle Band (Moving Average)
    df['bb_upper'] = bollinger.bollinger_hband()  # Upper Band (Moving Resistance)
    df['bb_lower'] = bollinger.bollinger_lband()  # Lower Band (Moving Support)
    
    # Latest candles
    current_candle = df.iloc[-1]
    prev_candle = df.iloc[-2]

    # Check for breakouts
    if current_candle['close'] > current_candle['bb_upper']:
        # Price breaks above the upper band here -> check for high generalized volume
        # If current volume is higher than (average volume * threshold)
        if current_candle['volume'] > (volume_threshold * current_candle['volume_ma']):
            return 'buy'
    elif current_candle['close'] < current_candle['bb_lower']:
        # Price breaks below the lower band here -> check for high generalized volume
        if current_candle['volume'] > (volume_threshold * current_candle['volume_ma']):
            return 'sell'