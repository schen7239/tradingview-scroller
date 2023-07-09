from tradingview_stock_scroller import TradingViewWatcher

watcher = TradingViewWatcher("./holdings/russell_2000.json", "JSON")

watcher.run(0)