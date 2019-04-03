import operator  # importing operator module for sorting.
inputString = "" #initializing input text.
count = 0;       #initializing count.
punctuations = ["." ,",", ":" ,";" ,"'" ,"\"" ,")" ,"(" ,"?" ,"!"] #initializing punctuations as given in the question.

#Defining function to take user input and store it.
def get_string(inputString):
    inputString = input("Enter a text:\n")
    return inputString

#Defining function to find the punctuation count.
def punctuation_count(inputString, count):
    #iterating through the string.
    for i in inputString:
        #checking for punctuations.
        for p in punctuations:
            if (i == p):
               count += 1 #incrementing count.
    print("Total number of punctuations in this text is: " + str(count))

#Defining function to find kth frequent word.    
def top_frequent(inputString):
    k = input("Enter a number")
    no_punct = ""
    #Iteration for removing punctuations from the text.
    for char in inputString:
         if char not in punctuations:
                no_punct = no_punct + char
    no_punct = no_punct.lower() # converting text to lower case.
    words = no_punct.split()    # splitting into individual words based on white space.
    Dict = {} # initializing empty dictionary.
    # iterating through all the words and keeping count of frequency.
    for w in words:
        if w in Dict:
            Dict[w] += 1
        else:
            Dict[w] = 1
    # sorting based on frequency in decreasing order.        
    sorted_d = sorted(Dict.items(), key=operator.itemgetter(1),reverse=True)
    print(sorted_d[int(k)-1]) # printing kth most frequent word.


    
inputString = get_string(inputString) # calling the function get_string.

punctuation_count(inputString, count) # calling the function punctuation_count.

top_frequent(inputString)             # calling the function top_frequent.
