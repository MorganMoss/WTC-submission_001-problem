def create_outline():    

    course_topics = {
        "Introduction to Python", "Tools of the Trade", 
        "How to make decisions", "How to repeat code", 
        "How to structure data", "Functions", "Modules"}

    problem_map = dict()

    student_progress = [
        ("Morgan", "Functions", "Problem 3", "[GRADED]"),
        ("Lee", "How to structure data", "Problem 1","[COMPLETED]"),
        ("Willa", "How to make decisions", "Problem 2", "[STARTED]")]

    course_topics = list(course_topics)
    course_topics.sort()

    def get_key(item):
        return item[3]
    student_progress.sort(key = get_key, reverse = True)


    print("Course Topics:")
    for topic in course_topics:
        print("* {0}".format(topic)) 
        problem_map[topic] = [
            "Problem 1", "Problem 2", "Problem 3"]

    print("Problems:")
    for topic, problems in problem_map.items():
        print("* {0} : ".format(topic), end="")
        print(*problems, sep = ", ")
    
    print("Student Progress:")
    for i, entry in enumerate(student_progress):
        print("{0}. {1[0]} - {1[1]} - {1[2]} - {1[3]}".format(i+1, entry))


if __name__ == "__main__":
    create_outline()
