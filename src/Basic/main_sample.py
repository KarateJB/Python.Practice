"""
What is if __name__ == '__main__' 
See http://blog.konghy.cn/2017/04/24/python-entry-program/
"""

from main_add import X,Y


print ("main_sample's __name__ = " + __name__)

def main():
    print('X*Y='+str(X*Y))

# main() 
if(__name__ == '__main__'):
    main()

