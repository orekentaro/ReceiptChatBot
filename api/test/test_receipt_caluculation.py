from modules.recept_calculation import ReceiptCalculation


def test_正常():
    assert_dict = ReceiptCalculation(1000, 500).main()
    assert assert_dict["reduction"] == 168
    assert assert_dict["result_percent"] == "39.90%"
    assert assert_dict["percent"] == "50.0%"
    assert assert_dict["total"] == 1000
    assert assert_dict["contact"] == 500
    assert assert_dict["result_total"] == 832
    assert assert_dict["result_contact"] == 332


def test_正常_100_0():
    assert_dict = ReceiptCalculation(1000, 0).main()
    assert assert_dict["reduction"] == -663
    assert assert_dict["percent"] == "0.0%"
    assert assert_dict["result_percent"] == "39.86%"
    assert assert_dict["total"] == 1000
    assert assert_dict["contact"] == 0
    assert assert_dict["result_total"] == 1663
    assert assert_dict["result_contact"] == 663


def test_境界値_under():
    assert_dict = ReceiptCalculation(1000, 390).main()
    assert assert_dict["reduction"] == -14
    assert assert_dict["result_percent"] == "39.84%"
    assert assert_dict["percent"] == "39.0%"
    assert assert_dict["total"] == 1000
    assert assert_dict["contact"] == 390
    assert assert_dict["result_total"] == 1014
    assert assert_dict["result_contact"] == 404


def test_境界値_over():
    assert_dict = ReceiptCalculation(1000, 400).main()
    assert assert_dict["reduction"] == 1
    assert assert_dict["percent"] == "40.0%"
    assert assert_dict["result_percent"] == "39.93%"
    assert assert_dict["total"] == 1000
    assert assert_dict["contact"] == 400
    assert assert_dict["result_total"] == 999
    assert assert_dict["result_contact"] == 399


def test_異常_zero_error():
    assert_dict = ReceiptCalculation(0, 0).main()
    assert assert_dict["reduction"] == 0
    assert assert_dict["result_percent"] == "0.0%"
    assert assert_dict["percent"] == "0.0%"
    assert assert_dict["total"] == 0
    assert assert_dict["contact"] == 0
    assert assert_dict["result_total"] == 0
    assert assert_dict["result_contact"] == 0


def test_異常_計算不能():
    assert_dict = ReceiptCalculation(100, 100).main()
    assert assert_dict["reduction"] == 100
    assert assert_dict["result_percent"] == "0.0%"
    assert assert_dict["percent"] == "100.0%"
    assert assert_dict["total"] == 100
    assert assert_dict["contact"] == 100
    assert assert_dict["result_total"] == 0
    assert assert_dict["result_contact"] == 0


def test_異常_分母の方が小さい():
    assert_dict = ReceiptCalculation(10, 100).main()
    assert assert_dict["reduction"] == 10
    assert assert_dict["percent"] == "1000.%"
    assert assert_dict["result_percent"] == "0%"
    assert assert_dict["total"] == 10
    assert assert_dict["contact"] == 100
    assert assert_dict["result_total"] == 0
    assert assert_dict["result_contact"] == 0


def test_正常_加算():
    assert_dict = ReceiptCalculation(853, 337).main()
    assert assert_dict["reduction"] == -5
    assert assert_dict["result_percent"] == "39.86%"
    assert assert_dict["percent"] == "39.50%"
    assert assert_dict["total"] == 853
    assert assert_dict["contact"] == 337
    assert assert_dict["result_total"] == 858
    assert assert_dict["result_contact"] == 342


def test_正常_減算():
    assert_dict = ReceiptCalculation(853, 500).main()
    assert assert_dict["reduction"] == 265
    assert assert_dict["result_percent"] == "39.96%"
    assert assert_dict["percent"] == "58.61%"
    assert assert_dict["total"] == 853
    assert assert_dict["contact"] == 500
    assert assert_dict["result_total"] == 588
    assert assert_dict["result_contact"] == 235
