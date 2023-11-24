from swedish_market_insights.inside_trades import InsideTradesAPI
from datetime import date

from_date = date(2023, 11, 20)
to_date = date(2023, 11, 24)

recent_inside_trades = InsideTradesAPI.get_trades_by_transaction_date(from_date, to_date)
recent_inside_trades = recent_inside_trades.sort_values(by='Issuer')
recent_inside_trades.to_csv('output.csv')

