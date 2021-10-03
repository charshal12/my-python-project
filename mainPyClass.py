from post import Post
from post1 import Post1
from user_class import User

app_user_1 = User("tt@tt.com", "TT", "test123", "DevOps Engineer")
#app_user_1.get_user_detail()

app_user_2 = User("ravi@citi.com", "Ravi", "test123", "Automation Engineer")
#app_user_2.get_user_detail()

new_post = Post1("On  a secret mission today", app_user_2.name)
#new_post.get_post_info()

#commented as we are using it in mainPyClass.py file