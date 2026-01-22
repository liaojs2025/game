# 股票交易模拟系统 / Stock Trading Simulation System

一个简单但功能完整的股票交易模拟程序，用于学习和练习股票交易。

A simple but fully functional stock trading simulation program for learning and practicing stock trading.

## 功能特性 / Features

- 📈 实时股价模拟（随机波动）/ Real-time stock price simulation (random fluctuations)
- 💰 投资组合管理 / Portfolio management
- 🛒 买入/卖出操作 / Buy/sell operations
- 📊 市场行情显示 / Market quotes display
- 📜 交易历史记录 / Transaction history
- 💎 资产统计分析 / Asset statistics and analysis

## 快速开始 / Quick Start

### 运行要求 / Requirements

- Python 3.6 或更高版本 / Python 3.6 or higher

### 运行程序 / Run the Program

```bash
# 直接运行 / Direct execution
python3 stock_trading_simulator.py

# 或使其可执行 / Or make it executable
chmod +x stock_trading_simulator.py
./stock_trading_simulator.py
```

## 使用说明 / Usage

系统启动后会显示主菜单，你可以：

After the system starts, a main menu will be displayed, where you can:

1. **查看市场行情** - 查看所有股票的当前价格和涨跌情况
2. **查看我的投资组合** - 查看现金余额、持仓和总资产
3. **买入股票** - 输入股票代码和数量进行买入
4. **卖出股票** - 输入股票代码和数量进行卖出
5. **查看交易历史** - 查看所有买卖记录
6. **下一回合** - 时间推进，所有股票价格会随机波动
0. **退出系统** - 退出并显示最终统计数据

## 示例股票 / Sample Stocks

系统预置了以下股票：

The system comes with the following stocks:

- AAPL - 苹果公司 / Apple Inc.
- TSLA - 特斯拉 / Tesla
- BABA - 阿里巴巴 / Alibaba
- TCEHY - 腾讯控股 / Tencent Holdings
- MSFT - 微软 / Microsoft

## 系统设计 / System Design

### 核心类 / Core Classes

- **Stock** - 股票类，管理单只股票的信息和价格
- **Transaction** - 交易记录类，记录每笔交易的详情
- **Portfolio** - 投资组合类，管理现金和持仓
- **StockMarket** - 股票市场类，管理所有股票
- **TradingSimulator** - 交易模拟器主类，控制整个系统

### 游戏规则 / Game Rules

- 初始资金：¥100,000.00
- 股价波动范围：每回合 -5% 到 +5%
- 交易没有手续费（简化模型）
- 不能做空（只能买入持有的股票）

## 扩展建议 / Extension Suggestions

可以添加的功能：

Features that can be added:

- 交易手续费和税费 / Trading fees and taxes
- 限价单和止损单 / Limit orders and stop-loss orders
- 更复杂的股价模拟模型 / More complex stock price simulation models
- K线图显示 / Candlestick chart display
- 技术指标（MA, RSI等）/ Technical indicators (MA, RSI, etc.)
- 保存/加载游戏进度 / Save/load game progress
- 多人对战模式 / Multiplayer battle mode

## 许可证 / License

MIT License
