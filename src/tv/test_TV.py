import pytest

from TV import TV

tv = TV(14)


def test_initial_atributes():
    assert tv.on is False
    assert tv.volume == 50
    assert tv.on is False
    assert tv.screen_size == 14


def test_turn_up_volume():
    tv.turn_up_volume()
    assert tv.volume == 51

    for i in range(50):
        tv.turn_up_volume()
    assert tv.volume == 99


def test_turn_down_volume():
    tv.turn_down_volume()
    assert tv.volume == 98

    for i in range(100):
        tv.turn_down_volume()
    assert tv.volume == 0


def test_change_chanel():
    with pytest.raises(ValueError):
        tv.change_chanel(100)

    with pytest.raises(ValueError):
        tv.change_chanel(-1)

    tv.change_chanel(7)
    assert tv.chanel == 7
