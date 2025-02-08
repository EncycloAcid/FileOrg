import os  # For file operations
import json
import sys

# Configure encoding for Unicode support
sys.stdout.reconfigure(encoding='utf-8')

# Language dictionary for supporting different languages (English, Spanish, French, Chinese Simplified, Hindi)
translations = {
    "en": {
        "choose_option": "Choose an option:",
        "invalid_input": "Invalid input. Please try again.",
        "exiting": "Exiting the program.",
        "operation_completed": "Operation completed successfully!",
        "undo_last_operation": "Undo Last Operation",
        "restore_point": "Restore Point",
        "update_file_types": "Update File Types",
        "exit": "Exit",
        "change_language": "Change Language",
        "manage_categories": "Manage File Categories",
        "sort_files": "Sort files by type (into subfolders)",
        "dry_run": "Dry run (Preview organization)",
        "multi_folder_support": "Multi-Folder Support"
    },
    "es": {
        "choose_option": "Elige una opción:",
        "invalid_input": "Entrada no válida. Por favor, inténtalo de nuevo.",
        "exiting": "Saliendo del programa.",
        "operation_completed": "¡Operación completada con éxito!",
        "undo_last_operation": "Deshacer la última operación",
        "restore_point": "Punto de restauración",
        "update_file_types": "Actualizar los tipos de archivo",
        "exit": "Salir",
        "change_language": "Cambiar idioma",
        "manage_categories": "Gestionar categorías de archivos",
        "sort_files": "Ordenar archivos por tipo (en subcarpetas)",
        "dry_run": "Prueba (Previsualización de organización)",
        "multi_folder_support": "Soporte para múltiples carpetas"
    },
    "fr": {
        "choose_option": "Choisissez une option :",
        "invalid_input": "Entrée invalide. Veuillez réessayer.",
        "exiting": "Quitte le programme.",
        "operation_completed": "Opération terminée avec succès !",
        "undo_last_operation": "Annuler la dernière opération",
        "restore_point": "Point de restauration",
        "update_file_types": "Mettre à jour les types de fichiers",
        "exit": "Quitter",
        "change_language": "Changer de langue",
        "manage_categories": "Gérer les catégories de fichiers",
        "sort_files": "Trier les fichiers par type (dans des sous-dossiers)",
        "dry_run": "Essai (Aperçu de l'organisation)",
        "multi_folder_support": "Prise en charge de plusieurs dossiers"
    },
    "zh": {
        "choose_option": "请选择一个选项：",
        "invalid_input": "输入无效。请再试一次。",
        "exiting": "正在退出程序。",
        "operation_completed": "操作成功完成！",
        "undo_last_operation": "撤销上一次操作",
        "restore_point": "还原点",
        "update_file_types": "更新文件类型",
        "exit": "退出",
        "change_language": "更改语言",
        "manage_categories": "管理文件类别",
        "sort_files": "按类型排序文件（到子文件夹）",
        "dry_run": "试运行（预览组织）",
        "multi_folder_support": "多文件夹支持"
    },
    "hi": {
        "choose_option": "कोई विकल्प चुनें:",
        "invalid_input": "अमान्य इनपुट। कृपया फिर से प्रयास करें।",
        "exiting": "कार्यक्रम से बाहर निकल रहे हैं।",
        "operation_completed": "ऑपरेशन सफलतापूर्वक पूरा हुआ!",
        "undo_last_operation": "अंतिम क्रिया को पूर्ववत करें",
        "restore_point": "पुनर्स्थापना बिंदु",
        "update_file_types": "फ़ाइल प्रकार अपडेट करें",
        "exit": "बाहर निकलें",
        "change_language": "भाषा बदलें",
        "manage_categories": "फ़ाइल श्रेणियां प्रबंधित करें",
        "sort_files": "फ़ाइलों को प्रकार से क्रमबद्ध करें (सबसंकल्पनाओं में)",
        "dry_run": "ड्राई रन (पूर्वावलोकन संगठन)",
        "multi_folder_support": "मल्टी-फ़ोल्डर समर्थन"
    }
}

# Shared settings container
settings = {
    "language": "en"  # Default language
}

categories = {
    "Text Files": {".txt", ".md", ".csv"},
    "Document Files": {".docx", ".pdf", ".pptx", ".xlsx"},
    "Image Files": {".jpg", ".png", ".gif", ".bmp", ".tiff"},
    "Audio Files": {".mp3", ".wav", ".aac", ".flac"},
    "Video Files": {".mp4", ".avi", ".mkv", ".mov"},
    "Compressed Files": {".zip", ".rar", ".tar", ".7z"},
    "Executable Files": {".exe", ".bat", ".sh"},
    "Code Files": {".html", ".css", ".js", ".py", ".java", ".cpp"},
    "Database Files": {".sql", ".db", ".mdb"},
    "System Files": {".sys", ".dll", ".ini", ".log"},
}


def notify_user(message_key):
    """
    Logs the localized message for the given message key by retrieving the correct
    translation based on the current system language setting.

    If the translation for the provided key is missing in the current language,
    the function will print an error message indicating the absence of the
    translation.

    :param message_key: The key representing the message to be localized and
        displayed. This is used to fetch the corresponding translation.
    :type message_key: str
    :return: None
    """
    current_language = settings["language"]
    print(translations[current_language].get(message_key, f"[ERROR: Missing translation for '{message_key}']"))


def user_menu():
    """
    Displays the user menu and handles user input for selecting menu options. The function
    translates menu elements dynamically based on the current language, prompts the user
    for their choice, validates the input, and returns the user's choice or None if the
    input is invalid. Options include managing files, settings, and configurations.

    :return: An integer representing the user's valid choice between 1 and 9, or
        ``None`` if the input is invalid.
    :rtype: int | None
    """
    notify_user("choose_option")

    current_language = settings["language"]
    menu_options = [
        f"1. {translations[current_language]['sort_files']}",
        f"2. {translations[current_language]['dry_run']}",
        f"3. {translations[current_language]['undo_last_operation']}",
        f"4. {translations[current_language]['multi_folder_support']}",
        f"5. {translations[current_language]['restore_point']}",
        f"6. {translations[current_language]['update_file_types']}",
        f"7. {translations[current_language]['change_language']}",
        f"8. {translations[current_language]['manage_categories']}",
        f"9. {translations[current_language]['exit']}"
    ]

    for option in menu_options:
        print(option)

    try:
        choice = int(input("Enter your choice: ").strip())
        if choice not in range(1, 10):
            raise ValueError
        return choice
    except ValueError:
        notify_user("invalid_input")
        return None


def change_language():
    """
    Function to allow the user to select and change the application language. Provides a list of
    language options and updates the application's settings based on the user's selection. If the
    user input is invalid, a notification is displayed to inform them of the invalid input.

    :raises KeyError: If the `settings` dictionary is not properly initialized or the
       "language" key is missing.
    :raises ValueError: If the input provided by the user does not correspond to any valid
       language option in the defined `language_map`.
    """
    notify_user("choose_option")  # Use translated message for "Choose an option"
    print("Available languages:")
    print("1. English")
    print("2. Spanish (Español)")
    print("3. French (Français)")
    print("4. Chinese (中文)")
    print("5. Hindi (हिन्दी)")

    # Map numeric inputs to language codes
    language_map = {"1": "en", "2": "es", "3": "fr", "4": "zh", "5": "hi"}

    # Prompt user and handle choice
    language_choice = input("Enter the number of your choice: ").strip()
    if language_choice in language_map:
        settings["language"] = language_map[language_choice]
        notify_user("operation_completed")  # Notify user of successful operation
    else:
        notify_user("invalid_input")  # Notify user about invalid input


def organize_files_by_type(folder, dry_run, conflict_resolution):
    """
    Organizes files in a given folder into subfolders based on the file types.

    The function traverses through a specified folder, categorizes files based on
    their extensions, and organizes them into specific subfolders named by the
    categories. If `dry_run` is enabled, the function will only simulate the
    reorganization process without making actual changes. File name conflicts during
    the organization can be handled by either skipping the conflicting files or by
    renaming them as specified by the `conflict_resolution` parameter.

    :param folder: The root folder path where files are organized.
    :type folder: str
    :param dry_run: If True, simulates the organization process without making
        changes.
    :type dry_run: bool
    :param conflict_resolution: Specifies the method to resolve filename conflicts.
        Accepts "skip" to avoid moving conflicting files or "rename" to rename
        duplicate files.
    :type conflict_resolution: str
    :return: None
    :rtype: NoneType
    """
    for root, _, files in os.walk(folder):
        for file in files:
            file_extension = os.path.splitext(file)[1].lower()
            category = next((key for key, exts in categories.items() if file_extension in exts), "Other Files")
            target_folder = os.path.join(folder, category)

            if dry_run:  # Show what would happen
                print(f"[DRY RUN] {file} -> {target_folder}")
            else:
                os.makedirs(target_folder, exist_ok=True)

                # Handle file conflicts
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_folder, file)

                if os.path.exists(target_path):
                    if conflict_resolution == "skip":
                        print(f"Skipping {file} (already exists)")
                        continue
                    elif conflict_resolution == "rename":
                        base, ext = os.path.splitext(file)
                        target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                os.rename(source_path, target_path)


def main():
    """
    Main function for managing the file organization system. This function provides a
    menu-driven interface that allows the user to perform various actions including
    exiting the program, changing language, managing file categories, or organizing files
    in a selected folder. It also allows users to handle conflict resolution options while
    organizing files.

    The menu supports the following options:
    - Exit the program.
    - Change the application's language.
    - Manage existing file categories, including viewing, adding, and removing categories.
    - Organize files within a specified folder, including a preview mode for changes.

    This function acts as the entry point for the program execution and handles the main
    user interaction logic in a loop until the user opts to exit.

    :param: None

    :return: None
    """
    while True:
        choice = user_menu()  # Show the menu and get user choice
        if choice is None:
            continue

        if choice == 9:  # Exit
            notify_user("exiting")
            break
        elif choice == 7:  # Change Language
            change_language()  # Call the updated change_language() function
        elif choice == 8:  # Manage File Categories
            print("\nFile Category Management")
            print("1. View Categories")
            print("2. Add Category")
            print("3. Remove Category")
            sub_choice = input("Enter your choice: ").strip()

            if sub_choice == "1":
                print("List categories functionality placeholder")
            elif sub_choice == "2":
                print("Add category functionality placeholder")
            elif sub_choice == "3":
                print("Remove category functionality placeholder")
            else:
                notify_user("invalid_input")
        else:
            folder = input("Enter the folder path to organize: ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue

            conflict_resolution = input("Choose conflict resolution: (skip, rename, overwrite): ").strip()
            dry_run = (choice == 2)

            if not dry_run:
                print(f"Organizing folder: {folder}")
            else:
                print(f"[DRY RUN] Preview organization for folder: {folder}")

            organize_files_by_type(folder, dry_run, conflict_resolution)

        notify_user("operation_completed")


if __name__ == "__main__":
    main()
