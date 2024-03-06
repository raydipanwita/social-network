from lib.user import *

def test_constructs_user():
    user = User(1, "Dipa username", "Dipa email_address")
    assert user.id == 1
    assert user.username == "Dipa username"
    assert user.email_address == "Dipa email_address"


"""
We can format artists to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "Dipa username", "Dipa email_address")
    assert str(user) == "User(1, 'Dipa username', 'Dipa email_address')"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

# """
# We can compare two identical artists
# And have them be equal
# """
# def test_artists_are_equal():
#     artist1 = Artist(1, "Test Artist", "Test Genre")
#     artist2 = Artist(1, "Test Artist", "Test Genre")
#     assert artist1 == artist2
#     # Try commenting out the `__eq__` method in lib/artist.py
#     # And see what happens when you run this test again.
