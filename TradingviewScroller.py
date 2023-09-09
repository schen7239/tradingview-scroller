from src.classes.TradingViewWatcher import TradingViewWatcher
from src.constants.TradingViewWatcherConstants import FileTypes, ScrollType

watcher = TradingViewWatcher("./holdings/russell_2000.json", FileTypes.JSON, ScrollType.MANUAL, 60)

watcher.run()