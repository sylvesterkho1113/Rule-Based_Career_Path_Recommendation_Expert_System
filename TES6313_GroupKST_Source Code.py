# TES6313 Expert System
# EXS1 | 1B
# Title: Rule-based Career Path Recommendation Expert Systems for IT-related Job Seeker
# 242UT2449P See Chwan Kai
# 242UT2449Z Kho Wei Cong
# 242UT244B2 Tee Kian Hao
# 1221302254 ALGHANEM,HUSSAIN SALEH A

import clips 
import logging
import easygui
import re
import webbrowser # to open web
import smtplib # to send result to mailbox
from email.message import EmailMessage

# Setup working environment
logging.basicConfig(level=logging.INFO,format='%(message)s')
    
env = clips.Environment()
router = clips.LoggingRouter()
env.add_router(router)

# create template for suggested career (the result)
env.build("""
(deftemplate suggested_career
    (slot name))
""")

# 1 Junior Software Developer
env.build("""
(defrule Junior_Software_Developer
    (Enjoy_Programming Yes)
    (or (Edu_level Diploma)
        (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(> ?yoe 0))
    (personality $?p)
        (test (or (member$ "Keen to Learn" $?p)
        (member$ "Rational Thinking" $?p)))
    (skills $?s)
        (test (or (member$ "Python" $?s)
        (member$ "C Language" $?s)
        (member$ "Java" $?s)
        (member$ "Database" $?s)))
    =>
    (assert (suggested_career (name "Junior Software Developer")))
)
""")

# 2 Senior Software Developer
env.build("""
(defrule Senior_Software_Developer
    (Enjoy_Programming Yes)
    (Edu_level Master)
    (YOE ?yoe&:(>= ?yoe 3))
    (personality $?p)
        (test (or (member$ "Keen to Learn" $?p)
        (member$ "Rational Thinking" $?p)))
    (skills $?s)
        (test (or (member$ "Python" $?s)
        (member$ "C Language" $?s)
        (member$ "Java" $?s)
        (member$ "Database" $?s)))
    =>
    (assert (suggested_career (name "Senior Software Developer")))
)
""")

# 3 Data Scientist
env.build("""
(defrule Data_Scientist
    (Enjoy_Programming Yes)
    (or (Edu_level Diploma)
        (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Analytical Thinking" $?p)
                  (member$ "Math Knowledge" $?p)))
    (skills $?s)
        (test (or (member$ "Python" $?s)
                  (member$ "R" $?s)))
    =>
    (assert (suggested_career (name "Data Scientist")))
)
""")

# 4 Network Administrator
env.build("""
(defrule Network_Administrator
    (Enjoy_Programming No)
    (or (Edu_level Diploma)
        (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(>= ?yoe 1))
    (personality $?p)
        (test (or (member$ "Detail-Oriented" $?p)
                  (member$ "Problem-Solving" $?p)))
    (skills $?s)
        (test (or (member$ "Networking" $?s)
                  (member$ "Routing" $?s)
                  (member$ "Firewalls" $?s)))
    =>
    (assert (suggested_career (name "Network Administrator")))
)
""")

# 5 IT Support Specialist
env.build("""
(defrule IT_Support_Specialist
    (or (Edu_level Diploma)
        (Edu_level Degree)
        (Edu_level Master))
    =>
    (assert (suggested_career (name "IT Support Specialist")))
)
""")

# 6 Cybersecurity Analyst
env.build("""
(defrule Cybersecurity_Analyst
    (Enjoy_Programming No)
    (or (Edu_level Diploma)
        (Edu_level Degree))
    (YOE ?yoe&:(>= ?yoe 2))
    (personality $?p)
        (test (or (member$ "Problem-Solving" $?p)
                  (member$ "Detail-Oriented" $?p)))
    (skills $?s)
        (test (or (member$ "Network Security" $?s)
                  (member$ "Penetration Testing" $?s)))
    =>
    (assert (suggested_career (name "Cybersecurity Analyst")))
)
""")

# 7 Web Developer
env.build("""
(defrule Web_Developer
    (Enjoy_Programming Yes)
    (or (Edu_level Diploma)
        (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Creative" $?p)
                  (member$ "Keen to Learn" $?p)))
    (skills "HTML, CSS, JavaScript")
    =>
    (assert (suggested_career (name "Web Developer")))
)
""")

# 8 DevOps Engineer
env.build("""
(defrule DevOps_Engineer
    (Enjoy_Programming Yes)
    (Edu_level Degree)
    (YOE ?yoe&:(>= ?yoe 2))
    (personality $?p)
        (test (or (member$ "Team Player" $?p)
                  (member$ "Problem-Solving" $?p)))
    (skills "Python")
    =>
    (assert (suggested_career (name "DevOps Engineer")))
)
""")

# 9 Database Administrator
env.build("""
(defrule Database_Administrator
    (Enjoy_Programming No)
    (or (Edu_level Diploma)
        (Edu_level Degree))
    (YOE ?yoe&:(>= ?yoe 1))
    (personality $?p)
        (test (or (member$ "Detail-Oriented" $?p)
                  (member$ "Organized" $?p)))
    (skills "Database")
    =>
    (assert (suggested_career (name "Database Administrator")))
)
""")

# 10 Cloud Engineer
env.build("""
(defrule Cloud_Engineer
    (Enjoy_Programming Yes)
    (Edu_level Degree)
    (YOE ?yoe&:(>= ?yoe 2))
    (personality $?p)
        (test (or (member$ "Problem-Solving" $?p)
                  (member$ "Keen to Learn" $?p)))
    (skills $?s)
        (test (or (member$ "AWS" $?s)
                  (member$ "LINUX" $?s)))
    =>
    (assert (suggested_career (name "Cloud Engineer")))
)
""")

# 11 Artificial Intelligence Engineer
env.build("""
(defrule Artificial_Intelligence_Engineer
    (Enjoy_Programming Yes)
    (Edu_level Degree)
    (YOE ?yoe&:(>= ?yoe 1))
    (personality $?p)
        (test (or (member$ "Analytical Thinking" $?p)
                  (member$ "Innovative" $?p)))
    (skills $?s)
        (test (or (member$ "Python" $?s)
                  (member$ "Machine Learning" $?s)))
    =>
    (assert (suggested_career (name "Artificial Intelligence Engineer")))
)
""")

# 12 Mobile App Developer
env.build("""
(defrule Mobile_App_Developer
    (Enjoy_Programming Yes)
    (or (Edu_level Diploma)
        (Edu_level Degree))
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Creative" $?p)
                  (member$ "Keen to Learn" $?p)))
    (skills $?s)
        (test (or (member$ "SWIFT" $?s)
                  (member$ "Java" $?s)))
    =>
    (assert (suggested_career (name "Mobile App Developer")))
)
""")

# 13 UI/UX Designer
env.build("""
(defrule UI_UX_Designer
    (Enjoy_Programming No)
    (Edu_level Diploma)
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Creative" $?p)
                  (member$ "User-Focused" $?p)))
    (skills "FIGMA")
    =>
    (assert (suggested_career (name "UI/UX Designer")))
)
""")

# 14 IT Project Manager
env.build("""
(defrule IT_Project_Manager
    (Enjoy_Programming No)
    (Edu_level Master)
    (YOE ?yoe&:(>= ?yoe 5))
    (personality $?p)
        (test (or (member$ "Organized" $?p)
                  (member$ "Leadership" $?p)))
    (skills $?s)
        (test (or (member$ "Mircosoft Office" $?s)
                  (member$ "AGILE" $?s)))
    =>
    (assert (suggested_career (name "IT Project Manager")))
)
""")

# 15 Game Developer
env.build("""
(defrule Game_Developer
    (Enjoy_Programming Yes)
    (Edu_level Degree)
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Creative" $?p)
                  (member$ "Keen to Learn" $?p)))
    (skills $?s)
        (test (or (member$ "UNITY" $?s)
                  (member$ "C Language" $?s)))
    =>
    (assert (suggested_career (name "Game Developer")))
)
""")

# 16 Business Analyst
env.build("""
(defrule Business_Analyst
    (Enjoy_Programming No)
    (or (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(>= ?yoe 2))
    (personality $?p)
        (test (or (member$ "Analytical Thinking" $?p)
                  (member$ "Detail-Oriented" $?p)))
    (skills $?s)
        (test (or (member$ "Google Analytics" $?s)
                  (member$ "Power BI" $?s)))
    =>
    (assert (suggested_career (name "Business Analyst")))
)
""")

# 17 System Administrator
env.build("""
(defrule System_Administrator
    (Enjoy_Programming No)
    (or (Edu_level Diploma)
        (Edu_level Degree))
    (YOE ?yoe&:(>= ?yoe 1))
    (personality $?p)
        (test (or (member$ "Detail-Oriented" $?p)
                  (member$ "Problem-Solving" $?p)))
    (skills "LINUX")
    =>
    (assert (suggested_career (name "System Administrator")))
)
""")

# 18 IT Department Leader
env.build("""
(defrule IT_Department_Leader
    (Enjoy_Programming No)
    (Edu_level Master)
    (YOE ?yoe&:(>= ?yoe 3))
    (personality $?p)
        (test (or (member$ "Organized" $?p)
                  (member$ "Leadership" $?p)))
    (skills $?s)
        (test (or (member$ "Microsoft Office" $?s)
                  (member$ "PURECLOUD" $?s)))
    =>
    (assert (suggested_career (name "IT Department Leader")))
)
""")

# 19 Machine Learning Engineer
env.build("""
(defrule Machine_Learning_Engineer
    (Enjoy_Programming Yes)
    (or (Edu_level Degree)
        (Edu_level Master))
    (YOE ?yoe&:(>= ?yoe 1))
    (personality $?p)
        (test (or (member$ "Analytical Thinking" $?p)
                  (member$ "Keen to Learn" $?p)))
    (skills $?s)
        (test (or (member$ "Python" $?s)
                  (member$ "Machine Learning" $?s)))
    =>
    (assert (suggested_career (name "Machine Learning Engineer")))
)
""")

# 20 QA Engineer
env.build("""
(defrule QA_Engineer
    (Enjoy_Programming No)
    (or (Edu_level Diploma)
        (Edu_level Degree))
    (YOE ?yoe&:(>= ?yoe 0))
    (personality $?p)
        (test (or (member$ "Detail-Oriented" $?p)
                  (member$ "Rational Thinking" $?p)))
    (skills $?s)
        (test (member$ "Testing Tools" $?s))
    =>
    (assert (suggested_career (name "QA Engineer")))
)
""")

# Function to get user input with error handling
def get_user_input(prompt, title, choices=None, is_multiple=False):
    while True:
        if choices:
            if is_multiple:
                result = easygui.multchoicebox(prompt, title, choices)
            else:
                result = easygui.choicebox(prompt, title, choices)
        else:
            result = easygui.enterbox(prompt, title)

        if result is None or result == "":  # Handle cancel
            easygui.msgbox("You have cancel this program.", "Exit")
            exit()
        else:
            return result

# to get user's name        
def get_valid_name():
    while True:
        name = easygui.enterbox("Enter your name (alphabet characters only):", "User's Name")
        if name is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()
        if re.match("^[A-Za-z ]+$", name):  # Allow spaces for full names
            return name
        else:
            easygui.msgbox("Invalid name. Please enter alphabet characters only.", "Error")

# Function to get years of experience with validation
def get_years_of_experience():
    while True:
        years = easygui.enterbox("Enter your years of experience in the IT field (integer):", "Question 3")
        
        if years is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()
        
        if years.isdigit() and 0 <= int(years) <= 50:
            return int(years)  # Convert to integer
        else:
            easygui.msgbox("Please enter a valid number (integer 0-50).", "Invalid Input")

# Function to collect feedback and save to file
def collect_feedback():
    feedback = easygui.enterbox("Please provide your feedback or suggestions:", "Feedback")
    if feedback:
        with open("feedback.txt", "a") as file:
            file.write(feedback + "\n")
        easygui.msgbox("Thank you for your feedback!", "Feedback Received")
    else:
        easygui.msgbox("No feedback provided.", "Feedback")

# Function to send email
def send_email(result, uname, recipient_email):
    try:
        # Create the email message
        msg = EmailMessage()
        msg['Subject'] = f"Career Suggestion for {uname}"
        msg['From'] = f"Career Recommendation Expert System"
        msg['To'] = recipient_email
        msg.set_content(f"Hi {uname},\n\nThank you for taking career recommendation test with us.\n\nBased on your input, your suggested career is: {result}.\n\nBest regards,\nCareer Expert System")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login("chwankai09132@gmail.com", "hzir exlq bbpm dutd") 
            server.send_message(msg)

        easygui.msgbox(f"Email sent successfully to {recipient_email}!", "Success")
    except Exception as e:
        easygui.msgbox(f"Failed to send email. Error: {str(e)}", "Error")

# expert system function
def expert_system():

    while True:
        # clear the fact
        env.reset()
        # Input for the name
        uname = get_valid_name()

        # Selection for enjoying programming or not
        choice = ["Yes", "No"]
        prog = easygui.choicebox("Do you enjoy programming?", "Question 1", choice)

        if prog:
            env.assert_string(f"(Enjoy_Programming {prog})")
            
        if prog is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()

        # Selection for education level
        Edu = ["Diploma", "Degree", "Master"]
        certificate = easygui.choicebox("What is your education level?", "Question 2", Edu)

        if certificate:
            env.assert_string(f"(Edu_level {certificate})")
            
        if certificate is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()

        # Enter the years of experience in the IT field
        years = get_years_of_experience()
        env.assert_string(f"(YOE {years})")

        # Select personality traits
        per = ["Keen to Learn", "Detail-Oriented", "Organized", "Rational Thinking", "Problem-Solving",
            "Innovative", "Analytical Thinking Skill", "Creative", "User-focused", "Math Knowledge",
            "Team-Player", "Leadership"]
        personality = easygui.multchoicebox("Select the personality you have:", "Question 4", per)

        if personality:
            env.assert_string(f'(personality {" ".join([f"\"{p}\"" for p in personality])})')
            
        if personality is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()

        # Select equipped skills
        skills = ["Python", "Java", "Routing", "LINUX", "C language", "Database", "Firewalls", 
                "Machine Learning", "Network Security", "R", "HTML, CSS, JavaScript", "SWIFT", 
                "Penetrating Testing", "Networking", "AWS", "FIGMA", "AGILE", "UNITY", "Google Analytics",
                "PURECLOUD", "Microsoft Office", "Power BI", "Testing Tools"]
        skill_equipped = easygui.multchoicebox("Select the skills you have:", "Question 5", skills)

        if skill_equipped:
            env.assert_string(f'(skills {" ".join([f"\"{s}\"" for s in skill_equipped])}))')
            
        if skill_equipped is None:  # Handle cancel
            easygui.msgbox("You have canceled this program.", "Exit")
            exit()

        # run the fact
        env.run()

        # Retrieve suggested career name
        results = []
        for fact in env.facts():
            if fact.template.name == 'suggested_career':
                results.append(fact['name']) #Why assert the fact? 

        # Display results
        if results:
            # concatenate the recommended career
            result = ", ".join(results)
            
            # Display options to the user
            choice = easygui.buttonbox(f"Hi {uname}, based on your input, your suggested career is: {result}.", 
                                    "Result", 
                                    ["Send Result to Email", "Find Relevant Job Online", "Continue"])

            # if user wants to send result to email
            if choice == "Send Result to Email":
                recipient_email = easygui.enterbox("Enter the recipient's email address:", "Share via Email")
                if recipient_email:
                    send_email(result, uname, recipient_email)

            # if user wants to search job online
            elif choice == "Find Relevant Job Online":
                job_url = f"https://my.jobstreet.com/{result}-jobs"
                webbrowser.open(job_url)  # Opens the job URL in the default web browser
                easygui.msgbox(f"Your relevant job listings are opening in the browser.", "Job Listings")
                
        else:
            easygui.msgbox(f"Sorry {uname}, no suitable career suggestions were found based on your input.", "Result")

        # Ask user if they want to do it again
        if not easygui.ynbox("Do you want to try again?", "Do Again"):
            break

# main function here
while True:

    # index page
    choice = easygui.buttonbox("Welcome to the Career Expert System. Choose an option:", "Career Path Recommendation System", ["Expert System", "Feedback", "Exit"])

    if choice == "Expert System":
        expert_system()
    elif choice == "Feedback":
        collect_feedback()
    elif choice == "Exit":
        easygui.msgbox("Thank you for using the system!", "Goodbye")
        break
