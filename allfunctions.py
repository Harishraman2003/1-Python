class allfunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
    def OddEven():
        num=int(input("Enter a number: "))
        if(num%2==0):
            print(num,"is Even number")
        else:
            print(num,"is odd number")
         
    def Eligible():
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if(gender=='Male'):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif(gender=='Female'):
            if(age>18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
                
    def Percentage():
        sub1=int(input("Subject1= "))
        sub2=int(input("Subject2= "))
        sub3=int(input("Subject3= "))
        sub4=int(input("Subject4= "))
        sub5=int(input("Subject5= "))
        print("Total: ",sub1+sub2+sub3+sub4+sub5)
        print("Percentage :",((sub1+sub2+sub3+sub4+sub5)/500)*100 )
        
    def Triangle():
        height1=int(input("Height:"))
        breadth1=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(height1*breadth1)/2)
        height2=int(input("Height1:"))
        height3=int(input("Height2:"))
        breadth2=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",height2+height3+breadth2)