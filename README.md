# Griffin's Crypto Day Trading Bot

## Overview

This Python-based trading bot is designed for day trading cryptocurrencies. It utilizes various technical indicators such as SMAs, RSI, Bollinger Bands, and volume analysis to identify potential buy and sell opportunities. Data is fetched from the Binance API to execute strategies based on live market conditions.

**Note**: This project is still under development, and much work remains to be done. A draft of the paper trading code is in place to test the bot without real risk.

## Features

- **RSI**: Determines overbought or oversold conditions to generate buy/sell signals.
- **SMAs**: Identifies trend reversals with confirmation to generate buy/sell signals.
- **Bollinger Bands**: 
  - Detects breakouts and consolidations using standard deviations from a moving average.
- **Volume Analysis**: Confirms buy/sell signals with volume thresholds.
- **Customizable Parameters**: Easily adjust thresholds for Bollinger Bands, volume analysis, and moving averages.
- **Buy/Sell Signal Generation**: Generates actionable signals based on specific market conditions.
- **Paper Trading**: Test the bot without real financial risk.

## Installation

1. Clone the repository:

   ```bash
   git clone
   cd trading-bot
   ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your API keys:
    - Create a file named api_keys.py in the project directory.
    - Add the following content to api_keys.py:
    ```python
    API_KEY = 'your_api_key'
    API_SECRET = 'your_api_secret'
    ```
    - Ensure api_keys.py is added to your .gitignore file to protect sensitive data.

## Usage

1. Run the bot:
    ```bash
    python main.py
    ```

2. The bot will fetch market data from Binance and generate buy/sell signals based on:
    - **RSI**: Overbought (sell) or oversold (buy) conditions.
    - **SMAs**: Buy signal on upward cross and sell signal on downward cross.
    - **Bollinger Band breakouts**.
    - **Volume thresholds** for confirmation.

3. **Paper Trading**: To test the bot without real financial risk, run the paper trading code draft.

## Key Strategies

### RSI (Relative Strength Index)

- **Buy signal**: When the RSI is below 30 (oversold condition).
- **Sell signal**: When the RSI is above 70 (overbought condition).

### SMAs (Simple Moving Averages)

- **Buy signal**: When the last two candles are both green (gain at close) and above the SMA.
- **Sell signal**: When the last two candles are both red (loss at close) and below the SMA.

### Bollinger Bands

- **Buy signal**: Breakout above the upper Bollinger Band with significant volume.
- **Sell signal**: Breakdown below the lower Bollinger Band with significant volume.

### Volume Analysis

- Confirms breakouts with:
    - Current candle volume exceeding a percentage threshold of its moving average.

## Dependencies

- Python 3.7+
- pandas
- numpy
- ta (Technical Analysis Library)
- requests (for API calls)

Install dependencies with:
```bash
pip install pandas numpy ta requests
```

## Notes

- Ensure you have a valid Binance API key and secret.
- Always test your strategies in a simulated environment before live trading.

## Disclaimer
This bot is for educational purposes only. Use it at your own risk. Trading cryptocurrencies involves significant risk and may result in financial loss.