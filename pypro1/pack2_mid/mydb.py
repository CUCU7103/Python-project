import pickle
 
config = {
    
    'host':'127.0.0.1',
    'user':'root',
    'password':'time@less6805',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True

}

with open ('mydb.dat', mode='wb') as obj:
    pickle.dump(config,obj) # 저장