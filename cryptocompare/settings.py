#!/usr/bin/env python
# encoding: utf-8

# CryptoCompare API client settings
API_PROTOCOL = 'https'
API_HOST = 'min-api.cryptocompare.com'
API_PATH_DATA = 'data'
API_PATH_STATS = 'stats'

# CryptoCompare API resources
# Price
PRICE_SINGLE_SYMBOL = 'single_symbol_price'
PRICE_MULTIPLE_SYMBOL = 'multiple_symbol_price'
PRICE_MULTIPLE_SYMBOLS_FULL_DATA = 'multiple_symbols_full_data'
PRICE_GENERATE_CUSTOM_AVERAGE = 'generate_custom_average'
# Historical data
HISTORICAL_DATA_DAILY_OHLCV = 'historical_daily_OHLCV'
HISTORICAL_DATA_HOURLY_OHLCV = 'historical_hourly_OHLCV'
HISTORICAL_DATA_MINUTE_OHLCV = 'historical_minute_OHLCV'
HISTORICAL_DATA_DAY_OHLCV_TIMESTAMP = 'historical_day_OHLCV_for_a_timestamp'
HISTORICAL_DATA_DAY_AVG_PRICE = 'historical_day_average_price'
HISTORICAL_DATA_DAILY_EXCHANGE_VOL = 'historical_daily_exchange_volume'
HISTORICAL_DATA_HOURLY_EXCHANGE_VOL = 'historical_hourly_exchange_volume'
# Pair mappings
PAIR_MAPPING_LATEST_FROM_SYM = 'latest_mapping_from_symbol'
PAIR_MAPPING_LATEST_EXCHANGE = 'latest_mapping_exchange'
PAIR_MAPPING_LATEST_EXCHANGE_FROM_SYM = 'latest_mapping_exchange_from_symbol'
PAIR_MAPPING_PLANNED_UPDATES = 'planned_pair_mapping_updates'
# Toplist
TOPLIST_BY_24H_VOL_FULL_DATA = 'toplist_by_24h_volume_full_data'
TOPLIST_BY_MARKET_CAP_FULL_DATA = 'toplist_by_market_cap_full_data'
TOPLIST_EXCHANGE_VOL_DATA_BY_PAIR = 'top_exchange_volume_data_by_pair'
TOPLIST_EXCHANGES_FULL_DATA_BY_PAIR = 'top_xchanges_full_data_by_pair'
TOPLIST_BY_PAIR_VOL = 'toplist_by_pair_volume'
TOPLIST_OF_TRADING_PAIRS = 'toplist_of_trading_pairs'
# Social data
SOCIAL_DATA_TOPLIST_OF_TRADING_PAIRS = 'latest_coin_social_stats_data'
SOCIAL_DATA_HISTORICAL_DAY_STATS = 'historical_day_social_stats_data'
SOCIAL_DATA_HISTORICAL_HOUR_STATS = 'historical_hour_social_stats_data'
# News
NEWS_LATEST_ARTICLES = 'latest_news_articles'
NEWS_LIST_FEEDS = 'list_news_feeds'
NEWS_ARTICLE_CATEGORIES = 'news_article_categories'
NEWS_LIST_FEEDS_AND_CATEGORIES = 'list_news_feeds_and_categories'
# Orderbook
ORDERBOOK_EXCHANGE_DATA = 'exchanges_with_orderbook_data'
ORDERBOOK_L1_TOP = 'orderbook_L1_top'
ORDERBOOK_L2_SNAPSHOT = 'orderbook_L2_snapshot'
# General info
GENERAL_INFO_RATE_LIMIT = 'rate_limit'
GENERAL_INFO_RATE_HOUR_LIMIT = 'rate_hour_limit'
GENERAL_INFO_ALL_EXCHANGES_AND_TRADING_PAIRS = 'all_the_exchanges_and_trading_pairs'
GENERAL_INFO_INSTRUMENT_CONSTITUENT_EXCHANGES = 'display_instrument_constituent_exchanges'
GENERAL_INFO_ALL_COINS = 'all_the_coins'
GENERAL_INFO_ALL_EXCHANGES = 'all_exchanges_general_info'
GENERAL_INFO_ALL_GAMBLING = 'all_gambling_general_info'
GENERAL_INFO_ALL_WALLETS = 'all_wallets_general_info'
GENERAL_INFO_ALL_CRYPTO_CARDS = 'all_crypto_cards_general_info'
GENERAL_INFO_ALL_MINING_CONTRACTS = 'all_mining_contracts_general_info'
GENERAL_INFO_ALL_MINING_COMPANIES = 'all_mining_companies_general_info'
GENERAL_INFO_ALL_MINING_EQUIPMENT = 'all_mining_equipment_general_info'
GENERAL_INFO_ALL_MINING_POOLS = 'all_mining_pools_general_info'
GENERAL_INFO_ALL_RECOMMENDED_ENTITIES = 'all_recommended_entities'
# Streaming
STREAMING_TOPLIST_BY_24H_VOL_SUBS = 'toplist_by _24h_volume_subscriptions'
STREAMING_TOPLIST_BY_MARKET_CAP_SUBS = 'toplist_by_market_cap_subscriptions'
STREAMING_SUBS_BY_PAIR = 'subs_by_pair'
STREAMING_SUBS_WATCHLIST = 'subs_watchlist'
STREAMING_COINS_GENERAL_INFO = 'coins_general_info'

# CryptoCompare API query parameters
ALL_DATA_PARAM = 'allData'
AGGREGATE_PARAM = 'aggregate'
AGGREGATE_PRED_TIME_PARAM = 'aggregatePredictableTimePeriods'
ASCENDING_PARAM = 'ascending'
AVERAGE_TYPE_PARAM = 'avgType'
BUILT_ON_PARAM = 'builtOn'
CALCULATION_TYPE_PARAM = 'calculationType'
CATEGORIES_EXCLUDE_PARAM = 'excludeCategories'
CATEGORIES_PARAM = 'categories'
COIN_ID_PARAM = 'coinId'
CRYPTO_SYMBOL_PARAM = 'fsym'
CRYPTOS_SYMBOL_PARAM = 'fsyms'
CURRENCY_SYMBOL_PARAM = 'tsym'
CURRENCIES_SYMBOL_PARAM = 'tsyms'
EXCHANGE_CRYPTO_SYM_PARAM = 'exchangeFsym'
EXCHANGE_PARAM = 'e'
EXTRA_PARAM = 'extraParams'
FEEDS_PARAM = 'feeds'
INSTRUMENT_PARAM = 'instrument'
LANGUAGE_PARAM = 'lang'
LIMIT_PARAM = 'limit'
PAGE_PARAM = 'page'
SIGN_PARAM = 'sign'
SORT_ORDER_PARAM = 'sortOrder'
TIMESTAMP_LESS_PARAM = 'lTs'
TIMESTAMP_PARAM = 'ts'
TIMESTAMP_TO_PARAM = 'toTs'
TOP_TIER_PARAM = 'topTier'
TRY_CONVERSION_PARAM = 'tryConversion'
UTC_HOUR_DIFF_PARAM = 'UTCHourDiff'

# CryptoCompare API resources endpoints
API_ENDPOINTS = {
    PRICE_SINGLE_SYMBOL: {
        'caching': '10 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM
        ],
        'resource': 'price'
    },
    PRICE_MULTIPLE_SYMBOL: {
        'caching': '10 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM
        ],
        'resource': 'pricemulti'
    },
    PRICE_MULTIPLE_SYMBOLS_FULL_DATA: {
        'caching': '10 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM
        ],
        'resource': 'pricemultifull'
    },
    PRICE_GENERATE_CUSTOM_AVERAGE: {
        'caching': '10 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM
        ],
        'resource': 'generateAvg'
    },
    HISTORICAL_DATA_DAILY_OHLCV: {
        'caching': '610 seconds',
        'path': API_PATH_DATA,
        'params': [
            ALL_DATA_PARAM,
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'histoday'
    },
    HISTORICAL_DATA_HOURLY_OHLCV: {
        'caching': '610 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'histohour'
    },
    HISTORICAL_DATA_MINUTE_OHLCV: {
        'caching': '40 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'histominute'
    },
    HISTORICAL_DATA_DAY_OHLCV_TIMESTAMP: {
        'caching': '86400 seconds',
        'path': API_PATH_DATA,
        'params': [
            CALCULATION_TYPE_PARAM,
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TIMESTAMP_PARAM,
            TRY_CONVERSION_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM
        ],
        'resource': 'pricehistorical'
    },
    HISTORICAL_DATA_DAY_AVG_PRICE: {
        'caching': '610 seconds',
        'path': API_PATH_DATA,
        'params': [
            AVERAGE_TYPE_PARAM,
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM,
            TRY_CONVERSION_PARAM,
            UTC_HOUR_DIFF_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'dayAvg'
    },
    HISTORICAL_DATA_DAILY_EXCHANGE_VOL: {
        'caching': '610 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'exchange/histoday'
    },
    HISTORICAL_DATA_HOURLY_EXCHANGE_VOL: {
        'caching': '610 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'exchange/histohour'
    },
    PAIR_MAPPING_LATEST_FROM_SYM: {
        'caching': '3600 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'pair/mapping/fsym'
    },
    PAIR_MAPPING_LATEST_EXCHANGE: {
        'caching': '3600 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'pair/mapping/exchange'
    },
    PAIR_MAPPING_LATEST_EXCHANGE_FROM_SYM: {
        'caching': '3600 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXCHANGE_CRYPTO_SYM_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'pair/mapping/exchange/fsym'
    },
    PAIR_MAPPING_PLANNED_UPDATES: {
        'caching': '86400 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'pair/mapping/planned/updates'
    },
    TOPLIST_BY_24H_VOL_FULL_DATA: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            ASCENDING_PARAM,
            CURRENCY_SYMBOL_PARAM,
            LIMIT_PARAM,
            PAGE_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/totalvolfull'
    },
    TOPLIST_BY_MARKET_CAP_FULL_DATA: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            ASCENDING_PARAM,
            CURRENCY_SYMBOL_PARAM,
            LIMIT_PARAM,
            PAGE_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/mktcapfull'
    },
    TOPLIST_EXCHANGE_VOL_DATA_BY_PAIR: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/exchanges'
    },
    TOPLIST_EXCHANGES_FULL_DATA_BY_PAIR: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/exchanges/full'
    },
    TOPLIST_BY_PAIR_VOL: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/volumes'
    },
    TOPLIST_OF_TRADING_PAIRS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM
        ],
        'resource': 'top/pairs'
    },
    SOCIAL_DATA_TOPLIST_OF_TRADING_PAIRS: {
        'caching': '600 seconds',
        'path': API_PATH_DATA,
        'params': [
            COIN_ID_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'social/coin/latest'
    },
    SOCIAL_DATA_HISTORICAL_DAY_STATS: {
        'caching': '600 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            COIN_ID_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM
        ],
        'required': [],
        'resource': 'social/coin/histo/day'
    },
    SOCIAL_DATA_HISTORICAL_HOUR_STATS: {
        'caching': '600 seconds',
        'path': API_PATH_DATA,
        'params': [
            AGGREGATE_PARAM,
            AGGREGATE_PRED_TIME_PARAM,
            COIN_ID_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM,
            TIMESTAMP_TO_PARAM
        ],
        'required': [],
        'resource': 'social/coin/histo/hour'
    },
    NEWS_LATEST_ARTICLES: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CATEGORIES_EXCLUDE_PARAM,
            CATEGORIES_PARAM,
            EXTRA_PARAM,
            FEEDS_PARAM,
            LANGUAGE_PARAM,
            SIGN_PARAM,
            SORT_ORDER_PARAM,
            TIMESTAMP_LESS_PARAM
        ],
        'required': [],
        'resource': 'v2/news'
    },
    NEWS_LIST_FEEDS: {
        'caching': '86400 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'news/feeds'
    },
    NEWS_ARTICLE_CATEGORIES: {
        'caching': '86400 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'news/categories'
    },
    NEWS_LIST_FEEDS_AND_CATEGORIES: {
        'caching': '86400 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'news/feedsandcategories'
    },
    ORDERBOOK_EXCHANGE_DATA: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'ob/l2/exchanges'
    },
    ORDERBOOK_L1_TOP: {
        'caching': '30 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM
        ],
        'resource': 'ob/l1/top'
    },
    ORDERBOOK_L2_SNAPSHOT: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            LIMIT_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'ob/l2/snapshot'
    },
    GENERAL_INFO_RATE_LIMIT: {
        'caching': '0 seconds',
        'path': API_PATH_STATS,
        'params': [],
        'required': [],
        'resource': 'rate/limit'
    },
    GENERAL_INFO_RATE_HOUR_LIMIT: {
        'caching': '0 seconds',
        'path': API_PATH_STATS,
        'params': [],
        'required': [],
        'resource': 'rate/hour/limit'
    },
    GENERAL_INFO_ALL_EXCHANGES_AND_TRADING_PAIRS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            EXCHANGE_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM,
            TOP_TIER_PARAM
        ],
        'required': [],
        'resource': 'v3/all/exchanges'
    },
    GENERAL_INFO_INSTRUMENT_CONSTITUENT_EXCHANGES: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            INSTRUMENT_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'all/includedexchanges'
    },
    GENERAL_INFO_ALL_COINS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            BUILT_ON_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'all/coinlist'
    },
    GENERAL_INFO_ALL_EXCHANGES: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'exchanges/general'
    },
    GENERAL_INFO_ALL_GAMBLING: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'gambling/general'
    },
    GENERAL_INFO_ALL_WALLETS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'wallets/general'
    },
    GENERAL_INFO_ALL_CRYPTO_CARDS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'cards/general'
    },
    GENERAL_INFO_ALL_MINING_CONTRACTS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'mining/contracts/general'
    },
    GENERAL_INFO_ALL_MINING_COMPANIES: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'mining/companies/general'
    },
    GENERAL_INFO_ALL_MINING_EQUIPMENT: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'mining/equipment/general'
    },
    GENERAL_INFO_ALL_MINING_POOLS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'mining/pools/general'
    },
    GENERAL_INFO_ALL_RECOMMENDED_ENTITIES: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [],
        'resource': 'recommended/all'
    },
    STREAMING_TOPLIST_BY_24H_VOL_SUBS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            ASCENDING_PARAM,
            CURRENCY_SYMBOL_PARAM,
            LIMIT_PARAM,
            PAGE_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/totalvol'
    },
    STREAMING_TOPLIST_BY_MARKET_CAP_SUBS: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            ASCENDING_PARAM,
            CURRENCY_SYMBOL_PARAM,
            LIMIT_PARAM,
            PAGE_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'top/mktcap'
    },
    STREAMING_SUBS_BY_PAIR: {
        'caching': '10 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTO_SYMBOL_PARAM,
            CURRENCIES_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTO_SYMBOL_PARAM
        ],
        'resource': 'subs'
    },
    STREAMING_SUBS_WATCHLIST: {
        'caching': '60 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'subsWatchlist'
    },
    STREAMING_COINS_GENERAL_INFO: {
        'caching': '120 seconds',
        'path': API_PATH_DATA,
        'params': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM,
            EXTRA_PARAM,
            SIGN_PARAM
        ],
        'required': [
            CRYPTOS_SYMBOL_PARAM,
            CURRENCY_SYMBOL_PARAM
        ],
        'resource': 'coin/generalinfo'
    }
}
