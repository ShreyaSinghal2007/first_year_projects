
import string
def calculate_plagiarism(text1,text2):
    text1_clear1= text1.lower()
    text2_clear2= text2.lower()
    text1_clear= text1_clear1.translate(str.maketrans("","", string.punctuation))
    text2_clear= text2_clear2.translate(str.maketrans("","",string.punctuation))
    set1=set(text1_clear.split())
    set2=set(text2_clear.split())
    common_words=set1.intersection(set2)
    if(len(set2)==0):
        return 0
    percentage=(len(common_words)/len(set2))*100
    return round(percentage,2)
while True:
    print("\n"+"="*45)
    print("WELCOME TO ANTI- PLAGIARISM TOOL")
    print("="*45)
    print("1. Check Plagiarism")
    print("2. Exit")
    choice=input("Enter your choice(1 or 2):" )
    if choice== "1":
         
        with open("student1.txt","r") as file1:
          content1=file1.read()
        with open("student2.txt","r") as file2:
          content2=file2.read()
        result =calculate_plagiarism(content1,content2)
        print(f"plagiarism detected: {result}%")
        input("press enter after viewing the result...")
        
    elif choice== "2":

        print("Thankyou for using the tool. goodbye!!")
        input("press enter after viewing the result...")
    else:
        print("please choice 1 or 2")
        input("press enter after viewing the result...")
        



    
    


        

  








    
    


        

  





