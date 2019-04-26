from pytest_bdd import scenario, given, then, parsers
from rt.rtctuple import make_tuple, Point, Vector, point, vector, Tuple


@scenario("tuple.feature", "A tuple with w=1.0 is a point")
def test_point_tuple():
    pass


@scenario("tuple.feature", "A tuple with w=0 is a vector")
def test_vector_tuple():
    pass


@scenario("tuple.feature", "point() creates tuples with w=1")
def test_point_factory():
    pass


@scenario("tuple.feature", "vector() creates tuples with w=0")
def test_vector_factory():
    pass


@given(
    parsers.cfparse(
        "p = point({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _point(x, y, z):
    return point(x, y, z)


@given(
    parsers.cfparse(
        "v = vector({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _vector(x, y, z):
    return vector(x, y, z)


@given(
    parsers.cfparse(
        "a = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def _tuple(x, y, z, w):
    return make_tuple(x, y, z, w)


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
