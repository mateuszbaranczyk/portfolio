from app import wallet


def test_get_value_in_pln(mocker):
    mocker.patch("app.requester.ExchangeRateRequester.get_todays_rate", return_value=4.50)

    wallet_ = wallet.Wallet()
    result = wallet_.get_value_in_pln()

    assert result == 0


def test_get_value_in_pln_2(mocker):
    mocker.patch("app.requester.ExchangeRateRequester.get_todays_rate", return_value=4.50)
    # pass
    wallet_ = wallet.Wallet()
    wallet_.add_buy_transaction("2021-09-01", 200, 4.20)
    wallet_.add_buy_transaction("2021-09-02", 500, 4.60)

    result = wallet_.get_value_in_pln()

    assert result == 700 * 4.5


def test_add_buy_transaction():
    wallet_ = wallet.Wallet()
    wallet_.add_buy_transaction("2021-09-01", 500, 4.50)

    result = wallet_.transactions[0]

    assert result.value == 500
    assert result.date == "2021-09-01"
    assert result.rate == 4.5


def test_add_sell_transaction():
    wallet_ = wallet.Wallet()
    wallet_.add_sell_transaction("2021-09-01", 500, 4.50)

    result = wallet_.transactions[0]

    assert result.value == -500
    assert result.date == "2021-09-01"
    assert result.rate == 4.5


def test_get_paid_value_in_pln():
    wallet_ = wallet.Wallet()
    wallet_.add_buy_transaction("2021-09-01", 500, 4.50)
    result = wallet_.get_paid_value_in_pln()

    assert result == 2250


def test_get_profit_in_pln(mocker):
    mocker.patch("app.requester.ExchangeRateRequester.get_todays_rate", return_value=4.50)

    wallet_ = wallet.Wallet()
    wallet_.add_buy_transaction("2021-09-01", 500, 4.50)

    result = wallet_.get_profit_in_pln()

    assert result == 0
