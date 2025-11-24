class SocialMedia():
    def __init__(self, likes = 0, dislikes = 0, followers = 0, userID = ""):
        self._likes: int = likes 
        self._dislikes: int = dislikes
        self._followers: int = followers 
        self._userID: str = userID
    
    def display(self) -> None:
        print(f"Likes: {self._likes}\nDislikes: {self._dislikes}\nFollowers: {self._followers}\nUser ID: {self._userID}")

    def update(self, likes, dislikes, followers, userID) -> int:
        try:
            self._likes = int(likes)
            self._dislikes = int(dislikes)
            self._followers = int(followers)
            self._userID = str(userID)
            
             

        except ValueError:
            raise ValueError ("likes, dislikes, and followers has to be an integer")
        
        return 1
    
    def recommend() -> bool:
        pass
    
    def rating() -> int:
        pass

    def quality() -> int:
        pass
