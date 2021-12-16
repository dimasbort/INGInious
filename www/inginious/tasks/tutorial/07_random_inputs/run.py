#Dummy example of ipython script to evaluate student answer for equation: 2x²-Value=0
import math

#Get the random input parameter and select a predifined value based on it
randomIndex=int(float(get_input("@random")[0]*100))%6
values = [8, 18, 32, 50, 72, 98]
value=values[randomIndex]

#Get the student answer and the correct answer
student = int(get_input("student_code"))
solution = int(math.sqrt(value/2))

#As an example, the two answers can be accessed from command line via temporary environment variables
#This is useful if you want to share the same variable for python commands and bash commands
%env MY_SOLUTION=$solution
%env STUDENT_SOLUTION=$student

#Compare student solution and correct solution.
#This could be implemeneted in python but here it uses bash for the Ipython example
! if [ "$STUDENT_SOLUTION" = "$MY_SOLUTION" ]; then feedback-result success; else feedback-result failed; fi
