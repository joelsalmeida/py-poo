import pytest

from TV import TV


def test_initial_atributes():
    tv = TV(14)

    assert tv.on is False
    assert tv.volume == 50
    assert tv.on is False
    assert tv.screen_size == 14


def test_raises_if_invalid_interactions_when_off():
    tv_off = TV(14)

    with pytest.raises(ValueError):
        tv_off.turn_up_volume()

    with pytest.raises(ValueError):
        tv_off.turn_down_volume()

    with pytest.raises(ValueError):
        tv_off.change_chanel(7)


tv_on = TV(14)
tv_on.turn_on_off()  # NOW, TV IS ON


def test_turn_up_volume():
    tv_on.turn_up_volume()
    assert tv_on.volume == 51

    for i in range(50):
        tv_on.turn_up_volume()
    assert tv_on.volume == 99


def test_turn_down_volume():
    tv_on.turn_down_volume()
    assert tv_on.volume == 98

    for i in range(100):
        tv_on.turn_down_volume()
    assert tv_on.volume == 0


def test_change_chanel():
    with pytest.raises(ValueError):
        tv_on.change_chanel(100)

    with pytest.raises(ValueError):
        tv_on.change_chanel(-1)

    tv_on.change_chanel(7)
    assert tv_on.chanel == 7


def test_turn_on_off():
    tv_on.turn_on_off()
    assert tv_on.on is False

    tv_on.turn_on_off()
    assert tv_on.on is True
