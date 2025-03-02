import pandas as pd
import datetime as dt
import lxml
ewr = pd.read_html(r'https://www.ewrinc.com/cotton/contentPublic/reports/stateReceipts.aspx')
table = ewr[3]
date = str(dt.datetime.today())[:10]
table.to_csv(path_or_buf=f'EWR-{date}.csv')
