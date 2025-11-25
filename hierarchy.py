import math
import emoji

class SocialMedia():
    def __init__(self, likes=0, dislikes=0, followers=0, userID=""):
        self._likes: int = likes 
        self._dislikes: int = dislikes
        self._followers: int = followers 
        self._userID: str = userID
    
    def display(self) -> None:
        print("================")
        print(f"USER ID: {self._userID}\nLikes: {self._likes}\nDislikes: {self._dislikes}\nFollowers: {self._followers}")
        print("================")
        return None

    def update(self, likes, dislikes, followers, userID) -> int:
        try:
            # Make sure arguments coming in are ints and the user ID being a string
            if isinstance(likes, int) and isinstance(dislikes, int) and isinstance(followers, int) and isinstance(userID, str):
                
                # Check if integers are negative and raise an exception
                if likes < 0 or dislikes < 0 or followers < 0:
                    raise ValueError("likes, dislikes, and followers cannot be negative")
                
                if userID == "":
                    raise ValueError("UserID cannot be empty.")

                self._likes = int(likes)
                self._dislikes = int(dislikes)
                self._followers = int(followers)
                self._userID = str(userID)
                
            else:
                raise ValueError("Variables passed in do not match. You have Invalid types somewhere.")

        except ValueError or TypeError:
            print("Update failed, please try again.")
            return -1

        return 1
    
    def recommend(self) -> float:
        try:
            # Equation to calculate custom score 
            score: float = (self._likes / (self._followers)) + 0.1 * self._followers 

            # Threshold for user to be recommended is at least a score of 100000
            if score >= 100000:
                print(f"{self._userID} with the score of {score} reached the threshold to be recommended.")

            else:
                print(f"{self._userID} with the score of {score} has not quite reach recommended yet. Maybe soon.")

            return score
        
        except ZeroDivisionError:
            raise ZeroDivisionError("Score cannot be calculated because it tried to divide by zero, followers needs to not be zero.")

    def rating(self) -> float:
        try:
            rating_ratio : float = self._likes / (self._likes + self._dislikes)

            print(f"Rating of {self._userID} is {rating_ratio}.")

            return rating_ratio

        except ZeroDivisionError:
            raise ZeroDivisionError("rating cannot be generated because it tried to divide by zero.")

    def quality(self) -> float:
        try:
            quality_score: float = (self._likes - self._dislikes) / (self._likes + self._dislikes) + (0.1 * math.log10(self._followers))

            print (f"Quality of {self._userID} is {quality_score}.")

            return quality_score

        except ZeroDivisionError:
            raise ZeroDivisionError("quality cannot be generated because it tried to divide by zero.")


class Facebook(SocialMedia):
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", groups=0, photos=0):
        super().__init__(likes, dislikes, followers, userID)
        self.__groups: int = groups 
        self.__photos: int = photos

    def display(self)-> None:
        super().display()
        print("FFFFFFFFFFFFFFFF")
        print(f"Groups: {self.__groups}\nPhotos: {self.__photos}")
        print("FFFFFFFFFFFFFFFF")
        return None

    def upgrade_status(self) -> bool:
        pass

    def group_follower_ratio(self) -> float:
        pass

    def is_influencer(self) -> bool:
        pass

class Tiktok(SocialMedia):
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", watch_time=0, views=0):
        super().__init__(likes, dislikes, followers, userID)
        self.__watch_time: int = watch_time
        self.__views: int = views

    def display(self) -> None:
        super().display()
        print("TTTTTTTTTTTTTTTT")
        print(f"Watch Time in Minutes: {self.__watch_time}\nViews: {self.__views}")
        print("TTTTTTTTTTTTTTTT")
        return None

    def post_statistics(self):
        pass

    def calculate_revenue(self):
        pass

    def warning(self):
        pass

    pass
class Instagram(SocialMedia):
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", top_posts=0, posts=0, share=0):
        super().__init__(likes, dislikes, followers, userID)
        self.__top_posts: int = top_posts
        self.__posts: int = posts
        self.__share: int = share
        pass

    def display(self) -> None:
        super().display()
        print("IIIIIIIIIIIIIIII")
        print(f"Total Top Posts: {self.__top_posts}\nTotal Posts: {self.__posts}\nShares: {self.__share}")
        print("IIIIIIIIIIIIIIII")
        return None
    
    def post_ratio(self):
        pass 

    def post_like_ratio(self):
        pass

    def share_like_ratio(self):
        pass

