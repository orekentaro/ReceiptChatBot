from modules.recept_calculation import ReceiptCalculation


def test_正常():
    assert_dict = ReceiptCalculation(100, 50).main()
    assert assert_dict["reduction"] == 17
    assert assert_dict["result_percent"] == "39.75%"
    assert assert_dict["percent"] == "50.0%"
    assert assert_dict["total"] == 100
    assert assert_dict["contact"] == 50
    assert assert_dict["result_total"] == 83
    assert assert_dict["result_contact"] == 33


def test_正常_100_0():
    assert_dict = ReceiptCalculation(100, 0).main()
    assert assert_dict["reduction"] == -66
    assert assert_dict["percent"] == "0.0%"
    assert assert_dict["result_percent"] == "39.75%"
    assert assert_dict["total"] == 100
    assert assert_dict["contact"] == 0
    assert assert_dict["result_total"] == 166
    assert assert_dict["result_contact"] == 66


def test_境界値_under():
    assert_dict = ReceiptCalculation(100, 39).main()
    assert assert_dict["reduction"]
    assert assert_dict["result_percent"] == "39.60%"
    assert assert_dict["percent"] == "39.0%"
    assert assert_dict["total"] == 100
    assert assert_dict["contact"] == 39
    assert assert_dict["result_total"] == 101
    assert assert_dict["result_contact"] == 40


def test_境界値_over():
    assert_dict = ReceiptCalculation(100, 40).main()
    assert assert_dict["reduction"] == 1
    assert assert_dict["percent"] == "40.0%"
    assert assert_dict["result_percent"] == "39.39%"
    assert assert_dict["total"] == 100
    assert assert_dict["contact"] == 40
    assert assert_dict["result_total"] == 99
    assert assert_dict["result_contact"] == 39


def test_異常_zero_erorr():
    assert_dict = ReceiptCalculation(0, 0).main()
    assert assert_dict["reduction"] == 0
    assert assert_dict["result_percent"] == "0%"
    assert assert_dict["percent"] == "0%"
    assert assert_dict["total"] == 0
    assert assert_dict["contact"] == 0
    assert assert_dict["result_total"] == 0
    assert assert_dict["result_contact"] == 0


def test_異常_計算不能():
    assert_dict = ReceiptCalculation(100, 100).main()
    assert assert_dict["reduction"] == 100
    assert assert_dict["result_percent"] == "0%"
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
    assert assert_dict["reduction"] == -6
    assert assert_dict["result_percent"] == "39.93%"
    assert assert_dict["percent"] == "39.50%"
    assert assert_dict["total"] == 853
    assert assert_dict["contact"] == 337
    assert assert_dict["result_total"] == 859
    assert assert_dict["result_contact"] == 343


def test_正常_減算():
    assert_dict = ReceiptCalculation(853, 500).main()
    assert assert_dict["reduction"] == 265
    assert assert_dict["result_percent"] == "39.96%"
    assert assert_dict["percent"] == "58.61%"
    assert assert_dict["total"] == 853
    assert assert_dict["contact"] == 500
    assert assert_dict["result_total"] == 588
    assert assert_dict["result_contact"] == 235
