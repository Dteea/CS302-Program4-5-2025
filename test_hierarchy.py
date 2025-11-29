# Doney Tran
# 11/22/25
# CS302
# Program 4-5

import pytest
import hierarchy
import emoji

# Define empty objects
@pytest.fixture
def social_media_obj():
    return hierarchy.SocialMedia(0, 0, 0, "")

@pytest.fixture
def facebook_obj():
    return hierarchy.Facebook(0, 0, 0, "", 0, 0)

@pytest.fixture
def tiktok_obj():
    return hierarchy.Tiktok(0, 0, 0, "", 0, 0)

@pytest.fixture
def instagram_obj():
    return hierarchy.Instagram(0, 0, 0, "", 0, 0, 0)

# Testing creation of empty social_media_objs of each class
def test_empty_social_media(social_media_obj):
    assert social_media_obj._likes == 0
    assert social_media_obj._dislikes == 0
    assert social_media_obj._followers == 0
    assert social_media_obj._userID == ""

def test_empty_facebook(facebook_obj):
    assert facebook_obj._likes == 0
    assert facebook_obj._dislikes == 0
    assert facebook_obj._followers == 0
    assert facebook_obj._userID == ""
    assert facebook_obj._Facebook__groups == 0
    assert facebook_obj._Facebook__photos == 0

def test_empty_tiktok(tiktok_obj):
    assert tiktok_obj._likes == 0
    assert tiktok_obj._dislikes == 0
    assert tiktok_obj._followers == 0
    assert tiktok_obj._userID == ""
    assert tiktok_obj._Tiktok__watch_time == 0
    assert tiktok_obj._Tiktok__views == 0

def test_empty_instagram(instagram_obj):
    assert instagram_obj._likes == 0
    assert instagram_obj._dislikes == 0
    assert instagram_obj._followers == 0
    assert instagram_obj._userID == ""
    assert instagram_obj._Instagram__top_posts == 0
    assert instagram_obj._Instagram__posts == 0
    assert instagram_obj._Instagram__share == 0

# Test for SocialMedia Class methods
# Maybe remove update since interface should deal with input
#def test_update_with_negatives(social_media_obj):
#    assert social_media_obj.update(-1, 6, 1293, "Test") == -1 
#    assert social_media_obj.update(327, -32476, 1293, "Test") == -1
#    assert social_media_obj.update(327, 32476, -371293, "Test") == -1 
#
#def test_update_with_empty_string(social_media_obj):
#    assert social_media_obj.update(1, 6, 1293, "") == -1 
#    assert social_media_obj.update(327, 32476, 1293, "") == -1
#    assert social_media_obj.update(327, 32476, 371293, "") == -1 
#
#def test_update_valid(social_media_obj):
#    assert social_media_obj.update(327, 32479, 295801, "Test") == 1
#    assert social_media_obj.update(5, 0, 0, "127") == 1
#    assert social_media_obj.update(2136, 34, 3, "Adrian127") == 1

def test_recommend_valid_score_greater_than_100000(social_media_obj):
    social_media_obj._likes = 1000000
    social_media_obj._followers = 2347324 
    assert isinstance(social_media_obj.recommend(), float)
    assert social_media_obj.recommend() == 234732.83

def test_recommend_valid_score_less_than_100000(social_media_obj):
    social_media_obj._likes = 25 
    social_media_obj._followers = 237 
    assert isinstance(social_media_obj.recommend(), float)
    assert social_media_obj.recommend() == 23.81

def test_recommend_zero(social_media_obj):
    social_media_obj._likes = 25 
    social_media_obj._followers = 0
    assert social_media_obj.recommend() == -1.0

def test_rating_valid(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 9178
    social_media_obj._dislikes = 213
    assert isinstance(social_media_obj.rating(), float)
    assert social_media_obj.rating() == .98 

def test_rating_zero(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 0 
    social_media_obj._dislikes = 0 
    assert social_media_obj.rating() == -1.0

def test_quality_valid_score_greater_than_1(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 12793823472
    social_media_obj._dislikes = 23424
    social_media_obj._followers = 3744
    assert isinstance(social_media_obj.quality(), float)
    assert social_media_obj.quality() == 1.36

def test_quality_valid_score_between_0_and_1(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 1279372
    social_media_obj._dislikes = 2342429
    social_media_obj._followers = 3744
    assert isinstance(social_media_obj.quality(), float)
    assert social_media_obj.quality() == .06 

def test_quality_valid_score_negative(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 1279372
    social_media_obj._dislikes = 2342429576
    social_media_obj._followers = 3744
    assert isinstance(social_media_obj.quality(), float)
    assert social_media_obj.quality() == -0.64

def test_quality_zero(social_media_obj):
    social_media_obj._userID = "Kayle"
    social_media_obj._likes = 0 
    social_media_obj._dislikes = 0 
    social_media_obj._followers = 0 
    assert social_media_obj.quality() == -1.0 

def test_get_user_id(social_media_obj):
    social_media_obj._userID = "Vivia"
    assert isinstance(social_media_obj.get_user_id(), str)
    assert social_media_obj.get_user_id() == social_media_obj._userID

# Facebook derived class methods
def test_upgrade_status_valid(facebook_obj):
    facebook_obj._userID = "Ryan Jane"
    facebook_obj._Facebook__groups = 12444
    facebook_obj._Facebook__photos = 96368
    assert facebook_obj.upgrade_status() == True
    assert facebook_obj._userID == emoji.emojize("Ryan Jane :fire:") 

def test_upgrade_status_no_upgrade(facebook_obj):
    facebook_obj._userID = "Ryan Jane"
    facebook_obj._Facebook__groups = 9237
    facebook_obj._Facebook__photos = 3246 
    assert facebook_obj.upgrade_status() == False
    assert facebook_obj._userID == emoji.emojize("Ryan Jane") 

def test_group_follower_ratio_valid(facebook_obj):
    facebook_obj._Facebook__groups = 9237
    facebook_obj._followers = 65789
    assert facebook_obj.group_follower_ratio() == .14 
    
def test_group_follower_ratio_zero(facebook_obj):
    facebook_obj._Facebook__groups = 9237
    facebook_obj._followers = 0 
    assert facebook_obj.group_follower_ratio() == -1.0

def test_is_influencer_valid(facebook_obj):
    facebook_obj._userID = "CashMoney$$"
    facebook_obj._Facebook__groups = 7439
    facebook_obj._followers = 1239815 
    facebook_obj._likes = 2139649
    assert facebook_obj.is_influencer() == True 
    facebook_obj.is_influencer()
    assert facebook_obj._userID == "CashMoney (Influencer)"

def test_is_influencer_valid(facebook_obj):
    facebook_obj._userID = "CashMoney$$"
    facebook_obj._Facebook__groups = 7439
    facebook_obj._followers = 1239815 
    facebook_obj._likes = 2139649
    assert facebook_obj.is_influencer() == True 
    facebook_obj.is_influencer()
    assert facebook_obj._userID == "CashMoney (Influencer)"

def test_is_influencer_valid(facebook_obj):
    facebook_obj._userID = "CashMoney$$"
    facebook_obj._Facebook__groups = 7439
    facebook_obj._followers = 1239815 
    facebook_obj._likes = 2139649
    facebook_obj.is_influencer()
    assert facebook_obj._userID == "CashMoney$$ (Influencer)"
    assert facebook_obj.is_influencer() == True 

def test_is_influencer_not_influencer(facebook_obj):
    facebook_obj._userID = "jikzu123"
    facebook_obj._Facebook__groups = 2138
    facebook_obj._followers = 132
    facebook_obj._likes = 9710 
    facebook_obj.is_influencer()
    assert facebook_obj._userID == "jikzu123"
    assert facebook_obj.is_influencer() == False

# Tiktok derived class methods
def test_post_statisitcs(tiktok_obj):
    tiktok_obj._Tiktok__watch_time = 206457
    tiktok_obj._Tiktok__views = 31236
    assert tiktok_obj.post_statistics() == 153890.7 

    tiktok_obj._Tiktok__watch_time = 6457
    tiktok_obj._Tiktok__views = 3123
    assert tiktok_obj.post_statistics() == 5456.8 