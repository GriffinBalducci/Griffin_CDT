# DEPRECATED CODE BELOW: DECIDED HA IS NOT A GOOD INDICATOR FOR MY TYPE OF TRADING

import pandas as pd

def calculate_heikin_ashi(bars):
     # Convert bars to a DataFrame
    bars_df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    bars_df['timestamp'] = pd.to_datetime(bars_df['timestamp'], unit='ms')

    # Initialize Heikin-Ashi columns
    ha_df = bars_df.copy()
    ha_df['HA_Open'] = 0.0
    ha_df['HA_Close'] = 0.0
    ha_df['HA_High'] = 0.0
    ha_df['HA_Low'] = 0.0

    # Calculate Heikin-Ashi Closings
    ha_df['HA_Close'] = (bars_df['open'] + bars_df['close'] + bars_df['high'] + bars_df['low'] ) / 4

    # Iterate through the Heikin-Ashi dataframe to calculate the rest of the Heikin-Ashi values
    for i in range(len(ha_df)):
        if i == 0:
            # Set initial HA_Open as the average of the first candle's open and close (Case: No previous candles)
            ha_df.at[i, 'HA_Open'] = (bars_df.iloc[i]['open'] + bars_df.iloc[i]['close']) / 2
        else:
            # HA_Open = (previous HA_Open + previous HA_Close) / 2
            ha_df.at[i, 'HA_Open'] = (ha_df.at[i - 1, 'HA_Open'] + ha_df.at[i - 1, 'HA_Close']) / 2

        # HA_High = max(high, HA_Open, HA_Close)
        # high represents highest value from original bars_df
        ha_df.at[i, 'HA_High'] = max(bars_df.iloc[i]['high'], ha_df.at[i, 'HA_Open'], ha_df.at[i, 'HA_Close'])

        # HA_Low = min(low, HA_Open, HA_Close)
        # low represents lowest value from original bars_df
        ha_df.at[i, 'HA_Low'] = min(bars_df.iloc[i]['low'], ha_df.at[i, 'HA_Open'], ha_df.at[i, 'HA_Close'])

    return ha_df

def generate_ha_signals(ha_df):
    # CONFIGURATION
    lower_wick_threshold = 0.1 # Higher threshold allows longer wicks
    upper_wick_threshold = 0.25

    # Get the last two Heikin-Ashi candles
    current_candle = ha_df.iloc[-1]
    prev_candle = ha_df.iloc[-2]

    # Determine ranges
    current_range = current_candle['HA_high'] - current_candle['HA_low']
    prev_range = prev_candle['HA_High'] - prev_candle['HA_Low']

    # Check for green candle (Check for buying)
    if (current_candle['HA_close'] > current_candle['HA_open']):
        # Check for little to no bottom wick (Indicates low selling) and moderate upper wick (Indicates buying pressure)
        if (((current_candle['HA_Open'] - current_candle['HA_low']) / current_range) < lower_wick_threshold) \
            and (((current_candle['HA_high'] - current_candle['HA_Close']) / current_range) > upper_wick_threshold):
            # Confirm with previous candle
            if (((prev_candle['HA_Open'] - prev_candle['HA_low']) / prev_range) < lower_wick_threshold) \
            and (((prev_candle['HA_high'] - prev_candle['HA_Close']) / prev_range) > upper_wick_threshold):
                return 'buy'
        
        return 'neutral'
            
    # Check for selling
    #else:
        # Check if little to no top wick or large bottom wick