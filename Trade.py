from datetime import datetime
import config_binance as cfg
from binance.client import Client


class Trade:

    def __init__(self, symbol: str, id_bin: int, order_id: int, price: str, qty: str,
                 quote_qty: str, commission: str, commission_asset: str, time_trade: int, is_buyer: bool,
                 is_maker: bool, is_best_match: bool, id_trade: int = None):
        self.id_trade = id_trade
        self.symbol = symbol
        self.id_bin = id_bin
        self.order_id = order_id
        self.price = float(price)
        self.qty = float(qty)
        self.quote_qty = float(quote_qty)
        self.commission = float(commission)
        self.commission_asset = commission_asset
        self.time_trade = datetime.fromtimestamp(time_trade/1000)
        self.is_buyer = is_buyer
        self.is_maker = is_maker
        self.is_best_match = is_best_match

    def __str__(self):
        return f"symbol: {self.symbol}, id: {self.id_bin}, orderId: {self.order_id}, " \
               f"price: {self.price}, qty: {self.qty}, " \
               f"quoteQty: {self.quote_qty}, commission: {self.commission}, " \
               f"commissionAsset: {self.commission_asset}, time: {self.time_trade}, isBuyer: {self.is_buyer}, " \
               f"isMaker: {self.is_maker}, isBestMatch: {self.is_best_match}"
