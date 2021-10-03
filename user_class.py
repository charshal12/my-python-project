class User:
    # user attributes (information user has)
    def __init__(self, user_email, user_name, user_password, user_current_job_title):  # this is the constructor
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = user_current_job_title

    # user behaviour(an action user can perform)
    def change_password(self, new_password):  # Method
        self.password = new_password

    def change_job_title(self, new_job_title):  # Method
        self.current_job_title = new_job_title

    # def add_new_skill():
    def get_user_detail(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")

# This is moved to another file "post.py", as one file should be used only for creating class and another for data and objects
# # creating an object
# app_user_1 = User("tt@tt.com", "TT", "test123", "DevOps Engineer")
# app_user_1.get_user_detail()
#
# app_user_1.change_job_title("DevOps Trainer")
# app_user_1.get_user_detail()
#
# app_user_2 = User("ravi@citi.com", "Ravi", "test123", "Automation Engineer")
# app_user_2.get_user_detail()
#
# app_user_2.change_password("NewPassword123")
# app_user_2.get_user_detail()