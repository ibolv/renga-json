import generateJSON


def test_get_coord():
    building_element = {
        "XY": [
            {
                "points": [
                    {"x": 0, "y": 0},
                    {"x": 1, "y": 0},
                    {"x": 1, "y": 1},
                    {"x": 0, "y": 1},
                ]
            }
        ]
    }

    coordinates = {"X": [0, 1, 1, 0], "Y": [0, 0, 1, 1]}

    assert generateJSON.get_coord(building_element) == coordinates


def test_point_inside_edge():
    elem1_points_x = [0, 2, 2, 0]
    elem1_points_y = [0, 0, 2, 2]
    elem2_points_x = [0.5, 1, 1, 0.5]
    elem2_points_y = [-0.5, -0.5, 0, 0]

    assert generateJSON.is_in_edge(
        x=elem2_points_x, y=elem2_points_y, xp=elem1_points_x, yp=elem1_points_y
    )
