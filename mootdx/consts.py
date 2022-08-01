# 市场
MARKET_SZ = 0  # 深市
MARKET_SH = 1  # 沪市
MARKET_BJ = 2  # 北交

# K线种类
# 0 -   5 分钟K 线
KLINE_5MIN = 0
# 1 -   15 分钟K 线
KLINE_15MIN = 1
# 2 -   30 分钟K 线
KLINE_30MIN = 2
# 3 -   1 小时K 线
KLINE_1HOUR = 3
# 4 -   日K 线
KLINE_DAILY = 4
# 5 -   周K 线
KLINE_WEEKLY = 5
# 6 -   月K 线
KLINE_MONTHLY = 6
# 7 -   扩展市场 1 分钟
KLINE_EX_1MIN = 7
# 8 -   1 分钟K 线
KLINE_1MIN = 8
# 9 -   日K 线
KLINE_RI_K = 9
# 10 -  季K 线
KLINE_3MONTH = 10
# 11 -  年K 线
KLINE_YEARLY = 11

# 分笔行情最多2000条
MAX_TRANSACTION_COUNT = 2000

# K线数据最多800条
MAX_KLINE_COUNT = 800

FREQUENCY = ["5m", "15m", "30m", "1h", "day", "week", "mon", "ex_1m", "1m", "dk", "3mon", "year"]

# 板块相关参数
BLOCK_SZ = "block_zs.dat"
BLOCK_FG = "block_fg.dat"
BLOCK_GN = "block_gn.dat"
BLOCK_DEFAULT = "block.dat"

TYPE_FLATS = 0
TYPE_GROUP = 1

HQ_HOSTS = [
    ("上海双线主站1", "47.103.48.45", 7709),
    ("上海双线主站2", "47.103.86.229", 7709),
    ("上海双线主站3", "47.103.88.146", 7709),
    ("深圳双线主站1", "120.79.60.82", 7709),
    ("深圳双线主站2", "47.112.129.66", 7709),
    ("北京双线主站1", "39.98.234.173", 7709),
    ("北京双线主站2", "39.98.198.249", 7709),
    ("北京双线主站3", "39.100.68.59", 7709),
]

EX_HOSTS = [
    ("扩展市场深圳双线1", "112.74.214.43", 7727),
    ("扩展市场深圳双线2", "120.24.0.77", 7727),
    ("扩展市场深圳双线3", "47.107.75.159", 7727),
    ("扩展市场武汉主站1", "119.97.185.5", 7727),
    ("扩展市场武汉主站2", "202.103.36.71", 7727),
    ("扩展市场武汉主站3", "59.175.238.38", 7727),
    ("扩展市场北京双线0", "47.92.127.181", 7727),
    ("扩展市场上海双线0", "106.14.95.149", 7727),
    ("扩展市场新加双线0", "119.23.127.172", 7727),
]

GP_HOSTS = [
    ("默认财务数据线路", "120.76.152.87", 7709),
]

CONFIG = {
    "SERVER": {"HQ": HQ_HOSTS, "EX": EX_HOSTS, "GP": GP_HOSTS},
    "BESTIP": {"HQ": "", "EX": "", "GP": ""},
    "TDXDIR": "C:/new_tdx",
}


def return_last_value(retry_state):
    """return the result of the last call attempt"""
    return retry_state.outcome.result()


# 5MIN = 0
# 15MIN = 1
# 30MIN = 2
# 1HOUR = 3
# DAILY = 4
# WEEKLY = 5
# MONTHLY = 6
# EX_1MIN = 7
# 1MIN = 8
# RI_K = 9
# 3MONTH = 10
# YEARLY = 11
