from modules.rezept_calculation import RezeptCalculation


def test_正常():
    assert_dict = RezeptCalculation(100, 50).main()
    assert assert_dict['reduction'] == 17
    assert assert_dict['percent'] == '39.7%'
    assert assert_dict['total'] == 100
    assert assert_dict['contact'] == 50
    assert assert_dict['result_total'] == 83
    assert assert_dict['result_contact'] == 33


def test_正常_100_0():
    assert_dict = RezeptCalculation(100, 0).main()
    assert assert_dict['reduction'] == 0
    assert assert_dict['percent'] == '0.0%'
    assert assert_dict['total'] == 100
    assert assert_dict['contact'] == 0
    assert assert_dict['result_total'] == 100
    assert assert_dict['result_contact'] == 0


def test_境界値_under():
    assert_dict = RezeptCalculation(100, 39).main()
    assert assert_dict['reduction'] == 0
    assert assert_dict['percent'] == '39.0%'
    assert assert_dict['total'] == 100
    assert assert_dict['contact'] == 39
    assert assert_dict['result_total'] == 100
    assert assert_dict['result_contact'] == 39


def test_境界値_over():
    assert_dict = RezeptCalculation(100, 40).main()
    assert assert_dict['reduction'] == 1
    assert assert_dict['percent'] == '39.3%'
    assert assert_dict['total'] == 100
    assert assert_dict['contact'] == 40
    assert assert_dict['result_total'] == 99
    assert assert_dict['result_contact'] == 39


def test_異常_zero_erorr():
    assert_dict = RezeptCalculation(0, 0).main()
    assert assert_dict['reduction'] == 0
    assert assert_dict['percent'] == '0%'
    assert assert_dict['total'] == 0
    assert assert_dict['contact'] == 0
    assert assert_dict['result_total'] == 0
    assert assert_dict['result_contact'] == 0


def test_異常_計算不能():
    assert_dict = RezeptCalculation(100, 100).main()
    assert assert_dict['reduction'] == 100
    assert assert_dict['percent'] == '0%'
    assert assert_dict['total'] == 100
    assert assert_dict['contact'] == 100
    assert assert_dict['result_total'] == 0
    assert assert_dict['result_contact'] == 0


def test_異常_分母の方が小さい():
    assert_dict = RezeptCalculation(10, 100).main()
    assert assert_dict['reduction'] == 10
    assert assert_dict['percent'] == '0%'
    assert assert_dict['total'] == 10
    assert assert_dict['contact'] == 100
    assert assert_dict['result_total'] == 0
    assert assert_dict['result_contact'] == 0
