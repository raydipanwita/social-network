from lib.user import *
from lib.user_repository import *

def test_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    result = repository.all()
    assert result == [
        User(1, "Dipa", "rite2dipa@yahoo.com"),
        User(2, "Dalloway", "dalloway@gmail.com")
    ]

def test_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    
    result = repository.find(2)
    assert result == User(2, "Dalloway", "dalloway@gmail.com")
    
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    user = User("None", "e", "e@e.net")
    repository.create(user)
    assert repository.all() == [
        User(1, "Dipa", "rite2dipa@yahoo.com"),
        User(2, "Dalloway", "dalloway@gmail.com"),
        User(3, "e", "e@e.net")
    ] 

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    assert repository.delete(3) is None
    assert repository.all() == [
        User(1, "Dipa", "rite2dipa@yahoo.com"),
        User(2, "Dalloway", "dalloway@gmail.com")       
    ] 