# Modified by CrisisAlpha-Lab, 2026-11-12: the Provider description names the public source repository
# (AGPL-3.0 section 13). Changed lines are marked 'CrisisAlpha-Lab'. Part of a modified version of
# openbb-cboe 1.6.1 (AGPL-3.0-only, (c) OpenBB Inc.). See LICENSE / NOTICE.
"""Cboe provider module."""

from openbb_cboe.models.available_indices import CboeAvailableIndicesFetcher
from openbb_cboe.models.equity_historical import CboeEquityHistoricalFetcher
from openbb_cboe.models.equity_quote import CboeEquityQuoteFetcher
from openbb_cboe.models.equity_search import CboeEquitySearchFetcher
from openbb_cboe.models.futures_curve import CboeFuturesCurveFetcher
from openbb_cboe.models.index_constituents import (
    CboeIndexConstituentsFetcher,
)
from openbb_cboe.models.index_historical import (
    CboeIndexHistoricalFetcher,
)
from openbb_cboe.models.index_search import CboeIndexSearchFetcher
from openbb_cboe.models.index_snapshots import CboeIndexSnapshotsFetcher
from openbb_cboe.models.options_chains import CboeOptionsChainsFetcher
from openbb_core.provider.abstract.provider import Provider

cboe_provider = Provider(
    name="cboe",
    website="https://www.cboe.com",
    # CrisisAlpha-Lab: name the public source repository (AGPL-3.0 section 13) in the provider description
    description="""Cboe is the world's go-to derivatives and exchange network,
delivering cutting-edge trading, clearing and investment solutions to people
around the world.
Modified by CrisisAlpha-Lab (AGPL-3.0-only). Corresponding source: https://github.com/CrisisAlpha-Lab/openbb-cboe-patched""",
    credentials=None,
    fetcher_dict={
        "AvailableIndices": CboeAvailableIndicesFetcher,
        "EquityHistorical": CboeEquityHistoricalFetcher,
        "EquityQuote": CboeEquityQuoteFetcher,
        "EquitySearch": CboeEquitySearchFetcher,
        "EtfHistorical": CboeEquityHistoricalFetcher,
        "IndexConstituents": CboeIndexConstituentsFetcher,
        "FuturesCurve": CboeFuturesCurveFetcher,
        "IndexHistorical": CboeIndexHistoricalFetcher,
        "IndexSearch": CboeIndexSearchFetcher,
        "IndexSnapshots": CboeIndexSnapshotsFetcher,
        "OptionsChains": CboeOptionsChainsFetcher,
    },
    repr_name="Chicago Board Options Exchange (CBOE)",
)
