#Yfinance kütüphanesini indirme işlemi
pip install yfinance

#Gerekli kütüphanelerim import işlemi
import pandas as pd
import yfinance as yf

# Bir hisse senedinin tüm zamanlarına ait bilgilerine erişmek
yf.download("GARAN.IS")

# Bir hisse senedinin belirli bir zamandan itibaren olan bilgilerine erişmek
yf.download("GARAN.IS", start="2010-01-01")

# Bir hisse senedinin belirli bir zamana kadar olan bilgilerine erişmek
yf.download("GARAN.IS", end="2018-01-01")

# Bir hisse senedinin belirli bir zaman aralığındaki bilgilerine erişmek
yf.download("GARAN.IS", start="2012-01-01", end="2018-01-01")

# İşlemleri fonksiyonlaştırmak
def dataImporter(symbol="", date='2017-01-01', inBist=True):
    if inBist:
        symbol = symbol + ".IS"
        df = yf.download(symbol,
                         start=date,
                         progress=False)

    else:
        df = yf.download(symbol,
                         start=date,
                         progress=False)
    return df

dataImporter("AMZN", inBist=False)
