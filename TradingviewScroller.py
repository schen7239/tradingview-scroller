from classes.TradingViewWatcher import TradingViewWatcher
from constants.TradingViewWatcherConstants import FileTypes, ScrollType

watcher = TradingViewWatcher("./holdings/nasdaq_100.json", FileTypes.JSON, ScrollType.MANUAL)

watcher.run(0)