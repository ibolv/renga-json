import generateJSON


def test_get_coord():
    building_element = {
        'XY': [{
            'points': [
                {
                    'x': 0,
                    'y': 0
                },
                {
                    'x': 1,
                    'y': 0
                },
                {
                    'x': 1,
                    'y': 1
                },
                {
                    'x': 0,
                    'y': 1
                },
            ]
        }]
    }

    coordinates = {
        'X': [0, 1, 1, 0],
        'Y': [0, 0, 1, 1]
    }

    assert generateJSON.get_coord(building_element) == coordinates
