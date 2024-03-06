from lib.post import * 

def test_constructs_post():
    post = Post(1, "My Post", "My content", 3)
    assert post.id == 1
    assert post.title == "My Post"
    assert post.contents == "My content"
    assert post.no_of_views == 3



"""
We can format artists to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "My Post", "My content", 3)
    assert str(post) == "Post(1, 'My Post', 'My content', 3)"
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
