import unittest
import json
from senkalib.chain.bsc.bsc_transaction import BscTransaction
from src.pancake_plugin import PancakePlugin


class TestPancakePlugin(unittest.TestCase):
    # def test_can_handle_01(self):
    #     file_name = "exchange_bnb_to_cake"
    #     file_header = open("test/testdata/header.json",
    #                        "r", encoding="utf-8")
    #     header = json.load(file_header)
    #     file_header.close()

    #     file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
    #                         "r", encoding="utf-8")
    #     receipt = json.load(file_receipt)
    #     file_receipt.close()
    #     transaction = BscTransaction(
    #         header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
    #     swap_type = PancakePlugin.can_handle(transaction)
    #     assert swap_type

    def test_get_caajs_01(self):
        file_name = "exchange_bnb_to_cake"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82": "21.562948714728883817"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount": {"BNB": "0.5"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap trade"
        }
        caaj_fee_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"BNB": "0.00067182"},
            "debit_from": "0x0000000000000000000000000000000000000000",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount":  {"BNB": "0.00067182"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x0000000000000000000000000000000000000000",
            "comment": "pancakeswap transaction fee"
        }

        caaj_model = [caaj_main_model, caaj_fee_model]
        assert caaj == caaj_model

    def test_get_caajs_01_2(self):
        file_name = "exchange_cake_to_bnb"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"BNB": "0.496512815787098187"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount": {"0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82": "21.5721707333114908"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap trade"
        }

        assert caaj[0]['debit_amount'] == caaj_main_model['debit_amount']
        assert caaj[0]['credit_amount'] == caaj_main_model['credit_amount']

    def test_get_caajs_01_3(self):
        file_name = "exchange_cake_to_eth"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0x4f8534e85849cb54f0ae4ca0718939ab22de248f64e2e4dc607a76b12f20f109",
            "debit_title": "SPOT",
            "debit_amount": {"0x2170Ed0880ac9A755fd29B2688956BD959F933F8": "0.003189165151348716"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount": {"0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82": "1"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap trade"
        }

        assert caaj[0]['debit_amount'] == caaj_main_model['debit_amount']
        assert caaj[0]['credit_amount'] == caaj_main_model['credit_amount']

    def test_get_caajs_02(self):
        file_name = "liquidity_add_bnb_cake"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0xb4c3ed5db127089cd1be4b247537d163e74e99e33598348579ffae4f81877834",
            "debit_title": "LIQUIDITY",
            "debit_amount": {"0x0ed7e52944161450477ee417de9cd3a859b14fd0": "3.164332228458444898"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount":
            {"BNB": "0.497952988038470308",
                "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82": "21.562948714728883817"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap add liquidity"
        }

        assert caaj[0] == caaj_main_model

    def test_get_caajs_02_2(self):
        file_name = "liquidity_add_busd_eth"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0x9ef2e5580e57286e81d468bcf014bf875c0bbf23895a3b849a24965de9e65282",
            "debit_title": "LIQUIDITY",
            "debit_amount": {"0x7213a321F1855CF1779f42c0CD85d3D95291D34C": "0.036045299930279785"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "SPOT",
            "credit_amount": {"0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56":
                              "4.777146419651962634", "0x2170Ed0880ac9A755fd29B2688956BD959F933F8":
                              "0.001481713954703829"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap add liquidity"
        }

        assert caaj[0] == caaj_main_model

    def test_get_caajs_03(self):

        file_name = "liquidity_remove_bnb_cake"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0xdc70901bcb2517a885e41ab9ccb0a739ae73af4b8862a1c46f9ca2ce583b8cd3",
            "debit_title": "SPOT",
            "debit_amount": {"BNB": "0.497740943162833803", "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82":
                             "21.5721707333114908"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "LIQUIDITY",
            "credit_amount": {"0x0eD7e52944161450477ee417DE9Cd3a859b14fD0": "3.164332228458444898"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap remove liquidity"
        }

        assert caaj[0]['debit_title'] == caaj_main_model['debit_title']
        assert caaj[0]['debit_amount'] == caaj_main_model['debit_amount']
        assert caaj[0]['credit_title'] == caaj_main_model['credit_title']
        assert caaj[0]['credit_amount'] == caaj_main_model['credit_amount']

    def test_get_caajs_03_2(self):

        file_name = "liquidity_remove_eth_busd"
        file_header = open("test/testdata/header.json",
                           "r", encoding="utf-8")
        header = json.load(file_header)
        file_header.close()

        file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
                            "r", encoding="utf-8")
        receipt = json.load(file_receipt)
        file_receipt.close()
        transaction = BscTransaction(
            header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
        caaj = PancakePlugin.get_caajs(transaction)
        caaj_main_model = {
            "time": "2021-12-28 01:28:52",
            "platform": "bnb_pancakeswap",
            "transaction_id": "0xdc70901bcb2517a885e41ab9ccb0a739ae73af4b8862a1c46f9ca2ce583b8cd3",
            "debit_title": "SPOT",
            "debit_amount": {"0x2170Ed0880ac9A755fd29B2688956BD959F933F8": "0.003470017891951227",
                             "0x55d398326f99059fF775485246999027B3197955": "10.957944733812157838"},
            "debit_from": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_title": "LIQUIDITY",
            "credit_amount": {"0x531FEbfeb9a61D948c384ACFBe6dCc51057AEa7e": "0.143435764222230339"},
            "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
            "credit_to": "0x10ED43C718714eb63d5aA57B78B54704E256024E",
            "comment": "pancakeswap remove liquidity"
        }

        assert caaj[0]['debit_title'] == caaj_main_model['debit_title']
        assert caaj[0]['debit_amount'] == caaj_main_model['debit_amount']
        assert caaj[0]['credit_title'] == caaj_main_model['credit_title']
        assert caaj[0]['credit_amount'] == caaj_main_model['credit_amount']

    # def test_get_caajs_04(self):
    #     file_name = "transaction_fail"
    #     file_header = open("test/testdata/header.json",
    #                        "r", encoding="utf-8")
    #     header = json.load(file_header)
    #     file_header.close()

    #     file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
    #                         "r", encoding="utf-8")
    #     receipt = json.load(file_receipt)
    #     file_receipt.close()
    #     transaction = BscTransaction(
    #         header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
    #     caaj = PancakePlugin.get_caajs(transaction)
    #     assert caaj is None

    # def test_get_caajs_05(self):
    #     file_name = "stake_cake_bnb"
    #     file_header = open("test/testdata/header.json",
    #                        "r", encoding="utf-8")
    #     header = json.load(file_header)
    #     file_header.close()

    #     file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
    #                         "r", encoding="utf-8")
    #     receipt = json.load(file_receipt)
    #     file_receipt.close()
    #     transaction = BscTransaction(
    #         header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
    #     caaj = PancakePlugin.get_caajs(transaction)
    #     caaj_main_model = {
    #         "time": "2021-12-28 01:28:52",
    #         "platform": "bnb_pancakeswap",
    #         "transaction_id": "0x0ccda1b34404e55bd211144b7d024f03c47bdc1fd8a47396271ffe1f63a8c0cb",
    #         "debit_title": "STAKING",
    #         "debit_amount": {"0x0eD7e52944161450477ee417DE9Cd3a859b14fD0": "0.291597195540468368"},
    #         "debit_from": "0x73feaa1eE314F8c655E354234017bE2193C9E24E",
    #         "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
    #         "credit_title": "SPOT",
    #         "credit_amount": {"0x0eD7e52944161450477ee417DE9Cd3a859b14fD0": "0.291597195540468368"},
    #         "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
    #         "credit_to": "0x73feaa1eE314F8c655E354234017bE2193C9E24E",
    #         "comment": "pancakeswap stake"
    #     }
    #     assert caaj[0] == caaj_main_model

    # def test_get_caajs_06(self):
    #     file_name = "unstake_cake_bnb"
    #     file_header = open("test/testdata/header.json",
    #                        "r", encoding="utf-8")
    #     header = json.load(file_header)
    #     file_header.close()

    #     file_receipt = open("test/testdata/transaction_receipt/" + file_name + ".json",
    #                         "r", encoding="utf-8")
    #     receipt = json.load(file_receipt)
    #     file_receipt.close()
    #     transaction = BscTransaction(
    #         header['hash'], receipt, header['timeStamp'], header['gasUsed'], header['gasPrice'])
    #     caaj = PancakePlugin.get_caajs(transaction)
    #     caaj_main_model = {
    #         "time": "2021-12-28 01:28:52",
    #         "platform": "bnb_pancakeswap",
    #         "transaction_id": "0x0ccda1b34404e55bd211144b7d024f03c47bdc1fd8a47396271ffe1f63a8c0cb",
    #         "debit_title": "STAKING",
    #         "debit_amount": {"0x0eD7e52944161450477ee417DE9Cd3a859b14fD0": "0.291597195540468368"},
    #         "debit_from": "0x73feaa1eE314F8c655E354234017bE2193C9E24E",
    #         "debit_to": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
    #         "credit_title": "SPOT",
    #         "credit_amount": {"0x0eD7e52944161450477ee417DE9Cd3a859b14fD0": "0.291597195540468368"},
    #         "credit_from": "0xDa28ecfc40181a6DAD8b52723035DFba3386d26E",
    #         "credit_to": "0x73feaa1eE314F8c655E354234017bE2193C9E24E",
    #         "comment": "pancakeswap unstake"
    #     }
    #     assert caaj[0] == caaj_main_model


if __name__ == '__main__':
    unittest.main()
