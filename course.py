def create_outline():    
    "Manages data of and prints the outline of the course"
    # step 1 : using a set
    course_topics = {
        "Introduction to Python", "Tools of the Trade", 
        "How to make decisions", "How to repeat code", 
        "How to structure data", "Functions", "Modules"}

    # step 2 : using a dictionary
    problem_map = dict() # values are added later on

    # step 3 : using a list of tuples
    student_progress = [
        ("Morgan", "Functions", "Problem 3", "[GRADED]"),
        ("Lee", "How to structure data", "Problem 1","[COMPLETED]"),
        ("Willa", "How to make decisions", "Problem 2", "[STARTED]")]
    
    # step 4 : converting and sorting topics
    course_topics = list(course_topics)
    course_topics.sort()
    # step 4 : sorting student progress by state
    def get_key(item):  # sort key value needs a function
        return item[3]  # index 3 of the tuple holds the progress state 
    student_progress.sort(key = get_key, reverse = True)


    print("Course Topics:")     # printing step 1
    for topic in course_topics:
        print("* {0}".format(topic))

        '''
        Adding default values to each entry with key being topic below 
        Using the same for-loop used to print step 1
        '''
        problem_map[topic] = ["Problem 1", "Problem 2", "Problem 3"] 
             

    print("Problems:")          # printing step 2
    for topic, problems in problem_map.items():
        print("* {0} : ".format(topic), end="")
        print(*problems, sep = ", ")  
    
    print("Student Progress:")  # printing step 3
    for i, entry in enumerate(student_progress):
        print("{0}. {1[0]} - {1[1]} - {1[2]} - {1[3]}".format(i+1, entry)) 


if __name__ == "__main__":
    create_outline()
