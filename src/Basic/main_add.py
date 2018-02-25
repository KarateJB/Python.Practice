"""
What is if __name__ == '__main__' 
See http://blog.konghy.cn/2017/04/24/python-entry-program/
"""

print ("main_add's __name__ = " + __name__)

X = 10
Y = 20

def main():
    print('X+Y='+str(X+Y))

# main()
if __name__ == "__main__":
    main()
