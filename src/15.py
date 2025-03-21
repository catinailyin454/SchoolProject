def main():
    # Initialize variables
    user_input = ""
    
    # Main loop
    while True:
        print("\nWelcome to SchoolProject!")
        print("1. Create a new project")
        print("2. View existing projects")
        print("3. Search for projects by keywords or name")
        print("4. Edit existing project details")
        print("5. Delete project details")
        print("0. Exit program")

        # Take user input
        choice = input("\nChoose an option: ")

        if choice == "1":
            create_new_project()
        elif choice == "2":
            view_projects()
        elif choice == "3":
            search_for_projects_by_keyword_or_name()
        elif choice == "4":
            edit_project_details()
        elif choice == "5":
            delete_project_details()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def create_new_project():
    project_name = input("\nPlease enter the name of your new project: ")
    description = input(f"\n{project_name} - Enter a brief description: ")
    status = input(f"{project_name} - Status (draft, in progress): ")

    print("\nProject details:")
    print(f"Name: {project_name}")
    print(f"Description: {description}")
    print(f"Status: {status}")

def view_projects():
    projects = []
    
    # Fetching all projects and their details
    for project in get_all_projects():
        projects.append(project)
        
    print("\nProject list:")
    for i, project in enumerate(projects):
        print(f"{i+1}. {project[0]} - {project[2]}")

def search_for_projects_by_keyword_or_name():
    keyword = input("Enter a keyword or name to search: ")
    
    projects = get_projects_by_keyword_or_name(keyword)
    if not projects:
        print("\nNo matching projects found.")
    else:
        display_projects(projects)

def edit_project_details():
    project_name = input("Enter the project's name to edit details: ")
    
    for project in get_all_projects():
        if project[0] == project_name:
            edit_details(project)
            break

def delete_project_details():
    project_name = input("\nPlease enter the project name you want to delete: ")

    for index, project in enumerate(get_all_projects()):
        if project[0] == project_name:
            del get_all_projects()[index]
            break
