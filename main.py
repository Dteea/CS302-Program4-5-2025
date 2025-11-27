# Doney Tran
# 11/22/25
# CS302
# Program 4-5


import hierarchy as socialmedia
import numpy as np
def main():
    obj = socialmedia.SocialMedia()
    obj2 = socialmedia.Instagram(0,0,0,"",0,0,0)

    obj.update(20,30,40,"jeff")
    obj.display()

if __name__ == "__main__":
    main()