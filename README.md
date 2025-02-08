FileOrg

FileOrg is a Python-based file organization tool that sorts files into subfolders based on file type. With multi-language support (English, Spanish, French, Chinese Simplified, and Hindi), FileOrg offers features like dry-run mode, conflict resolution, and placeholders for managing file categories.
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

FileOrg is a menu-driven Python script designed to help you organize files within a specified folder. Files are automatically moved into subfolders based on their file type (for example, Text Files, Document Files, Image Files, etc.). The application supports multiple languages, making it accessible to a diverse audience.
Features

    Multi-Language Support:
    Interact with FileOrg in English, Spanish, French, Chinese Simplified, or Hindi. All messages and menu options are dynamically translated based on the selected language.

    File Organization:
    Automatically sorts files into subfolders according to their extensions. For example, files like .txt, .md, and .csv are grouped under "Text Files."

    Dry Run Mode:
    Preview the organization process without making any changes to your files.

    Conflict Resolution:
    Choose how to handle file name conflicts:
        Skip: Do not move files that conflict with an existing file.
        Rename: Automatically rename conflicting files (e.g., by appending _copy).

    File Category Management (Placeholder):
    Provides options for viewing, adding, and removing file categories (currently placeholders for future enhancements).

How It Works

FileOrg is structured into several key functions:

    notify_user(message_key)
    Displays messages in the selected language by retrieving translations from a predefined dictionary.

    user_menu()
    Presents a dynamically translated menu and handles user input. Options include organizing files, performing a dry run, changing language, and managing file categories.

    change_language()
    Allows users to switch the application's language. The function updates the language setting and confirms the change.

    organize_files_by_type(folder, dry_run, conflict_resolution)
    Walks through the specified folder, categorizes files based on their extensions, and either simulates (if dry run is enabled) or performs the file organization. Applies conflict resolution (skip or rename) when needed.

    main()
    Acts as the entry point. It continuously displays the menu and processes user selections until the exit option is chosen.

Installation

    Prerequisites:
        Python 3.6 or later is required.

    Clone the Repository:

git clone https://github.com/yourusername/FileOrg.git
cd FileOrg

Run FileOrg:

    python fileorg.py

Usage

    Start FileOrg:
    Run the script from your terminal. The program displays a menu with options translated based on your current language.

    Select an Option:
        Sort Files by Type:
        Organizes files into subfolders based on file extensions.
        Dry Run (Preview):
        Simulates the organization process without moving any files.
        Undo Last Operation:
        (Placeholder for future functionality)
        Multi-Folder Support:
        (Placeholder for future functionality)
        Restore Point / Update File Types:
        (Placeholders for future features)
        Change Language:
        Switch the interface language.
        Manage File Categories:
        View, add, or remove file categories (currently placeholders).
        Exit:
        Exits the application.

    During File Organization:
        Enter the folder path when prompted.
        Choose a conflict resolution method (skip or rename).
        (Note: Although "overwrite" is mentioned as an option, it is not implemented yet.)

Customization & Future Work

    Implement Overwrite Functionality:
    Add support to overwrite files when conflicts occur.

    Enhance Category Management:
    Develop the placeholders to dynamically view, add, or remove file categories. You could also integrate configuration storage using the json module.

    Improve Error Handling:
    Enhance robustness with additional error checking and logging.

    Additional Features:
    Consider adding an "undo" feature or more advanced file organization rules.

Contributing

Contributions are welcome! If you have suggestions, bug fixes, or new features, please open an issue or submit a pull request.
License

This project is licensed under the MIT License.
