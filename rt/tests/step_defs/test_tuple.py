from math import sqrt
from pytest_bdd import scenarios
from pytest_bdd import given, when, then, parsers
from rt.rtctuple import make_tuple, dot, cross
from rt import Colour, Point, Vector, Tuple

scenarios("../features/tuple.feature")


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
        "p1 = point({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _p1_point(x, y, z):
    return Point(x, y, z)


@given(
    parsers.cfparse(
        "p2 = point({x:Number}, {y:Number}, {z:Number})", extra_types=dict(Number=float)
    )
)
def _p2_point(x, y, z):
    return Point(x, y, z)


@given(
    parsers.cfparse(
        "v1 = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def _v1_vector(x, y, z):
    return Vector(x, y, z)


@given(
    parsers.cfparse(
        "v2 = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def _v2_vector(x, y, z):
    return Vector(x, y, z)


@given(parsers.cfparse("zero = vector(0, 0, 0)"))
def _zero():
    return Vector(0, 0, 0)


@given(parsers.cfparse(
    "c = color({r:Number}, {g:Number}, {b:Number})",
    extra_types=dict(Number=float)
    )
)
def _colour(r, g, b):
    return Colour(r, g, b)


"""

    WHEN STEPS

"""
@when("norm = normalize(v)")
def _normalized_vector(_vector):
    _vector.norm


"""

    THEN STEPS

"""


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
        extra_types=dict(Number=float),
    )
)
def validate_point_minus_point_subtraction(_p1_point, _p2_point, x, y, z):
    assert Vector(x, y, z) == _p1_point - _p2_point


@then(
    parsers.cfparse(
        "p - v = point({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_point_minus_vector_subtraction(_point, _vector, x, y, z):
    assert Point(x, y, z) == _point - _vector


@then(
    parsers.cfparse(
        "v1 - v2 = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_vector_minus_vector_subtraction(_v1_vector, _v2_vector, x, y, z):
    assert Vector(x, y, z) == _v1_vector - _v2_vector


@then(
    parsers.cfparse(
        "zero - v = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_zero_minus_vector(_zero, _vector, x, y, z):
    assert _zero - _vector == Vector(x, y, z)


@then(
    parsers.cfparse(
        "-a = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_tuple_negation(_tuple, x, y, z, w):
    assert -_tuple == Tuple(x, y, z, w)


@then(
    parsers.cfparse(
        "a * {s:Number} = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_scalar_multiply(_tuple, s, x, y, z, w):
    assert _tuple * s == Tuple(x, y, z, w)


@then(
    parsers.cfparse(
        "a / {s:Number} = tuple({x:Number}, {y:Number}, {z:Number}, {w:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_scalar_division(_tuple, s, x, y, z, w):
    assert _tuple / s == Tuple(x, y, z, w)


@then(
    parsers.cfparse(
        "magnitude(v) = {m:Number}",
        extra_types=dict(Number=float),
    )
)
def validate_magnitude_computation(_vector, m):
    assert _vector.magnitude == m


@then(
    parsers.cfparse(
        "magnitude(v) = sqrt({m:Number})",
        extra_types=dict(Number=float),
    )
)
def validate_magnitude_computation_2(_vector, m):
    assert _vector.magnitude == sqrt(m)


@then(
    parsers.cfparse(
        "normalize(v) = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float),        
    )
)
def validate_normalize(_vector, x, y, z):
    assert _vector.norm == Vector(x, y, z)


@then(
    parsers.cfparse(
        "normalize(v) = approximately vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float)
    )
)
def validate_normalize_approximately(_vector, x, y, z):
    """ Floating-point comparison; use an epsilon to assert correctness
    """
    epsilon = 0.00001
    under_test = _vector.norm
    assert x - epsilon <= under_test.x <= x + epsilon
    assert y - epsilon <= under_test.y <= y + epsilon
    assert z - epsilon <= under_test.z <= z + epsilon


@then(
    parsers.cfparse(
        "magnitude(norm) = {n:Number}",
        extra_types=dict(Number=float)
    )
)
def validate_magnitude_of_normalized_vector(_vector, n):
    assert _vector.norm.magnitude == n


@then(
    parsers.cfparse(
        "dot(v1, v2) = {n:Number}",
        extra_types=dict(Number=float)
    )
)
def validate_dot_product(_v1_vector, _v2_vector, n):
    assert dot(_v1_vector, _v2_vector) == n


@then(
    parsers.cfparse(
        "cross(v1, v2) = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float)
    )
)
def validate_cross_product_v1_v2(_v1_vector, _v2_vector, x, y, z):
    assert cross(_v1_vector, _v2_vector) == Vector(x, y, z)


@then(
    parsers.cfparse(
        "cross(v2, v1) = vector({x:Number}, {y:Number}, {z:Number})",
        extra_types=dict(Number=float)
    )
)
def validate_cross_product_v2_v1(_v1_vector, _v2_vector, x, y, z):
    assert cross(_v2_vector, _v1_vector) == Vector(x, y, z)


@then(parsers.cfparse("c.red = {n:Number}", extra_types=dict(Number=float)))
def validate_red_component(_colour, n):
    assert _colour.red == n


@then(parsers.cfparse("c.green = {n:Number}", extra_types=dict(Number=float)))
def validate_red_component(_colour, n):
    assert _colour.green == n


@then(parsers.cfparse("c.blue = {n:Number}", extra_types=dict(Number=float)))
def validate_red_component(_colour, n):
    assert _colour.blue == n