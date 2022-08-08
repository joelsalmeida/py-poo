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
