"""# LAB_LAMBDA_RECURSION



## 1) Using recursion, if given a word/phrase return how many vowels(a,e,i,o,u) are in that phrase or word:

#### Note: the function should be able to count how many vowels no matter if it is lowercase or uppercase . 
#### Example: given the phrase `I love python` , it should return : `4` 


## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Hint: use map() with a lambda funciton

"""

def count_vowel(phrase:str):

    if len(phrase)==0 or phrase==None:
        return 0
    
    if phrase[0].lower() in ['o','a','i','e','u']:
        return 1 + count_vowel(phrase[1:])
    return count_vowel(phrase[1:])
    
print(count_vowel("I love python"))

old_list=[40,35, 10, 15, 20]
new_list=map(lambda number:number*number,old_list)
print(list(new_list))
