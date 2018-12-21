#Employee Simple Database

class EmployeeRecord:
    def __init__(self,n,i,r):
        self.name = n
        self.id=i
        self.pay_rate=r
def open_database(filename, db):
    lines = open(filename)
    for line in lines:
        name, id, pay_rate = eval(line)
        db.append(EmployeeRecord(name,id,pay_rate))
    return True

def print_database(db):
    for rec in db:
        print(rec.name ," ", rec.id , " ", rec.pay_rate)

def by_name(n1,n2):
    if n1.name > n2.name:
        return 1
    else:
        return 0

def by_id(n1,n2):
    if n1.id > n2.id:
        return 1
    else:
        return 0

def by_pay_rate(n1,n2):
    if n1.pay_rate > n2.pay_rate:
        return 1
    else:
        return 0
        
def sort(db, sort_by_function):
    for i in range(0,len(db)-1):
        for j in range(i+1,len(db)):
            if sort_by_function(db[i],db[j]) > 0:
                db[i],db[j]=db[j],db[i]

def main():
    db = []
    open_database("data.dat", db)
    sort(db, by_name)
    print_database(db)
    print("----------------")
    sort(db, by_id)
    print_database(db)
    print("----------------")
    sort(db, by_pay_rate)
    print_database(db)
main()
