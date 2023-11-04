import argparse
from src.classes.TradingViewWatcher import TradingViewWatcher
from src.constants.TradingViewWatcherConstants import FileTypes, ScrollType


def main(args) -> None:
    watcher = TradingViewWatcher(args.file, FileTypes.JSON, ScrollType.MANUAL, int(args.idx))
    watcher.run()
    

if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-f", "--file", help="File with tickers to pipe into tradingview")
    argParser.add_argument("-i", "--idx", help="Ticker starting idx")
    args = argParser.parse_args()
    main(args)