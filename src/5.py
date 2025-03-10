def get_project_info():
    # Get project name from user input
    project_name = input("Enter your project name: ")
    
    # Check if project name is valid
    while not project_name.isalpha():
        print("Invalid project name. Please enter a valid project name.")
        project_name = input("Enter your project name: ")
    
    # Get project description from user input
    project_description = input("Enter a brief description of your project: ")
    
    # Check if project description is valid
    while not project_description.isalpha():
        print("Invalid project description. Please enter a valid project description.")
        project_description = input("Enter a brief description of your project: ")
    
    # Get project goals from user input
    project_goals = input("Enter the goals of your project: ")
    
    # Check if project goals are valid
    while not project_goals.isalpha():
        print("Invalid project goals. Please enter a valid set of project goals.")
        project_goals = input("Enter the goals of your project: ")
    
    # Get project timeline from user input
    project_timeline = input("Enter the timeline for your project: ")
    
    # Check if project timeline is valid
    while not project_timeline.isalpha():
        print("Invalid project timeline. Please enter a valid set of project milestones.")
        project_timeline = input("Enter the timeline for your project: ")
    
    # Return project information as dictionary
    return {
        "project_name": project_name,
        "project_description": project_description,
        "project_goals": project_goals,
        "project_timeline": project_timeline
    }
