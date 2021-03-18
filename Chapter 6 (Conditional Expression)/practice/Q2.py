# Write a programm to find out wheather a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input form.

sub1 = int(input("Enter the 1st mark: "))
sub2 = int(input("Enter the 2nd mark: "))
sub3 = int(input("Enter the 3rd mark: "))

if(sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail ! because you have less than 33% in one subject")
elif((sub1 + sub2 + sub3)/3 < 40):
    print("You are fail ! beacuse total percentage is less than 40%")
else:
    print("You are passed !!!")
