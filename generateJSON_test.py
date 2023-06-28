import generateJSON
from domain.Room import Room
from domain.Geometry import Geometry
from domain.Point3D import Point3D
import uuid


def test_get_coord():
    building_element = Room(
        id=uuid.uuid4(),
        name="Room",
        outputs=[],
        area=1,
        sizeZ=2,
        zLevel=0,
        xy=[
            Geometry(
                [
                    Point3D(x=0, y=0, z=0),
                    Point3D(x=1, y=0, z=0),
                    Point3D(x=1, y=1, z=0),
                    Point3D(x=0, y=1, z=0),
                ]
            )
        ],
    )

    coordinates = {"X": [0, 1, 1, 0], "Y": [0, 0, 1, 1]}

    assert generateJSON.get_coord(building_element) == coordinates


def test_point_inside_edge():
    elem1_points_x = [0.0, 2.0, 2.0, 0.0]
    elem1_points_y = [0.0, 0.0, 2.0, 2.0]
    elem2_points_x = [0.5, 1, 1, 0.5]
    elem2_points_y = [-0.5, -0.5, 0, 0]

    assert generateJSON.is_in_edge(
        x=elem2_points_x, y=elem2_points_y, xp=elem1_points_x, yp=elem1_points_y
    )
