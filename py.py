score = 0

print("WELCOME TO PYTHON MCQ QUIZ")
print("Each correct answer gives 1 mark\n")

# Question 1
print("1. What is the output of: print(2 + 3 * 4)?")
print("A) 20  B) 14  C) 24  D) 10")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 2
print("\n2. Which symbol is used for comments in Python?")
print("A) //  B) #  C) /* */  D) --")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 3
print("\n3. What is the output of: print(10 // 3)?")
print("A) 3.33  B) 3  C) 4  D) Error")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 4
print("\n4. Which keyword is used for decision making?")
print("A) for  B) while  C) if  D) loop")
ans = input("Answer: ")
if ans.upper() == "C":
    score += 1

# Question 5
print("\n5. What is the output of: print(5 == 5)?")
print("A) True  B) False  C) 5  D) Error")
ans = input("Answer: ")
if ans.upper() == "A":
    score += 1

# Question 6
print("\n6. Which operator is used for AND?")
print("A) &  B) and  C) &&  D) AND")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 7
print("\n7. What is the output of: print(not True)?")
print("A) True  B) False  C) Error  D) None")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 8
print("\n8. Which operator is used for remainder?")
print("A) /  B) //  C) %  D) **")
ans = input("Answer: ")
if ans.upper() == "C":
    score += 1

# Question 9
print("\n9. What is the output of: print(type(5))?")
print("A) int  B) float  C) str  D) class")
ans = input("Answer: ")
if ans.upper() == "D":
    score += 1

# Question 10
print("\n10. Which keyword is used for multiple conditions?")
print("A) else if  B) elif  C) elseif  D) ifelse")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 11
print("\n11. What is the output of: print(3 > 2 and 2 > 1)?")
print("A) True  B) False  C) Error  D) None")
ans = input("Answer: ")
if ans.upper() == "A":
    score += 1

# Question 12
print("\n12. Which operator checks equality?")
print("A) =  B) ==  C) !=  D) <=")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 13
print("\n13. What is the output of: print(bool(0))?")
print("A) True  B) False  C) 0  D) Error")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 14
print("\n14. Which function is used to take input?")
print("A) read()  B) scan()  C) input()  D) get()")
ans = input("Answer: ")
if ans.upper() == "C":
    score += 1

# Question 15
print("\n15. What is the output of: print(2 ** 3)?")
print("A) 6  B) 8  C) 9  D) Error")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 16
print("\n16. Which operator means OR?")
print("A) ||  B) or  C) |  D) OR")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 17
print("\n17. What is the output of: print(5 != 5)?")
print("A) True  B) False  C) Error  D) None")
ans = input("Answer: ")
if ans.upper() == "B":
    score += 1

# Question 18
print("\n18. Which operator is used for greater than?")
print("A) <  B) <=  C) >  D) ==")
ans = input("Answer: ")
if ans.upper() == "C":
    score += 1

# Question 19
print("\n19. What is the output of: print(4 >= 4)?")
print("A) True  B) False  C) Error  D) None")
ans = input("Answer: ")
if ans.upper() == "A":
    score += 1

# Question 20
print("\n20. Which statement is used to exit from if block?")
print("A) break  B) continue  C) pass  D) end")
ans = input("Answer: ")
if ans.upper() == "C":
    score += 1

print("\nQUIZ COMPLETED!")
print("Your Total Score:", score, "/20")
