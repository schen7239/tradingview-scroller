from tradingview_stock_scroller import TradingViewWatcher

watcher = TradingViewWatcher("./holdings/nasdaq_100.json", "JSON")

watcher.run(60)