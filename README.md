# FileOrg
1. Imports and Initial Setup

    Modules Imported:
        os: For file and directory operations.
        json: (Imported but not used in the current snippet—possibly intended for future enhancements such as saving configuration.)
        sys: To adjust system-level settings, like output encoding.

    Encoding Configuration:
        sys.stdout.reconfigure(encoding='utf-8') ensures that Unicode characters (from languages like Chinese and Hindi) are handled properly when printing to the console.

2. Multi-Language Support

    Translations Dictionary:
        A dictionary named translations contains localized strings for each supported language. Each language (identified by its language code such as "en" for English, "es" for Spanish, etc.) has its own dictionary mapping keys (like "choose_option", "invalid_input", etc.) to the appropriate translated messages.

    Settings:
        The settings dictionary holds application-wide settings, currently with one key: "language", which defaults to English ("en").

3. File Categories

    Categories Dictionary:
        The categories dictionary maps category names (e.g., "Text Files", "Document Files") to a set of file extensions. These are used later to determine into which subfolder a file should be moved based on its extension.
        If a file's extension is not found in any category, it is grouped under "Other Files".

4. Key Functions
a. notify_user(message_key)

    Purpose:
    Displays a message to the user in the currently selected language.

    Mechanism:
        Retrieves the current language from settings.
        Uses the translations dictionary to get the corresponding string for the provided message_key.
        If the translation is missing, it prints an error message indicating the missing key.

b. user_menu()

    Purpose:
    Displays a menu with several options (such as sorting files, performing a dry run, changing language, etc.) and prompts the user to make a selection.

    Features:
        The menu options are dynamically translated based on the current language.
        It validates that the user input is an integer between 1 and 9.
        Returns the user's choice or None if the input is invalid.

c. change_language()

    Purpose:
    Provides a mechanism for the user to change the application's language.

    Features:
        Lists the available languages.
        Maps a numeric input (from 1 to 5) to a language code.
        Updates the settings["language"] accordingly.
        Uses notify_user to inform the user whether the operation was successful or if the input was invalid.

d. organize_files_by_type(folder, dry_run, conflict_resolution)

    Purpose:
    Organizes files by moving them into subfolders named according to file categories.

    Functionality:
        Uses os.walk to recursively traverse the provided folder.
        For each file, the script extracts its file extension and determines its category (or defaults to "Other Files" if no match is found).
        Dry Run Mode:
            If dry_run is set to True, it only prints out what actions it would perform (e.g., showing which file would go into which folder) without making any changes.
        Conflict Resolution:
            If a file with the same name already exists in the target folder, the script can either:
                Skip: Do not move the file.
                Rename: Append _copy to the filename.
                (Although "overwrite" is mentioned in the prompt for conflict resolution, it is not explicitly implemented in the code.)

e. main()

    Purpose:
    Serves as the entry point and manages the overall flow of the program.

    Features:
        Runs an infinite loop where it repeatedly shows the menu and processes the user's selection.
        Options Include:
            Option 9: Exit the program.
            Option 7: Change the application's language by calling change_language().
            Option 8: Manage file categories (currently a placeholder for viewing, adding, or removing categories).
            Other Options:
            For other menu choices, the user is prompted to provide:
                A folder path to organize.
                A method for conflict resolution (e.g., "skip" or "rename").
                Whether to perform a dry run (if the selected option corresponds to dry run).
        After completing an operation, it notifies the user that the operation was completed successfully.

    Program Exit:
    When the user selects the exit option, it prints an exit message (localized) and breaks out of the loop.

    Script Execution:
    The if __name__ == "__main__": block ensures that main() runs when the script is executed as a standalone program.

5. Overall Workflow

    Startup:
    The program starts, configures Unicode output, and defaults to English.

    User Menu Display:
    The user is presented with a menu of options that are dynamically translated based on the current language setting.

    User Interaction:
        The user can choose to:
            Organize files by type (with options for a dry run and conflict resolution).
            Change the application's language.
            Manage file categories (currently as placeholders).
            Exit the program.

    File Organization:
        When organizing files, the user provides a folder path.
        Files are then categorized by their extension and either moved to the corresponding subfolder (if not a dry run) or just previewed (if a dry run is selected).

    Operation Completion:
    After each operation, the user is notified of its successful completion.
