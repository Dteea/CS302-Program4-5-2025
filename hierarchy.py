# Doney Tran
# 11/22/25
# CS302
# Program 4-5

import math
import emoji

# Core Hierarchy
class SocialMedia():
    # Default constructor
    def __init__(self, likes=0, dislikes=0, followers=0, userID=""):
        self._likes: int = likes 
        self._dislikes: int = dislikes
        self._followers: int = followers 
        self._userID: str = userID

    # This function displays the user's id and the protected data members. The function will return None to indicate success.
    def display(self) -> None:
        print("================")
        print(f"USER ID: {self._userID}\nLikes: {self._likes}\nDislikes: {self._dislikes}\nFollowers: {self._followers}")
        print("================")
        return None

    # This function uses the likes and followers of the user and throws it into an equation to generate a score. If the score
    # reaches a certain amount, then a special message is printed, otherwise a default message is printed. The function returns the
    # score calculated from the equation if successful, and returns a -1 if the numerator is being divided by zero.
    def recommend(self) -> float:
        try:

            # Equation to calculate custom score 
            score: float = round((self._likes / (self._followers)) + 0.1 * self._followers, 2)
            # Threshold for user to be recommended is at least a score of 100000
            if score >= 100000:
                print(f"{self._userID} with the score of {score} reached the threshold to be recommended.")

            else:
                print(f"{self._userID} with the score of {score} has not quite reach recommended yet. Maybe soon.")

            return score
        
        except ZeroDivisionError:
            print("Score cannot be calculated because it tried to divide by zero, followers needs to not be zero.")
            return -1.0

    # This function takes in the likes and dislikes to generate a rating for the user. It will return a rating that is rounded to 2 decimal places.
    # Otherwise this function returns a -1 indicating that the rating is being divided by 0.
    def rating(self) -> float:
        try:
            rating_ratio : float = round(self._likes / (self._likes + self._dislikes), 2)

            print(f"Rating of {self._userID} is {rating_ratio}.")

            return rating_ratio

        except ZeroDivisionError:
            print("rating cannot be generated because it tried to divide by zero.")
            return -1.0

    # This function uses likes, dislikes, and followers to generate a quality score. Depending on the score, special statements will be 
    # printed out. It will return the quality score rounded to 2 decimal places if successful, otherwise it will return a -1 indicating 
    # that the equation tried to divide by zero.
    def quality(self) -> float:
        try:
            quality_score: float = round((self._likes - self._dislikes) / (self._likes + self._dislikes) + (0.1 * math.log10(self._followers)), 2)
            if quality_score > 1:
                print(f"{self._userID} based on their stats, they should be a go to if they haven't been visited yet!")

            elif quality_score < 1:
                print(f"{self._userID} based on their stats, they should at least get a visit!") 

            elif quality_score < 0:
                print(f"{self._userID} based on their stats, they should not be visited at any cost!")

            print (f"Quality of {self._userID} is {quality_score}.")

            return quality_score

        except ZeroDivisionError:
            print("quality cannot be generated because it tried to divide by zero.")
            return -1.0

    # This function returns the user id as a string. 
    def get_user_id(self) -> str:
        return self._userID

class Facebook(SocialMedia):
    # Default constructor
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", groups=0, photos=0):
        super().__init__(likes, dislikes, followers, userID)
        self.__groups: int = groups 
        self.__photos: int = photos

    # This function displays the private data members of the facebook class and it's SocialMedia base class members. The FFFF's indicate that
    # the data members belong to the facebook object. It returns None if successful.
    def display(self)-> None:
        super().display()
        print("FFFFFFFFFFFFFFFF")
        print(f"Groups: {self.__groups}\nPhotos: {self.__photos}")
        print("FFFFFFFFFFFFFFFF")
        return None

    # This function checks to see if the groups and photo data members of the facebook object has reached a certain amount.
    # If so, the function adds on a fire emoji :fire: to the userID. It returns True if that was successful, otherwise a message 
    # is printed out and returns false.
    def upgrade_status(self) -> bool:
        is_upgraded: bool = False
        if self.__groups >= 1000 and self.__photos > 30000:
            self._userID += emoji.emojize(" :fire:")
            print(f"ID updated, your new ID is {self._userID}")
            is_upgraded = True

        else:
            print("You do not have the total required amount for both groups and photots to be upgraded.")
            is_upgraded = False

        return is_upgraded


    # This function uses groups, and followers to generate a ratio. It will return the ratio rounded to 2 decimal places
    # otherwise it will return a -1 indicating that the equation tried to divide by zero.
    def group_follower_ratio(self) -> float:
        try:
            ratio: float = round(self.__groups / self._followers, 2)

            print(f"The Ratio between group and followers of {self._userID} is {ratio}.")
            return ratio

        except ZeroDivisionError:
            print("Ratio could not be calculated from groups and followers because followers was zero")
            return -1.0

    # This function checks to see if the groups, followers, and likes of a user is past a certain amount. If it is
    # the function will append on the (Influencer) Tag to the userID. If the thresholds are not meant, a message is
    # displayed. The function will return True if the threshold was met, otherwise it will return False.
    def is_influencer(self) -> bool:
        status: bool = False 

        if self.__groups >= 5000 and self._followers >= 100000 and self._likes >= 1000000:
            print(f"Welcome to the influencer club {self._userID}! Enjoy your stay!")
            self._userID += " (Influencer)"
            status = True

        else:
            print(f"{self._userID} has not quite reach the numbers yet to be considered. Give it some more time")
            
        return status 

class Tiktok(SocialMedia):
    # Default constructor
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", watch_time=0, views=0):
        super().__init__(likes, dislikes, followers, userID)
        # Watch time is in minutes
        self.__watch_time: int = watch_time
        self.__views: int = views

    # This function calls the base class display and also display's the Tiktok data members. TTTT's indicate that the Tiktok data
    # members are being printed out. It will return None if successful.
    def display(self) -> None:
        super().display()
        print("TTTTTTTTTTTTTTTT")
        print(f"Watch Time in Minutes: {self.__watch_time}\nViews: {self.__views}")
        print("TTTTTTTTTTTTTTTT")
        return None

    # This function uses the watch time in minutes and views to throw in an equation to generate a score. If it reaches a certain
    # amount, a special message will be displayed depending on the score. It will return the score.
    def post_statistics(self) -> float:
        score: float = round((0.7 * self.__watch_time) + (0.3 * self.__views), 2)

        if score > 70000:
            print(f"{self._userID} is one popular fella!")

        elif score >= 20000 and score < 70000:
            print(f"{self._userID} is getting there with their posts.")

        elif score < 20000:
            print(f"{self._userID} posts fall a bit short.")

        print(f"Score for {self._userID} is {score}.")

        return score

    # Calculated in $USD
    # This function uses the watch time, view, like, and follower to determine the amount of money generated for a user.
    # The rates are listed below for each member. It will calculate the sum and return it rounded to 2 decimal places.
    def calculate_revenue(self) -> float:
        revenue_sum: float = 0
        # Watch time rate is 10 cents per minute
        watch_time_rate: float = (self.__watch_time * .10)

        # view rate is 5 cents per view
        view_rate: float  = (self.__views * .05)

        # like rate is 2 cents per like
        like_rate: float = (self._likes * .02)

        # follower rate is .1 cents per like
        follower_rate: float = (self._likes * .001)

        revenue_sum: float = round((watch_time_rate
                       + view_rate
                       + like_rate
                       + follower_rate), 2)

        print(f"{self._userID} estimated revenue from watch time, views, likes, and followers is:\n${revenue_sum}")        
        return revenue_sum

    # This function uses views and followers plugged into an equation to generate a ratio rounded down. It will return the
    # ratio calculated.
    def views_per_follower(self) -> int:
        try:
            ratio: int = math.floor(self.__views / self._followers)

            print(f"For every follower, there are about {ratio} views for {self._userID}")
            return ratio

        except ZeroDivisionError:
            print("Ratio could not be calculated from views and followers because followers was zero")
            return -1

class Instagram(SocialMedia):
    # Default constructor
    def __init__(self, likes=0, dislikes=0, followers=0, userID="", top_posts=0, posts=0, share=0):
        super().__init__(likes, dislikes, followers, userID)
        self.__top_posts: int = top_posts
        self.__posts: int = posts
        self.__share: int = share

    # This function calls the SocialMedia display and also display's Instagram's own data members. The IIII's indicate
    # the data members. The function returns None if successful.
    def display(self) -> None:
        super().display()
        print("IIIIIIIIIIIIIIII")
        print(f"Total Top Posts: {self.__top_posts}\nTotal Posts: {self.__posts}\nShares: {self.__share}")
        print("IIIIIIIIIIIIIIII")
        return None

    # This function generates a percentage of how many top posts they have relative to their total amount of posts.
    # It will return the ratio generated if successful, otherwise if the function tried to divide by zero, it will
    # return a -1.
    def post_ratio(self) -> float:
        try:
            top_post_ratio: float = round(self.__top_posts / self.__posts, 2)

            print(f"The percentage between top posts and posts of {self._userID} is %{top_post_ratio}")
            return top_post_ratio

        except ZeroDivisionError:
            print("Ratio could not be calculated because posts is 0")
            return -1.0

    # This function generates a score based off of the user's posts and likes.
    # It will return the ratio generated if successful, otherwise if the function tried to divide by zero, it will
    # return a -1.
    def post_like_ratio(self) -> float:
        try:
            score: float = round(self.__posts / self._likes, 2)

            print(f"The ratio between posts and likes of {self._userID} is {score}.")
            return score
            
        except ZeroDivisionError:
            print("Ratio could not be calculated due to likes being zero")
            return -1.0

    # This function generates a score based off the user's share and likes.
    # It will return the ratio generated if successful, otherwise if the function tried to divide by zero, it will
    # return a -1.
    def share_like_ratio(self) -> float:
        try:
            score: float = round(self.__share / self._likes, 2)

            print(f"The ratio between shares and likes of {self._userID} is {score}.")
            return score

        except ZeroDivisionError:
            print("Ratio could not be calculated due to likes being zero")
            return -1.0

# User/Client Interface
class Interface():
    # Default constructor
    def __init__(self):
        self.__list: list = list()

    # This helper function is used to check that all inputed integers are not negative and allows for numbers 0-MAX.
    # It will loop until the user sastifies those conditions and returns the correct inputed number
    def _validate_int(self, prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    raise ValueError("It cannot be negative and must be at least 0 or greater")
                return value

            except ValueError:
                print("Invalid Input, please try again.")

    # This helper function is used to check that all strings entered in is not empty and allows for any string. 
    # It will loop until the user sastifies those condition and return the correct inputed string.
    def _validate_str(self, prompt: str) -> int:
        while True:
            try:
                value = input(prompt)
                if value == "":
                    raise ValueError("User Id cannot be empty!")
                return value
                
            except ValueError:
                print("Invalid input, please try again.")

    # This function takes in a SocialMedia object and adds it to the interfaces list of SocialMedia objects. It will also
    # add the object to the 234 tree. It will return None if successful. 
    def add(self, data: SocialMedia) -> None:
        # When 234 Tree is implemented use this to add to the Tree
        print(f"Added {data.get_user_id()} to the List")
        self.__list.append(data)
        return None

    # This function shows a list of options for the user/client to interact with. Depending on what they select, the selected
    # function will be ran until the user/client enters a 0. It will give an exit message and return None if successful.
    def menu(self) -> None:
        choice: int = 20 
        while choice != 0:
            print("^^^^^^^^^^^^^^^^^^^\n")
            print("Welcome to the Social Media Analytics Tool! Please select from below!")
            print("1. Add Social Media user")
            print("2. Add Instagram user")
            print("3. Add Tiktok user")
            print("4. Add Facebook user")
            print("5. Display List")
            print("6. Search for user")
            print("7. ")

            print("0. Exit")
            print("^^^^^^^^^^^^^^^^^^^")
            choice = self._validate_int("Please select from the options for below on what you want to do :D\n")
            
            match choice:
                case 1:
                    self.__input(1)
                case 2:
                    self.__input(2)
                case 3:
                    self.__input(3)
                case 4:
                    self.__input(4)
                case 5:
                    self.display()
                case 0:
                    print("Exiting! Have a great day!")

                case _:
                    print("Invalid selection")
        return None

    # This function is the hub for inputs of different SocialMedia objects. Depending on the object, prompts will be shown for
    # the user/client to enter in manually. All inputs are validated by the protected helper functions listed above. It will return
    # None if successful.
    def __input(self, choice) -> None:


        name: str = self._validate_str("Please enter the UserID: ")
        likes: int = self._validate_int("Please enter the amount of likes they have: ") 
        dislikes: int = self._validate_int("Please enter the amount of dislikes they have: ")
        followers: int = self._validate_int("Please enter the amount of followers they have: ")

        # Social Media object
        if choice == 1:
            self.add(SocialMedia(likes, dislikes, followers, name))

        # Instagram Object
        elif choice == 2:
            top_posts: int = self._validate_int("Please enter the amount of top_posts they have: ") 
            posts: int = self._validate_int("Please enter the amount of posts they have: ")
            share: int = self._validate_int("Please enter the amount of sharing they have done: ")
            self.add(Instagram(likes, dislikes, followers, name, top_posts, posts, share))

        # Tiktok Object 
        elif choice == 3:
            watch_time: int = self._validate_int("Please enter the watch time amount they have in minutes: ")
            views: int = self._validate_int("Please enter the amount of views they have: ")
            self.add(Tiktok(likes, dislikes, followers, name, watch_time, views))

        # Facebook Object
        elif choice == 4:
            groups: int = self._validate_int("Please enter the amount of groups they have")
            photos: int = self._validate_int("Please enter the amount of photos they have: ")
            self.add(Tiktok(likes, dislikes, followers, name, groups, photos))

        return None

    # This function displays the SocialMedia objects that is currently in the interface list. It will display empty if there is nothing.
    # The function returns None if successful.
    def display(self) -> None:
        print("List of stored users:")
        if not self.__list:
            print("EMPTY")

        else:
            for objects in self.__list:
                objects.display()
                print("\n")

        return None

