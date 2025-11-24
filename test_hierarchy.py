import pytest
import hierarchy






@pytest.fixture
def object():
    return hierarchy.SocialMedia(0, 0, 0, "")

# Empty object
def test_empty_object(object):
    assert object._likes == 0
    assert object._dislikes == 0
    assert object._followers == 0
    assert object._userID == ""

def test_update_negative(object):
    pass