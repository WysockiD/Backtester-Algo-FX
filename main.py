from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection

if __name__ == '__main__':
    api = OandaApi()    
    s = instrumentCollection.LoadInstruments("./data")
    print(s)
    
    