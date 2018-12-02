class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
def main():
    pt = Point(3.4,5)
    print("(", pt.x, ",", pt.y, ")", sep="")

main()
