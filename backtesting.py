import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-DOGE", count=100)

# 변동폭 * k 계산,(고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# target 매수가, range 컬럼을 한칸씩 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

print

df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("coinCrawlingData.xlsx")