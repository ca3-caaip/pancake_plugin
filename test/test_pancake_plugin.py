import json
import unittest
from typing import Optional
from unittest.mock import MagicMock

from hexbytes import HexBytes
from senkalib.chain.bsc.bsc_transaction import BscTransaction

from pancake_plugin.pancake_plugin import PancakePlugin


class TestPancakePlugin(unittest.TestCase):
    @classmethod
    def get_token_table_mock(cls):
        def mock_get_symbol(chain: str, token_original_id: str) -> Optional[str]:
            if (
                chain == "bsc"
                and token_original_id == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            ):
                return "bnb"
            elif (
                chain == "bsc"
                and token_original_id == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
            ):
                return "cake"
            elif (
                chain == "bsc"
                and token_original_id == "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
            ):
                return "eth"
            else:
                return None

        def mock_get_symbol_uuid(chain: str, token_original_id: str) -> str:
            if (
                chain == "bsc"
                and token_original_id == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
            ):
                return "87dae675-c183-c452-fffa-ac519b71df01"
            elif (
                chain == "bsc"
                and token_original_id == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
            ):
                return "547faa5d-8c2b-8964-9053-2c26eb32cd18"
            elif (
                chain == "bsc"
                and token_original_id == "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
            ):
                return "5408d890-493d-bbc9-57cd-cfd013fefdb8"
            else:
                return None

        mock = MagicMock()
        mock.get_symbol.side_effect = mock_get_symbol
        mock.get_symbol_uuid.side_effect = mock_get_symbol_uuid
        return mock

    def test_can_handle(self):
        transaction = self.get_bsc_transaction("header", "swap_bnb_to_cake")
        swap_type = PancakePlugin.can_handle(transaction)
        assert swap_type

        transaction = self.get_bsc_transaction("header", "approve")
        swap_type = PancakePlugin.can_handle(transaction)
        assert swap_type is False

    def test_transaction_fee(self):
        transaction = self.get_bsc_transaction("header", "swap_bnb_to_cake")
        mock = TestPancakePlugin.get_token_table_mock()
        caajs = PancakePlugin.get_caajs(
            "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E", transaction, mock
        )
        caaj_transaction_fee = caajs[2]
        assert caaj_transaction_fee.executed_at == "2021-12-28 01:28:52"
        assert caaj_transaction_fee.chain == "bsc"
        assert caaj_transaction_fee.platform == "pancakeswap"
        assert caaj_transaction_fee.application == "bsc"
        assert (
            caaj_transaction_fee.transaction_id
            == "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109"
        )
        assert caaj_transaction_fee.type == "lose"
        assert caaj_transaction_fee.amount == "0.00067182"
        assert caaj_transaction_fee.token_symbol == "bnb"
        assert (
            caaj_transaction_fee.token_original_id
            == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
        )
        assert (
            caaj_transaction_fee.token_symbol_uuid
            == "87dae675-c183-c452-fffa-ac519b71df01"
        )
        assert (
            caaj_transaction_fee.caaj_from
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert (
            caaj_transaction_fee.caaj_to == "0x0000000000000000000000000000000000000000"
        )
        assert caaj_transaction_fee.comment == "pancakeswap transaction fee"

    def test_get_caajs_swap_cake_to_eth(self):
        transaction = self.get_bsc_transaction("header", "swap_cake_to_eth")
        mock = TestPancakePlugin.get_token_table_mock()
        caajs = PancakePlugin.get_caajs(
            "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E", transaction, mock
        )

        assert caajs[0].trade_uuid == caajs[1].trade_uuid
        assert caajs[1].trade_uuid == caajs[2].trade_uuid

        caaj_transaction_swap = caajs[0]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0xae40de844d1c26be96db829ff0344e96ad38dc64d383b6e22d480c504b164ec0"
        )
        assert caaj_transaction_swap.type == "send"
        assert caaj_transaction_swap.amount == "1"
        assert caaj_transaction_swap.token_symbol == "cake"
        assert (
            caaj_transaction_swap.token_original_id
            == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "547faa5d-8c2b-8964-9053-2c26eb32cd18"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

        caaj_transaction_swap = caajs[1]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0xae40de844d1c26be96db829ff0344e96ad38dc64d383b6e22d480c504b164ec0"
        )
        assert caaj_transaction_swap.type == "receive"
        assert caaj_transaction_swap.amount == "0.003189165151348716"
        assert caaj_transaction_swap.token_symbol == "eth"
        assert (
            caaj_transaction_swap.token_original_id
            == "0x2170Ed0880ac9A755fd29B2688956BD959F933F8"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "5408d890-493d-bbc9-57cd-cfd013fefdb8"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

    def test_get_caajs_swap_cake_to_bnb(self):
        transaction = self.get_bsc_transaction("header", "swap_cake_to_bnb")
        mock = TestPancakePlugin.get_token_table_mock()
        caajs = PancakePlugin.get_caajs(
            "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E", transaction, mock
        )

        assert caajs[0].trade_uuid == caajs[1].trade_uuid
        assert caajs[1].trade_uuid == caajs[2].trade_uuid

        caaj_transaction_swap = caajs[0]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0xd3f63cdad3bb1b8ea46fafbaac21c93cdb7204daece60f1a44aaa198f58371fa"
        )
        assert caaj_transaction_swap.type == "send"
        assert caaj_transaction_swap.amount == "21.5721707333114908"
        assert caaj_transaction_swap.token_symbol == "cake"
        assert (
            caaj_transaction_swap.token_original_id
            == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "547faa5d-8c2b-8964-9053-2c26eb32cd18"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

        caaj_transaction_swap = caajs[1]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0xd3f63cdad3bb1b8ea46fafbaac21c93cdb7204daece60f1a44aaa198f58371fa"
        )
        assert caaj_transaction_swap.type == "receive"
        assert caaj_transaction_swap.amount == "0.496512815787098187"
        assert caaj_transaction_swap.token_symbol == "bnb"
        assert (
            caaj_transaction_swap.token_original_id
            == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "87dae675-c183-c452-fffa-ac519b71df01"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

    def test_get_caajs_swap_bnb_to_cake(self):
        transaction = self.get_bsc_transaction("header", "swap_bnb_to_cake")
        mock = TestPancakePlugin.get_token_table_mock()
        caajs = PancakePlugin.get_caajs(
            "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E", transaction, mock
        )

        assert caajs[0].trade_uuid == caajs[1].trade_uuid
        assert caajs[1].trade_uuid == caajs[2].trade_uuid

        caaj_transaction_swap = caajs[0]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109"
        )
        assert caaj_transaction_swap.type == "send"
        assert caaj_transaction_swap.amount == "0.5"
        assert caaj_transaction_swap.token_symbol == "bnb"
        assert (
            caaj_transaction_swap.token_original_id
            == "0xbb4CdB9CBd36B01bD1cBaEBF2De08d9173bc095c"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "87dae675-c183-c452-fffa-ac519b71df01"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

        caaj_transaction_swap = caajs[1]
        assert caaj_transaction_swap.chain == "bsc"
        assert caaj_transaction_swap.platform == "pancakeswap"
        assert caaj_transaction_swap.application == "bsc"
        assert (
            caaj_transaction_swap.transaction_id
            == "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109"
        )
        assert caaj_transaction_swap.type == "receive"
        assert caaj_transaction_swap.amount == "21.562948714728883817"
        assert caaj_transaction_swap.token_symbol == "cake"
        assert (
            caaj_transaction_swap.token_original_id
            == "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82"
        )
        assert (
            caaj_transaction_swap.token_symbol_uuid
            == "547faa5d-8c2b-8964-9053-2c26eb32cd18"
        )
        assert (
            caaj_transaction_swap.caaj_from
            == "0x10ED43C718714eb63d5aA57B78B54704E256024E"
        )
        assert (
            caaj_transaction_swap.caaj_to
            == "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E"
        )
        assert caaj_transaction_swap.comment == "pancakeswap swap"

    def test_get_caajs_failed(self):
        transaction = self.get_bsc_transaction("header", "transaction_fail")
        mock = TestPancakePlugin.get_token_table_mock()
        caajs = PancakePlugin.get_caajs(
            "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E", transaction, mock
        )
        assert not caajs

    # TODO: 未対応トランザクションファイル
    # - liquidity_add_bnb_cake
    # - liquidity_add_busd_eth
    # - liquidity_remove_bnb_cake
    # - liquidity_remove_eth_busd
    # - unstake_cake_bnb
    # - stake_cake_bnb
    # - harvest_cake_bnb

    def get_bsc_transaction(self, header_filename, receipt_filename):
        file_header = open(
            f"test/testdata/{header_filename}.json", "r", encoding="utf-8"
        )
        header = json.load(file_header)
        file_header.close()

        file_receipt = open(
            f"test/testdata/transaction_receipt/{receipt_filename}.json",
            "r",
            encoding="utf-8",
        )
        receipt = json.load(file_receipt)
        for i_logs, log in enumerate(receipt["logs"]):
            for i_topics, topic in enumerate(log["topics"]):
                receipt["logs"][i_logs]["topics"][i_topics] = HexBytes(topic)
            pass
        file_receipt.close()

        transaction = BscTransaction(
            receipt["transactionHash"],
            receipt,
            header["timeStamp"],
            header["gasUsed"],
            header["gasPrice"],
        )

        return transaction


if __name__ == "__main__":
    unittest.main()
