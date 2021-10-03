from user_class import User


class Post:
    # creating an object
    app_user_1 = User("tt@tt.com", "TT", "test123", "DevOps Engineer")
    app_user_1.get_user_detail()

    app_user_1.change_job_title("DevOps Trainer")
    app_user_1.get_user_detail()

    app_user_2 = User("ravi@citi.com", "Ravi", "test123", "Automation Engineer")
    app_user_2.get_user_detail()

    app_user_2.change_password("NewPassword123")
    app_user_2.get_user_detail()
