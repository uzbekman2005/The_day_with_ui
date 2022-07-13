from signup import *


class Person:
    def __init__(self, u_id):
        self.u_id = u_id
        self.db_connection()
        self.selectTheUser()

    def db_connection(self):
        try:
            self.connection = pymysql.connect(host=host, user=user, password=password,
                                              charset="utf8mb4", port=port, database=database,
                                              cursorclass=pymysql.cursors.DictCursor)
        except Exception as ex:
            print(ex)
    def selectTheUser(self):
        try:
            sql = f"SELECT  * from users where user_id = {self.u_id}"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
                self.human = cursor.fetchall()[0]

        except Exception as ex:
            print(ex)

    def get_f_name(self):
        return self.human["u_fname"]

    def get_l_name(self):
        return self.human["u_lname"]

    def get_score(self):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM users where user_id = {self.u_id}"
                cursor.execute(sql)
                self.human = cursor.fetchall()[0]
            return self.human["score"]
        except Exception as ex:
            print(ex)

    def get_gender(self):
        return self.human["u_gender"]

    def get_email(self):
        return self.human["u_email"]

    def get_username(self):
        return self.human["u_username"]

    def get_userID(self):
        return int(self.u_id)

    def setScore(self, score):
        try:
            sql = f"update users set score = {score + self.get_score()}"
            with self.connection.cursor() as cursor:
                cursor.execute(sql)
        except Exception as ex:
            print(ex)
        finally:
            self.connection.commit()

# def main():
#     man = Person(1)
#     man.selectTheUser()
#     print(man.get_username())
#     print(man.get_f_name())
#     print(man.get_email())
#     print(man.get_score())

# if __name__ == '__main__':
#     main()