class Symbol:
    def __init__(self, symbol, base_asset, quote_asset):
        self.symbol = symbol
        self.base_asset = base_asset
        self.quote_asset = quote_asset

    def __str__(self):
        return f"The pair {self.symbol} has quote Asset {self.base_asset} and {self.quote_asset}"
