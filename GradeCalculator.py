import random


# Set Requirements for Each Grade (F Will be under the value of D)
A = 90
B = 80
C = 70
D = 60


StudentScore = random.randint(0,100) # Set Min / Max or Set Fixed Value for Student Grade




def CalculateGrade(score):
    GivenGrade = "F"
    if score >= A:
        GivenGrade = "A"
    elif score >= B:
        GivenGrade = "B"
    elif score >= C:
        GivenGrade = "C"
    elif score >= D:
        GivenGrade = "D"

    
    return(GivenGrade)


PrintStatementGrade = CalculateGrade(StudentScore)
print(f"Student Received The Grade {PrintStatementGrade} With A Score Of {StudentScore}!")

    
    


        


