class EmployeeRecords:
    def __init__(self, n, i, r):
        self.n = n
        self.i = i
        self.r = r
def main():
   rec = EmployeeRecords("Mary", 2148, 10.50)
   print(rec.n,"",rec.i,"",rec.r)
main()
