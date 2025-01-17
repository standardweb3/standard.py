import pytest
import pytest_asyncio
from standardweb3 import StandardClient
from standardweb3.types.orderbook import Orderbook
from standardweb3.types.orderhistory import AccountOrderHistory
from standardweb3.types.order import AccountOrders
from standardweb3.types.pair import Pair, PairData
from standardweb3.types.token import TokenData, TokenInfo
from standardweb3.types.tradehistory import AccountTradeHistory
from standardweb3.types.trade import TradesData
import os


@pytest_asyncio.fixture
async def client():
    return StandardClient(
        private_key=os.getenv("PRIVATE_KEY", ""),
        http_rpc_url="https://your_rpc_url",
        networkName="Story Odyssey Testnet",
        api_key=os.getenv("ADMIN_API_KEY", ""),
    )


@pytest.mark.asyncio
async def test_fetch_orderbook(client):
    orderbook = await client.fetch_orderbook(
        base="0xe8CabF9d1FFB6CE23cF0a86641849543ec7BD7d5",
        quote="0x40fCa9cB1AB15eD9B5bDA19A52ac00A78AE08e1D",
    )
    assert isinstance(orderbook, Orderbook)


@pytest.mark.asyncio
async def test_fetch_account_order_history_paginated_with_limit(client):
    order_history = await client.fetch_account_order_history_paginated_with_limit(
        address=os.getenv("ADDRESS", ""), limit=10, page=1
    )
    assert isinstance(order_history, AccountOrderHistory)


@pytest.mark.asyncio
async def test_fetch_account_orders_paginated_with_limit(client):
    account_orders = await client.fetch_account_orders_paginated_with_limit(
        address=os.getenv("ADDRESS", ""), limit=10, page=1
    )
    assert isinstance(account_orders, AccountOrders)


@pytest.mark.asyncio
async def test_fetch_all_pairs(client):
    all_pairs = await client.fetch_all_pairs(limit=10, page=1)
    assert isinstance(all_pairs, PairData)


@pytest.mark.asyncio
async def test_fetch_new_listing_pairs(client):
    new_listing_pairs = await client.fetch_new_listing_pairs(limit=10, page=1)
    assert isinstance(new_listing_pairs, PairData)


@pytest.mark.asyncio
async def test_fetch_pair_info(client):
    pair_info = await client.fetch_pair_info(
        base="0xe8CabF9d1FFB6CE23cF0a86641849543ec7BD7d5",
        quote="0x40fCa9cB1AB15eD9B5bDA19A52ac00A78AE08e1D",
    )
    assert isinstance(pair_info, Pair)


@pytest.mark.asyncio
async def test_fetch_top_gainer_pairs(client):
    top_gainer_pairs = await client.fetch_top_gainer_pairs(limit=10, page=1)
    assert isinstance(top_gainer_pairs, PairData)


@pytest.mark.asyncio
async def test_fetch_top_loser_pairs(client):
    top_loser_pairs = await client.fetch_top_loser_pairs(limit=10, page=1)
    assert isinstance(top_loser_pairs, PairData)


@pytest.mark.asyncio
async def test_fetch_all_tokens(client):
    all_tokens = await client.fetch_all_tokens(limit=10, page=1)
    assert isinstance(all_tokens, TokenData)


@pytest.mark.asyncio
async def test_fetch_new_listing_tokens(client):
    new_listing_tokens = await client.fetch_new_listing_tokens(limit=10, page=1)
    assert isinstance(new_listing_tokens, TokenData)


@pytest.mark.asyncio
async def test_fetch_token_info(client):
    token_info = await client.fetch_token_info(
        address="0x40fCa9cB1AB15eD9B5bDA19A52ac00A78AE08e1D"
    )
    assert isinstance(token_info, TokenInfo)


@pytest.mark.asyncio
async def test_fetch_account_trade_history_paginated_with_limit(client):
    trade_history = await client.fetch_account_trade_history_paginated_with_limit(
        address=os.getenv("ADDRESS", ""), limit=10, page=1
    )
    assert isinstance(trade_history, AccountTradeHistory)


@pytest.mark.asyncio
async def test_fetch_recent_overall_trades_paginated(client):
    recent_overall_trades = await client.fetch_recent_overall_trades_paginated(
        limit=10, page=1
    )
    assert isinstance(recent_overall_trades, TradesData)


@pytest.mark.asyncio
async def test_fetch_recent_pair_trades_paginated(client):
    recent_pair_trades = await client.fetch_recent_pair_trades_paginated(
        base="0xe8CabF9d1FFB6CE23cF0a86641849543ec7BD7d5",
        quote="0x40fCa9cB1AB15eD9B5bDA19A52ac00A78AE08e1D",
        limit=10,
        page=1,
    )
    assert isinstance(recent_pair_trades, TradesData)
