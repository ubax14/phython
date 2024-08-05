def main():
    num_ist=int(input("enter a number of student"))
    cl_st_score(num_ist)
def cl_st_score(a):
    for i in range(a):
        sub1=int(input("enter the subjec1t:"))
        sub2=int(input("enter a number of subject2:"))
        sub3=int(input("enter a number of subject3:"))
        sub4=int(input("enter a number of subject4:"))
        sub5=int(input("enter a number of subject5:"))
        sub6=int(input("enter a number of subject6:"))
        total=sub1+sub2+sub3+sub4+sub5+sub6
        average=sub1+sub2+sub3+sub4+sub5+sub6%2
        print("the score of student is :",total,average)
main()


