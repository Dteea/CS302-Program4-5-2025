# Doney Tran
# 11/22/25
# CS302
# Program 4-5

import pytest
import hierarchy

@pytest.fixture
# Define empty objects
def social_media_obj():
    return hierarchy.SocialMedia(0, 0, 0, "")

def facebook_obj():
    return hierarchy.Facebook(0, 0, 0, "", 0, 0)

def tiktok_obj():
    return hierarchy.Tiktok(0, 0, 0, "", 0, 0)

def instagram_obj():
    return hierarchy.Instagram(0, 0, 0, "", 0, 0, 0)

# Testing creation of empty social_media_objs of each class
def test_empty_social_media(social_media_obj):
    assert social_media_obj._likes == 0
    assert social_media_obj._dislikes == 0
    assert social_media_obj._followers == 0
    assert social_media_obj._userID == ""

def test_empty_facebook(facebook_obj):
    assert facebook_obj.__groups == 0
    assert facebook_obj.__photos == 0

def test_empty_tiktok(tiktok_obj):
    assert tiktok_obj.__watch_time == 0
    assert tiktok_obj.__views == 0

def test_empty_instagram(instagram_obj):
    assert instagram_obj.__top_posts == 0
    assert instagram_obj.__posts == 0
    assert instagram_obj.__share == 0

# Test for SocialMedia Class methods
def test_update_with_negatives(social_media_obj):
    assert social_media_obj.update(-1, 6, 1293, "Test") == -1 
    assert social_media_obj.update(327, -32476, 1293, "Test") == -1
    assert social_media_obj.update(327, 32476, -371293, "Test") == -1 

def test_update_with_empty_string(social_media_obj):
    assert social_media_obj.update(1, 6, 1293, "") == -1 
    assert social_media_obj.update(327, 32476, 1293, "") == -1
    assert social_media_obj.update(327, 32476, 371293, "") == -1 

def test_update_valid(social_media_obj):
    assert social_media_obj.update(327, 32479, 295801, "Test") == 1
    assert social_media_obj.update(5, 0, 0, "127") == 1
    assert social_media_obj.update(2136, 34, 3, "Adrian127") == 1

def test_recommend_valid(social_media_obj):
    assert social_media_obj.recommend() == True 

def test_rating_valid(social_media_obj):
    assert social_media_obj.rating() >= 0

def test_quality_valid(social_media_obj):
    assert social_media_obj.quality() >= 0

# Test for Facebook Class methods
def test_upgrade_status_valid(facebook_obj):
    facebook_obj.upgrade_status()
    assert facebook_obj._userID == "Test" + ":thumbs:up:"

def test_group_follower_ratio_valid(facebook_obj):
    assert isinstance(facebook_obj.group_follower_ratio, int)

def test_is_influencer_valid(facebook_obj):
    assert facebook_obj.is_influencer() == True


# Test for Tiktok Class methods
def test_post_statistics_valid(tiktok_obj):
    assert tiktok_obj.post_statistics() >= 0

def test_calculate_revenue_valid(tiktok_obj):
    assert tiktok_obj.calculate_revenue() >= 0

def test_warning_valid(tiktok_obj):
    assert tiktok_obj.warning() == True

# Test for Instagram Class methods

def test_all_method_return_types(instagram_obj):
    assert isinstance(instagram_obj.average_post(), float)
    assert isinstance(instagram_obj.post_like_ratio(), float)
    assert isinstance(instagram_obj.share_like_ratio(), float) 

def test_all_method_returns_non_negative(instagram_obj):
    assert instagram_obj.average_post() > 0
    assert instagram_obj.post_like_ratio() > 0
    assert instagram_obj.share_like_ratio() > 0

def test_average_post_valid(instagram_obj):
    assert instagram_obj.average_post() >= 0

def test_post_like_ratio_valid(instagram_obj):
    assert instagram_obj.post_like_ratio() >= 0

def test_share_like_ratio_valid(instagram_obj):
    assert instagram_obj.share_like_ratio() >= 0