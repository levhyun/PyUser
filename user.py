import pymysql as db

connect = db.connect(host='localhost', user='root', password='2345s', db='pyuser', charset='utf8', autocommit=True, cursorclass=db.cursors.DictCursor)

class PyUser:
    def userSelect(self):
        try:
            handle = connect.cursor()
            sql = 'SELECT * FROM users;' 
            handle.execute(sql)
            result = handle.fetchall()
            handle.close()
            return result
        except:
            return -1

    def userLogin(self, id, pswd):
        Users =  self.userSelect()
        for user in Users:
            if id == user['userID'] and pswd == user["userPSWD"]:
                return "success"
        return "failure"
    
    def duplicateCheck(self, id, mail, Users):
        for user in Users:
            if id == user['userID'] or mail == user['userMAIL']:
                return "duplicate"
            
    def userSignup(self, id, mail, pswd):
        Users = self.userSelect()
        if self.duplicateCheck(id, mail, Users) == "duplicate":
            return "failure"
        handle = connect.cursor()
        sql = f'INSERT INTO users(userID, userMAIL, userPSWD) VALUES("{id}","{mail}","{pswd}");' 
        handle.execute(sql)
        handle.close()
        return "success"