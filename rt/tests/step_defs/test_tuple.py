from pytest_bdd import scenarios
from pytest_bdd import given, then, parsers
from rt.rtctuple import make_tuple, Point, Vector, Tuple

scenarios('../features/tuple.feature')


@given(
    parsers.cfparse(
        "p = point({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _point(x, y, z):
    return Point(x, y, z)


@given(
    parsers.cfparse(
        "v = vector({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _vector(x, y, z):
    return Vector(x, y, z)


@given(
    parsers.cfparse(
        "a = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def _tuple(x, y, z, w):
    return make_tuple(x, y, z, w)


@given(
    parsers.cfparse(
        "a1 = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def _a1_tuple(x, y, z, w):
    return make_tuple(x, y, z, w)


@given(
    parsers.cfparse(
        "a2 = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def _a2_tuple(x, y, z, w):
    return make_tuple(x, y, z, w)


@given(
    parsers.cfparse(
        "p1 = point({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def _p1_point(x, y, z):
    return Point(x, y, z)


@given(
    parsers.cfparse(
        "p2 = point({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def _p2_point(x, y, z):
    return Point(x, y, z)


@then(parsers.cfparse("a.x = {x:Number}", extra_types=dict(Number=float)))
def x_coord_matches_value(_tuple, x):
    assert _tuple.x == x


@then(parsers.cfparse("a.y = {y:Number}", extra_types=dict(Number=float)))
def y_coord_matches_value(_tuple, y):
    assert _tuple.y == y


@then(parsers.cfparse("a.z = {z:Number}", extra_types=dict(Number=float)))
def z_coord_matches_value(_tuple, z):
    assert _tuple.z == z


@then(parsers.cfparse("a.w = {w:Number}", extra_types=dict(Number=float)))
def w_coord_matches_value(_tuple, w):
    assert _tuple.w == w


@then(parsers.cfparse("a is a {t:String}", extra_types=dict(String=str)))
def is_a_klass(_tuple, t):
    klass = Point if t == "point" else Vector
    assert isinstance(_tuple, klass)


@then(parsers.cfparse("a is not a {t:String}", extra_types=dict(String=str)))
def is_not_a_klass(_tuple, t):
    klass = Point if t == "point" else Vector
    assert not isinstance(_tuple, klass)


@then(
    parsers.cfparse(
        "p = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def is_point_from_tuple(_point, x, y, z, w):
    pass


@then(
    parsers.cfparse(
        "v = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def is_vectory_from_tuple(_vector, x, y, z, w):
    assert _vector == Tuple(x, y, z, w)


@then(
    parsers.cfparse(
        "a1 + a2 = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def valid_addition(_a1_tuple, _a2_tuple, x, y, z, w):
    assert Tuple(x, y, z, w) == _a1_tuple + _a2_tuple


@then(
    parsers.cfparse(
        "p1 - p2 = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float)
    )
)
def validate_subtraction(_p1_point, _p2_point, x, y, z):
    assert Vector(x, y, z) == _p1_point - _p2_point