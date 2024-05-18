import statistics
from abc import ABC, abstractmethod


class ExchangeConnctionError(Exception):
    pass


class Exchange:
    def __init__(self):
        self.connected = False

    def connect(self) -> None:
        print("connecting to exchange")
        self.connected = True

    def check_connection(self) -> None:
        if not self.connected:
            ExchangeConnctionError()

    def get_market_data(self, symbol: str) -> list[float]:
        self.check_connection()

        price_data = {
            "BTC/USD": [100.01, 200.04, 400.00],
            "ETH/USD": [1.01, 2.04, 4.00],
        }
        return price_data[symbol]

    def buy(self, symbol: str, amount: float) -> None:
        self.check_connection()
        print(f"buying {amount} of {symbol}")

    def sell(self, symbol: str, amount: float) -> None:
        self.check_connection()
        print(f"selling {amount} of {symbol}")


# the man said you should split to 2 ABC, a tradingbuy and tradingsell strategy


class TradingStrategy(ABC):
    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool:
        pass

    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool:
        pass


class AverageTradingStrategy(TradingStrategy):
    def should_buy(self, prices: list[float]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[float]) -> bool:
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)


class MinMaxTradingStrategy(TradingStrategy):
    def should_buy(self, prices: list[float]) -> bool:
        return prices[-1] < 32000.0

    def should_sell(self, prices: list[float]) -> bool:
        return prices[-1] > 33000.0


class TradingBot:
    def __init__(self, exchange: Exchange, trading_strategy: TradingStrategy):
        self.exchange = exchange
        self.trading_strategy = trading_strategy

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)
        if should_buy:
            self.exchange.buy(symbol, 1)
        elif should_sell:
            self.exchange.sell(symbol, 1)
        else:
            print(f"no action for {symbol}")


def main():
    exchange = Exchange()
    exchange.connect()

    trading_strategy = MinMaxTradingStrategy()

    bot = TradingBot(exchange, trading_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()
