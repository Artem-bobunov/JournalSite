from datetime import datetime


now = datetime.now().time()
dt_string =  now.strftime("%d.%m.%Y")


file = 'C:\JournalSite\journal_set\media\logger\log.txt'

class LoggerPasport:

    def __init__(self,users, numberACT):
        self.users = str(users)
        self.numberACT = str(numberACT)

    def add_record(self):
        with open(file, 'a') as f:
            f.writelines("Пользователь {} добавил запись под № акта {}, время: {} \n".format(self.users, self.numberACT,now))
            f.close()

    def update_record(self):
        with open (file,'a') as f:
            #for i in f.readline():
            f.writelines('Пользователь {} обновил запись под № акта {}. Дата: {}, время: {} \n '.format(self.users, self.numberACT,dt_string,now))
            f.close()
                #print("Пользователь {} обновил запись под № акта {}".format(self.users, self.number))

    def delete_record(self):
        with open(file, 'a') as f:
            f.write('Пользователь {} удалил запись под № акта {} \n'.format(self.users, self.numberACT))
            f.close()






