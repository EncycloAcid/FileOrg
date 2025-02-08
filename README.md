File Organizer with Multi-language Support

A Python-based file organization tool that sorts files into subfolders based on file type. The application supports multiple languages (English, Spanish, French, Chinese Simplified, Hindi) and offers features such as a dry run mode, conflict resolution, and placeholder options for managing file categories.
Table of Contents

    Overview
    Features
    How It Works
    Installation
    Usage
    Customization & Future Work
    Contributing
    License

Overview

This project provides a menu-driven Python script that helps you organize files within a given folder. Files are automatically moved into subfolders according to their file type (e.g., Text Files, Document Files, Image Files). The application supports multiple languages so you can interact with the interface in your preferred language.
Features

    Multi-Language Support:
    The interface supports English, Spanish, French, Chinese Simplified, and Hindi. Messages and menu options are dynamically translated based on the current language setting.

    File Organization:
    Files are sorted into subfolders based on their extensions. For example, .txt, .md, and .csv files are grouped under "Text Files."

    Dry Run Mode:
    Preview the organization process without making any changes to your files.

    Conflict Resolution:
    Choose from different conflict resolution strategies when a file with the same name exists in the target folder:
        Skip: Do not move the conflicting file.
        Rename: Automatically rename the file (e.g., appending _copy).

    File Category Management (Placeholder):
    Options are provided for viewing, adding, and removing file categories. These functions are currently placeholders for future expansion.

How It Works

The script is structured into several key functions:

    notify_user(message_key)
    Displays messages to the user in the selected language by retrieving translations from a predefined dictionary.

    user_menu()
    Presents a dynamically translated menu to the user and handles input validation. Options include sorting files, performing a dry run, changing language, and managing file categories.

    change_language()
    Allows users to select and change the application language. The function updates the language setting and confirms the operation.

    organize_files_by_type(folder, dry_run, conflict_resolution)
    Walks through the specified folder, categorizes files based on their extensions, and either simulates (dry run) or performs the file organization. Conflict resolution (skip or rename) is applied when necessary.

    main()
    Acts as the entry point for the application. It continuously displays the menu and processes user selections until the exit option is chosen.

Installation

    Prerequisites:
        Python 3.6 or later is required.

    Clone the Repository:

git clone https://github.com/EncycloAcid/FileOrg.git
cd file-organizer

Run the Script:

    python organizer.py

    (Replace organizer.py with the actual filename if it’s different.)

Usage

    Start the Application:
    Run the script from your terminal. The program will display a menu with options (translated based on the current language).

    Select an Option:
        Sort Files by Type:
        Organizes files into subfolders.
        Dry Run (Preview):
        Simulates the organization process without moving any files.
        Undo Last Operation:
        Placeholder for undo functionality.
        Multi-Folder Support:
        Placeholder for organizing multiple folders.
        Restore Point / Update File Types:
        Placeholders for future features.
        Change Language:
        Switch the interface language.
        Manage File Categories:
        View, add, or remove file categories (currently placeholders).
        Exit:
        Exits the program.

    When Organizing Files:
        Enter the folder path when prompted.
        Choose a conflict resolution method (skip or rename).
        (Note: Although "overwrite" is mentioned, it is not yet implemented.)

Customization & Future Work

    Implement Overwrite:
    Add functionality to overwrite files when a conflict occurs.

    Enhance Category Management:
    Develop the placeholders to dynamically view, add, or remove file categories. Consider saving changes using the json module.

    Error Handling:
    Improve robustness by adding better error handling and logging.

    Additional Features:
    Consider adding an "undo" feature or more advanced organization rules.

Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new features, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
