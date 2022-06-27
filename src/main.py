import argparse

import pandas as pd
from senkalib.chain.bsc.bsc_transaction_generator import BscTransactionGenerator
from senkalib.senka_setting import SenkaSetting
from senkalib.token_original_id_table import TokenOriginalIdTable

from pancake_plugin.pancake_plugin import PancakePlugin

TOKEN_ORIGINAL_IDS_URL = "https://raw.githubusercontent.com/ca3-caaip/token_original_id/master/token_original_id.csv"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PancakeSwap plugin")
    parser.add_argument(
        "address",
        type=str,
        help="BSC address",
    )
    parser.add_argument(
        "bscscan_key",
        type=str,
        help="BSCScan API key",
    )
    address = parser.parse_args().address
    bscscan_key = parser.parse_args().bscscan_key
    caajs = []
    settings = SenkaSetting({"bscscan_key": bscscan_key})
    token_original_ids = TokenOriginalIdTable(TOKEN_ORIGINAL_IDS_URL)
    transactions = BscTransactionGenerator.get_transactions(
        {"settings": settings, "data": address}
    )

    for transaction in transactions:
        if PancakePlugin.can_handle(transaction):
            caaj_peace = PancakePlugin.get_caajs(
                address, transaction, token_original_ids
            )
            caajs.extend(caaj_peace)

    df = pd.DataFrame(caajs)
    df = df.sort_values("executed_at")
    caaj_csv = df.to_csv(None, index=False)
    print(caaj_csv)
