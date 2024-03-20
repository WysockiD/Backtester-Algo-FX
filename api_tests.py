from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

from models.candle_timing import CandleTiming
from bot.trade_risk_calculator import get_trade_units
import constants.defs as defs

def lm(msg, pair):
    print(msg, pair)

if __name__ == '__main__':
    api = OandaApi()  
    # print(api.get_account_summary())  
    z = instrumentCollection.LoadInstruments("./data")
    print(z)

    print(api.fetch_candles("GBP_JPY", 10, "H1", "MBA"))

    print(api.get_account_instruments())

    # print(get_trade_units(api, "GBP_JPY", defs.BUY, 0.4, 60, lm))
    
