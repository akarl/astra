from models.system import Body


def test_body():
    body = Body(None, 1.0)

    for x in range(365):
        body.update_position()
        print body.position

    assert 1 == 2
