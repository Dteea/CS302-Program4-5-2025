class SocialMedia():
    def __init__(self, likes = 0, dislikes = 0, followers = 0, userID = ""):
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
            if isinstance(likes, int) and isinstance(dislikes, int) and isinstance(followers, int) and isinstance(userID, str):

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

        except ValueError:
            print("Update failed, please try again.")
            return -1

        return 1
    
    def recommend() -> bool:
        pass
    
    def rating() -> int:
        pass

    def quality() -> int:
        pass

class Facebook(SocialMedia):
    pass
class Tiktok(SocialMedia):
    pass
class Instagram(SocialMedia):
    pass