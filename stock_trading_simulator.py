#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
股票交易模拟系统 (Stock Trading Simulation System)
一个简单的股票交易模拟程序
"""

import random
import time
from datetime import datetime
from typing import Dict, List, Optional


class Stock:
    """股票类"""
    
    def __init__(self, symbol: str, name: str, initial_price: float):
        self.symbol = symbol  # 股票代码
        self.name = name  # 股票名称
        self.current_price = initial_price  # 当前价格
        self.price_history = [initial_price]  # 价格历史
    
    def update_price(self):
        """模拟股价波动（随机波动 -5% 到 +5%）"""
        change_percent = random.uniform(-0.05, 0.05)
        self.current_price *= (1 + change_percent)
        self.current_price = round(self.current_price, 2)
        self.price_history.append(self.current_price)
    
    def __str__(self):
        return f"{self.symbol} - {self.name}: ¥{self.current_price:.2f}"


class Transaction:
    """交易记录类"""
    
    def __init__(self, transaction_type: str, stock: Stock, quantity: int, price: float):
        self.timestamp = datetime.now()
        self.type = transaction_type  # 'BUY' or 'SELL'
        self.stock_symbol = stock.symbol
        self.stock_name = stock.name
        self.quantity = quantity
        self.price = price
        self.total = quantity * price
    
    def __str__(self):
        type_text = "买入" if self.type == "BUY" else "卖出"
        return (f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] "
                f"{type_text} {self.stock_symbol} {self.quantity}股 "
                f"@¥{self.price:.2f} = ¥{self.total:.2f}")


class Portfolio:
    """投资组合类"""
    
    def __init__(self, initial_cash: float = 100000.0):
        self.cash = initial_cash  # 现金
        self.holdings: Dict[str, int] = {}  # 持仓 {股票代码: 数量}
        self.transactions: List[Transaction] = []  # 交易历史
    
    def buy_stock(self, stock: Stock, quantity: int) -> bool:
        """买入股票"""
        cost = stock.current_price * quantity
        if cost > self.cash:
            print(f"❌ 余额不足！需要 ¥{cost:.2f}，可用 ¥{self.cash:.2f}")
            return False
        
        self.cash -= cost
        self.holdings[stock.symbol] = self.holdings.get(stock.symbol, 0) + quantity
        transaction = Transaction("BUY", stock, quantity, stock.current_price)
        self.transactions.append(transaction)
        print(f"✅ 成功买入 {stock.symbol} {quantity}股，花费 ¥{cost:.2f}")
        return True
    
    def sell_stock(self, stock: Stock, quantity: int) -> bool:
        """卖出股票"""
        if stock.symbol not in self.holdings or self.holdings[stock.symbol] < quantity:
            current_holding = self.holdings.get(stock.symbol, 0)
            print(f"❌ 持仓不足！持有 {current_holding}股，想要卖出 {quantity}股")
            return False
        
        revenue = stock.current_price * quantity
        self.cash += revenue
        self.holdings[stock.symbol] -= quantity
        if self.holdings[stock.symbol] == 0:
            del self.holdings[stock.symbol]
        transaction = Transaction("SELL", stock, quantity, stock.current_price)
        self.transactions.append(transaction)
        print(f"✅ 成功卖出 {stock.symbol} {quantity}股，获得 ¥{revenue:.2f}")
        return True
    
    def get_holdings_value(self, stocks: Dict[str, Stock]) -> float:
        """计算持仓市值"""
        total_value = 0.0
        for symbol, quantity in self.holdings.items():
            if symbol in stocks:
                total_value += stocks[symbol].current_price * quantity
        return total_value
    
    def get_total_assets(self, stocks: Dict[str, Stock]) -> float:
        """计算总资产（现金 + 持仓市值）"""
        return self.cash + self.get_holdings_value(stocks)
    
    def display_portfolio(self, stocks: Dict[str, Stock]):
        """显示投资组合"""
        print("\n" + "="*60)
        print("📊 投资组合")
        print("="*60)
        print(f"💰 可用现金: ¥{self.cash:.2f}")
        print("\n📈 持仓明细:")
        if not self.holdings:
            print("  （暂无持仓）")
        else:
            total_value = 0.0
            for symbol, quantity in self.holdings.items():
                if symbol in stocks:
                    stock = stocks[symbol]
                    value = stock.current_price * quantity
                    total_value += value
                    print(f"  {symbol} - {stock.name}: {quantity}股 "
                          f"@¥{stock.current_price:.2f} = ¥{value:.2f}")
            print(f"\n  持仓总市值: ¥{total_value:.2f}")
        
        total_assets = self.get_total_assets(stocks)
        print(f"\n💎 总资产: ¥{total_assets:.2f}")
        print("="*60)


class StockMarket:
    """股票市场类"""
    
    def __init__(self):
        self.stocks: Dict[str, Stock] = {}
        self.is_running = False
    
    def add_stock(self, symbol: str, name: str, initial_price: float):
        """添加股票"""
        self.stocks[symbol] = Stock(symbol, name, initial_price)
    
    def update_all_prices(self):
        """更新所有股票价格"""
        for stock in self.stocks.values():
            stock.update_price()
    
    def display_market(self):
        """显示市场行情"""
        print("\n" + "="*60)
        print("📊 股票市场行情")
        print("="*60)
        for stock in self.stocks.values():
            if len(stock.price_history) >= 2:
                change = stock.current_price - stock.price_history[-2]
                change_percent = (change / stock.price_history[-2]) * 100
                change_symbol = "📈" if change >= 0 else "📉"
                print(f"{stock} {change_symbol} {change:+.2f} ({change_percent:+.2f}%)")
            else:
                print(f"{stock}")
        print("="*60)


class TradingSimulator:
    """交易模拟器主类"""
    
    def __init__(self):
        self.market = StockMarket()
        self.portfolio = Portfolio(initial_cash=100000.0)
        self.round_number = 0
        
        # 初始化一些示例股票
        self.market.add_stock("AAPL", "苹果公司", 180.50)
        self.market.add_stock("TSLA", "特斯拉", 245.30)
        self.market.add_stock("BABA", "阿里巴巴", 88.60)
        self.market.add_stock("TCEHY", "腾讯控股", 380.20)
        self.market.add_stock("MSFT", "微软", 378.90)
    
    def display_menu(self):
        """显示菜单"""
        print("\n" + "="*60)
        print("🎮 股票交易模拟系统")
        print("="*60)
        print("1. 查看市场行情")
        print("2. 查看我的投资组合")
        print("3. 买入股票")
        print("4. 卖出股票")
        print("5. 查看交易历史")
        print("6. 下一回合（时间推进，股价更新）")
        print("0. 退出系统")
        print("="*60)
    
    def view_market(self):
        """查看市场"""
        self.market.display_market()
    
    def view_portfolio(self):
        """查看投资组合"""
        self.portfolio.display_portfolio(self.market.stocks)
    
    def buy_stock_interactive(self):
        """交互式买入股票"""
        self.market.display_market()
        symbol = input("\n请输入股票代码（如 AAPL）: ").strip().upper()
        
        if symbol not in self.market.stocks:
            print(f"❌ 股票代码 {symbol} 不存在")
            return
        
        stock = self.market.stocks[symbol]
        try:
            quantity = int(input(f"请输入买入数量（当前价格 ¥{stock.current_price:.2f}）: "))
            if quantity <= 0:
                print("❌ 数量必须大于0")
                return
            self.portfolio.buy_stock(stock, quantity)
        except ValueError:
            print("❌ 请输入有效的数字")
    
    def sell_stock_interactive(self):
        """交互式卖出股票"""
        self.portfolio.display_portfolio(self.market.stocks)
        symbol = input("\n请输入股票代码（如 AAPL）: ").strip().upper()
        
        if symbol not in self.market.stocks:
            print(f"❌ 股票代码 {symbol} 不存在")
            return
        
        stock = self.market.stocks[symbol]
        try:
            quantity = int(input(f"请输入卖出数量（当前价格 ¥{stock.current_price:.2f}）: "))
            if quantity <= 0:
                print("❌ 数量必须大于0")
                return
            self.portfolio.sell_stock(stock, quantity)
        except ValueError:
            print("❌ 请输入有效的数字")
    
    def view_transactions(self):
        """查看交易历史"""
        print("\n" + "="*60)
        print("📜 交易历史")
        print("="*60)
        if not self.portfolio.transactions:
            print("（暂无交易记录）")
        else:
            for transaction in self.portfolio.transactions:
                print(transaction)
        print("="*60)
    
    def next_round(self):
        """下一回合"""
        self.round_number += 1
        print(f"\n⏰ 时间推进到第 {self.round_number} 回合...")
        self.market.update_all_prices()
        print("✅ 股票价格已更新")
        time.sleep(0.5)
        self.market.display_market()
    
    def run(self):
        """运行模拟器"""
        print("\n" + "🌟"*30)
        print("  欢迎使用股票交易模拟系统！")
        print("  初始资金: ¥100,000.00")
        print("🌟"*30)
        
        while True:
            self.display_menu()
            choice = input("\n请选择操作 (0-6): ").strip()
            
            if choice == "0":
                print("\n👋 感谢使用股票交易模拟系统！")
                final_assets = self.portfolio.get_total_assets(self.market.stocks)
                profit = final_assets - 100000.0
                profit_percent = (profit / 100000.0) * 100
                print(f"\n📊 最终统计:")
                print(f"  初始资金: ¥100,000.00")
                print(f"  最终资产: ¥{final_assets:.2f}")
                print(f"  盈亏: ¥{profit:+.2f} ({profit_percent:+.2f}%)")
                break
            elif choice == "1":
                self.view_market()
            elif choice == "2":
                self.view_portfolio()
            elif choice == "3":
                self.buy_stock_interactive()
            elif choice == "4":
                self.sell_stock_interactive()
            elif choice == "5":
                self.view_transactions()
            elif choice == "6":
                self.next_round()
            else:
                print("❌ 无效的选择，请重新输入")


def main():
    """主函数"""
    simulator = TradingSimulator()
    simulator.run()


if __name__ == "__main__":
    main()
