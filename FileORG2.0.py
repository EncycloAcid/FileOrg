import os  # For file operations
import json
import sys
import time  # For timestamps and date formatting
from tqdm import tqdm  # For the progress bar


# Configure encoding for Unicode support
sys.stdout.reconfigure(encoding='utf-8')


# Helper functions for output management
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
def chat_support_interface():
    """
    Chat-like support interface for helping users understand features.
    """
    print("Welcome to the Support Bot! Ask a feature-related question.")
    print("Example queries:")
    print("- 'How can I sort videos by type and date?'")
    print("- 'What does Multi-Folder Support do?'")
    print("- 'How do I restore file types?'")
    print("- 'How do I change the language?'")
    print("\nType 'exit' to go back to the menu.\n")

    # Predefined support FAQs for menu items
    support_faqs = {
        "sort videos by type and date": (
            "The 'Sort videos by type and date' option organizes video files into subfolders based on their file type "
            "(e.g., MP4, AVI) and also groups them chronologically into folders by year/month/date. "
            "It's perfect for organizing videos in an orderly multimedia library."
        ),
        "multi-folder support": (
            "The 'Multi-Folder Support' option enables you to select multiple folders to sort and organize files at the same time. "
            "This is useful if you have several different source directories with mixed file types that need to be organized "
            "into a common structure."
        ),
        "restore point": (
            "The 'Restore Point/Update File Types' option allows you to manage file type recognition. For example, you can assign "
            "specific extensions (like '.csv', '.log') to the 'Documents' or 'Logs' category. It also ensures new file types "
            "are recognized during file organization in the future."
        ),
        "change language": (
            "The 'Change Language' option lets you switch between different supported languages for the user interface. "
            "This helps users who prefer working in a language other than the default (e.g., English to Spanish to French)."
        )
    }

    while True:
        # Ask the user for their question
        user_query = input("Ask your question: ").strip().lower()

        # Check if the user wants to exit
        if user_query in ["exit", "quit", "back"]:
            print("Exiting support. Returning to the main menu...")
            break

        # Find and respond to matching queries
        found_match = False
        for key, response in support_faqs.items():
            if key in user_query:
                print(f"\n💡 {response}\n")
                found_match = True
                break

        if not found_match:
            print(
                "❓ Sorry, I didn't understand that. Try asking about one of the menu options, such as 'Sort videos by type and date' or 'Multi-Folder Support'.\n"
            )

def pause_and_clear():
    """Waits for user input then clears the terminal screen."""
    input("Press Enter to continue...")
    clear_screen()


def count_files(folder):
    """
    Returns the total number of files in the given folder (including subdirectories).
    """
    count = 0
    for _, _, files in os.walk(folder):
        count += len(files)
    return count


# Language dictionary for supporting different languages (English, Spanish, French, Chinese Simplified, Hindi)
translations = {
    "en": {
        "choose_option": "Choose an option:",
        "invalid_input": "Invalid input. Please try again.",
        "exiting": "Exiting the program.",
        "operation_completed": "Operation completed successfully!",
        "undo_last_operation": "Undo Last Operation",
        "multi_folder_support": "Multi-Folder Support",
        "change_language": "Change Language",
        "manage_categories": "Manage File Categories",
        "sort_files": "Sort files by type (into subfolders)",
        "sort_files_by_date": "Sort files by type and by date",
        "sort_photos_videos_by_date": "Sort photos and videos by type and by date",
        "sort_photos_by_date": "Sort photos by type and by date",
        "sort_videos_by_date": "Sort videos by type and by date",
        "dry_run": "Dry run (Preview organization)",
        "exit": "Exit"
    },
    "es": {
        "choose_option": "Elige una opción:",
        "invalid_input": "Entrada no válida. Por favor, inténtalo de nuevo.",
        "exiting": "Saliendo del programa.",
        "operation_completed": "¡Operación completada con éxito!",
        "undo_last_operation": "Deshacer la última operación",
        "multi_folder_support": "Soporte para múltiples carpetas",
        "change_language": "Cambiar idioma",
        "manage_categories": "Gestionar categorías de archivos",
        "sort_files": "Ordenar archivos por tipo (en subcarpetas)",
        "sort_files_by_date": "Ordenar archivos por tipo y por fecha",
        "sort_photos_videos_by_date": "Ordenar fotos y vídeos por tipo y por fecha",
        "sort_photos_by_date": "Ordenar fotos por tipo y por fecha",
        "sort_videos_by_date": "Ordenar vídeos por tipo y por fecha",
        "dry_run": "Prueba (Previsualización de organización)",
        "exit": "Salir"
    },
    "fr": {
        "choose_option": "Choisissez une option :",
        "invalid_input": "Entrée invalide. Veuillez réessayer.",
        "exiting": "Quitte le programme.",
        "operation_completed": "Opération terminée avec succès !",
        "undo_last_operation": "Annuler la dernière opération",
        "multi_folder_support": "Prise en charge de plusieurs dossiers",
        "change_language": "Changer de langue",
        "manage_categories": "Gérer les catégories de fichiers",
        "sort_files": "Trier les fichiers par type (dans des sous-dossiers)",
        "sort_files_by_date": "Trier les fichiers par type et par date",
        "sort_photos_videos_by_date": "Trier les photos et vidéos par type et par date",
        "sort_photos_by_date": "Trier les photos par type et par date",
        "sort_videos_by_date": "Trier les vidéos par type et par date",
        "dry_run": "Essai (Aperçu de l'organisation)",
        "exit": "Quitter"
    },
    "zh": {
        "choose_option": "请选择一个选项：",
        "invalid_input": "输入无效。请再试一次。",
        "exiting": "正在退出程序。",
        "operation_completed": "操作成功完成！",
        "undo_last_operation": "撤销上一次操作",
        "multi_folder_support": "多文件夹支持",
        "change_language": "更改语言",
        "manage_categories": "管理文件类别",
        "sort_files": "按类型排序文件（到子文件夹）",
        "sort_files_by_date": "按类型和日期对文件进行排序",
        "sort_photos_videos_by_date": "按类型和日期对照片和视频进行排序",
        "sort_photos_by_date": "按类型和日期对照片进行排序",
        "sort_videos_by_date": "按类型和日期对视频进行排序",
        "dry_run": "试运行（预览组织）",
        "exit": "退出"
    },
    "hi": {
        "choose_option": "कोई विकल्प चुनें:",
        "invalid_input": "अमान्य इनपुट। कृपया फिर से प्रयास करें।",
        "exiting": "कार्यक्रम से बाहर निकल रहे हैं।",
        "operation_completed": "ऑपरेशन सफलतापूर्वक पूरा हुआ!",
        "undo_last_operation": "अंतिम क्रिया को पूर्ववत करें",
        "multi_folder_support": "मल्टी-फ़ोल्डर समर्थन",
        "change_language": "भाषा बदलें",
        "manage_categories": "फ़ाइल श्रेणियां प्रबंधित करें",
        "sort_files": "फ़ाइलों को प्रकार से क्रमबद्ध करें (सबसंकल्पनाओं में)",
        "sort_files_by_date": "फ़ाइलों को प्रकार और तारीख के अनुसार क्रमबद्ध करें",
        "sort_photos_videos_by_date": "फोटो और वीडियो को प्रकार और तारीख के अनुसार क्रमबद्ध करें",
        "sort_photos_by_date": "फोटो को प्रकार और तारीख के अनुसार क्रमबद्ध करें",
        "sort_videos_by_date": "वीडियो को प्रकार और तारीख के अनुसार क्रमबद्ध करें",
        "dry_run": "ड्राई रन (पूर्वावलोकन संगठन)",
        "exit": "बाहर निकलें"
    }
}

# Shared settings container
settings = {
    "language": "en"  # Default language
}

# File categories dictionary (used for sorting by type)
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
    "System Files": {".sys", ".dll", ".ini", ".log"}
}

# Global undo log to record file moves (for undo functionality)
undo_log = []


def notify_user(message_key):
    """
    Logs the localized message for the given message key.
    """
    current_language = settings["language"]
    print(translations[current_language].get(message_key, f"[ERROR: Missing translation for '{message_key}']"))


import time


def typing_animation(text, delay=0.01):
    """
    Displays a typing animation for the given text.
    :param text: The text to display with typing effect.
    :param delay: The delay (in seconds) between character prints (default: 0.05).
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)  # Add delay between characters
    print()  # Newline after typing effect


def user_menu():
    """
    Displays a boxed menu with purple text, icons, and a typing animation.
    """
    current_language = settings["language"]

    # Purple text in a box
    purple_color = "\033[95m"  # Purple text color
    reset_color = "\033[0m"  # Reset color
    border_color = "\033[94m"  # Blue for border

    # Icons for each menu option
    icons = {
        "sort_files": "📂",  # Folder
        "sort_files_by_date": "🗃️",  # File drawer
        "sort_photos_videos": "🖼️",  # Frame
        "sort_photos": "📸",  # Camera
        "sort_videos": "🎥",  # Video camera
        "undo_operation": "⏪",  # Undo
        "multi_folder": "📁",  # Multi-folder
        "restore_point": "🔄",  # Refresh
        "change_language": "🌐",  # Globe
        "manage_categories": "🗄️",  # Filing cabinet
        "Chat-like Support (Help)": "🤖",
            "exit": "❌"  # Exit
    }

    # Menu options with translations and icons
    menu_options = [
        f"1. {icons['sort_files']} {translations[current_language]['sort_files']}",
        f"2. {icons['sort_files_by_date']} {translations[current_language]['sort_files_by_date']}",
        f"3. {icons['sort_photos_videos']} {translations[current_language]['sort_photos_videos_by_date']}",
        f"4. {icons['sort_photos']} {translations[current_language]['sort_photos_by_date']}",
        f"5. {icons['sort_videos']} {translations[current_language]['sort_videos_by_date']}",
        f"6. {icons['undo_operation']} {translations[current_language]['undo_last_operation']}",
        f"7. {icons['multi_folder']} {translations[current_language]['multi_folder_support']}",
        f"8. {icons['restore_point']} Restore Point / Update File Types",
        f"9. {icons['change_language']} {translations[current_language]['change_language']}",
        f"10. {icons['manage_categories']} {translations[current_language]['manage_categories']}",
        f"11. 🤖 Chat-like Support (Help)",  # Added Help Bot Option
        f"12. {icons['exit']} {translations[current_language]['exit']}"
    ]

    # Typing Animation for Intro Text
    typing_animation("Welcome to the File Organizer!", delay=0.02)
    typing_animation("Select an option below:\n", delay=0.02)

    # Frame the menu with a box
    for option in menu_options:
        print(f"{purple_color}{option}{reset_color}")

    # Capturing user input
    try:
        choice = int(input("Enter your choice: ").strip())
        if choice not in range(1, 12):
            raise ValueError
        return choice
    except ValueError:
        notify_user("invalid_input")
        return None


def change_language():
    """
    Allows the user to change the application language.
    """
    notify_user("choose_option")
    print("Available languages:")
    print("1. English")
    print("2. Spanish (Español)")
    print("3. French (Français)")
    print("4. Chinese (中文)")
    print("5. Hindi (हिन्दी)")
    language_map = {"1": "en", "2": "es", "3": "fr", "4": "zh", "5": "hi"}
    language_choice = input("Enter the number of your choice: ").strip()
    if language_choice in language_map:
        settings["language"] = language_map[language_choice]
        notify_user("operation_completed")
    else:
        notify_user("invalid_input")


def organize_files_by_type(folder, dry_run, conflict_resolution):
    """
    Organizes files in a given folder into subfolders based on file types.
    Each file processed updates the progress bar.
    """
    total_files = count_files(folder)
    with tqdm(total=total_files, desc="Moving files", unit="file") as pbar:
        for root, _, files in os.walk(folder):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                category = next((key for key, exts in categories.items() if file_extension in exts), "Other Files")
                target_folder = os.path.join(folder, category)
                if dry_run:
                    print(f"[DRY RUN] {file} -> {target_folder}")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(target_folder, file)
                    if os.path.exists(target_path):
                        if conflict_resolution == "skip":
                            print(f"Skipping {file} (already exists)")
                            pbar.update(1)
                            continue
                        elif conflict_resolution == "rename":
                            base, ext = os.path.splitext(file)
                            target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                        elif conflict_resolution == "overwrite":
                            os.remove(target_path)
                    os.rename(source_path, target_path)
                    undo_log.append({"source": source_path, "target": target_path})
                pbar.update(1)


def organize_files_by_type_and_date(folder, dry_run, conflict_resolution):
    """
    Organizes files in a given folder into subfolders based on file type and modification date.
    Each file processed updates the progress bar.
    """
    total_files = count_files(folder)
    with tqdm(total=total_files, desc="Moving files", unit="file") as pbar:
        for root, _, files in os.walk(folder):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                category = next((key for key, exts in categories.items() if file_extension in exts), "Other Files")
                source_path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(source_path)
                except OSError:
                    print(f"Could not get modification time for {file}. Skipping.")
                    pbar.update(1)
                    continue
                date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
                target_folder = os.path.join(folder, category, date_str)
                if dry_run:
                    print(f"[DRY RUN] {file} -> {target_folder}")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    target_path = os.path.join(target_folder, file)
                    if os.path.exists(target_path):
                        if conflict_resolution == "skip":
                            print(f"Skipping {file} (already exists)")
                            pbar.update(1)
                            continue
                        elif conflict_resolution == "rename":
                            base, ext = os.path.splitext(file)
                            target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                        elif conflict_resolution == "overwrite":
                            os.remove(target_path)
                    os.rename(source_path, target_path)
                    undo_log.append({"source": source_path, "target": target_path})
                pbar.update(1)


def organize_photos_videos_by_type_and_date(folder, dry_run, conflict_resolution,
                                            manual_naming_photos=False, manual_naming_videos=False):
    """
    Organizes both photo and video files in a given folder into subfolders based on their file type and modification date.
    A progress bar is updated for each file encountered.
    """
    total_files = count_files(folder)
    photo_custom_names = {}
    video_custom_names = {}
    with tqdm(total=total_files, desc="Moving files", unit="file") as pbar:
        for root, _, files in os.walk(folder):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                source_path = os.path.join(root, file)

                # Process Image Files
                if file_extension in categories["Image Files"]:
                    category = "Image Files"
                    try:
                        mtime = os.path.getmtime(source_path)
                    except OSError:
                        print(f"Could not get modification time for {file}. Skipping.")
                        pbar.update(1)
                        continue
                    default_date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
                    if manual_naming_photos:
                        if default_date_str not in photo_custom_names:
                            custom_name = input(
                                f"Enter custom folder name for photos with date {default_date_str} (or press Enter to use default): "
                            ).strip()
                            photo_custom_names[default_date_str] = custom_name if custom_name else default_date_str
                        chosen_date_folder = photo_custom_names[default_date_str]
                    else:
                        chosen_date_folder = default_date_str

                    target_folder = os.path.join(folder, category, chosen_date_folder)
                    if dry_run:
                        print(f"[DRY RUN] {file} -> {target_folder}")
                    else:
                        os.makedirs(target_folder, exist_ok=True)
                        target_path = os.path.join(target_folder, file)
                        if os.path.exists(target_path):
                            if conflict_resolution == "skip":
                                print(f"Skipping {file} (already exists)")
                                pbar.update(1)
                                continue
                            elif conflict_resolution == "rename":
                                base, ext = os.path.splitext(file)
                                target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                            elif conflict_resolution == "overwrite":
                                os.remove(target_path)
                        os.rename(source_path, target_path)
                        undo_log.append({"source": source_path, "target": target_path})

                # Process Video Files
                elif file_extension in categories["Video Files"]:
                    category = "Video Files"
                    try:
                        mtime = os.path.getmtime(source_path)
                    except OSError:
                        print(f"Could not get modification time for {file}. Skipping.")
                        pbar.update(1)
                        continue
                    default_date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
                    if manual_naming_videos:
                        if default_date_str not in video_custom_names:
                            custom_name = input(
                                f"Enter custom folder name for videos with date {default_date_str} (or press Enter to use default): "
                            ).strip()
                            video_custom_names[default_date_str] = custom_name if custom_name else default_date_str
                        chosen_date_folder = video_custom_names[default_date_str]
                    else:
                        chosen_date_folder = default_date_str

                    target_folder = os.path.join(folder, category, chosen_date_folder)
                    if dry_run:
                        print(f"[DRY RUN] {file} -> {target_folder}")
                    else:
                        os.makedirs(target_folder, exist_ok=True)
                        target_path = os.path.join(target_folder, file)
                        if os.path.exists(target_path):
                            if conflict_resolution == "skip":
                                print(f"Skipping {file} (already exists)")
                                pbar.update(1)
                                continue
                            elif conflict_resolution == "rename":
                                base, ext = os.path.splitext(file)
                                target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                            elif conflict_resolution == "overwrite":
                                os.remove(target_path)
                        os.rename(source_path, target_path)
                        undo_log.append({"source": source_path, "target": target_path})
                # Skip files that are not photos or videos.
                pbar.update(1)


def organize_photos_by_type_and_date(folder, dry_run, conflict_resolution, manual_naming_photos=False):
    """
    Organizes only photo files in a given folder into subfolders based on modification date.
    A progress bar is updated for each file encountered.
    """
    total_files = count_files(folder)
    photo_custom_names = {}
    with tqdm(total=total_files, desc="Moving files", unit="file") as pbar:
        for root, _, files in os.walk(folder):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension not in categories["Image Files"]:
                    pbar.update(1)
                    continue  # Process only photos
                source_path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(source_path)
                except OSError:
                    print(f"Could not get modification time for {file}. Skipping.")
                    pbar.update(1)
                    continue
                default_date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
                if manual_naming_photos:
                    if default_date_str not in photo_custom_names:
                        custom_name = input(
                            f"Enter custom folder name for photos with date {default_date_str} (or press Enter to use default): "
                        ).strip()
                        photo_custom_names[default_date_str] = custom_name if custom_name else default_date_str
                    chosen_date_folder = photo_custom_names[default_date_str]
                else:
                    chosen_date_folder = default_date_str

                target_folder = os.path.join(folder, "Image Files", chosen_date_folder)
                if dry_run:
                    print(f"[DRY RUN] {file} -> {target_folder}")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    target_path = os.path.join(target_folder, file)
                    if os.path.exists(target_path):
                        if conflict_resolution == "skip":
                            print(f"Skipping {file} (already exists)")
                            pbar.update(1)
                            continue
                        elif conflict_resolution == "rename":
                            base, ext = os.path.splitext(file)
                            target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                        elif conflict_resolution == "overwrite":
                            os.remove(target_path)
                    os.rename(source_path, target_path)
                    undo_log.append({"source": source_path, "target": target_path})
                pbar.update(1)


def organize_videos_by_type_and_date(folder, dry_run, conflict_resolution, manual_naming_videos=False):
    """
    Organizes only video files in a given folder into subfolders based on modification date.
    A progress bar is updated for each file encountered.
    """
    total_files = count_files(folder)
    video_custom_names = {}
    with tqdm(total=total_files, desc="Moving files", unit="file") as pbar:
        for root, _, files in os.walk(folder):
            for file in files:
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension not in categories["Video Files"]:
                    pbar.update(1)
                    continue  # Process only videos
                source_path = os.path.join(root, file)
                try:
                    mtime = os.path.getmtime(source_path)
                except OSError:
                    print(f"Could not get modification time for {file}. Skipping.")
                    pbar.update(1)
                    continue
                default_date_str = time.strftime("%Y-%m-%d", time.localtime(mtime))
                if manual_naming_videos:
                    if default_date_str not in video_custom_names:
                        custom_name = input(
                            f"Enter custom folder name for videos with date {default_date_str} (or press Enter to use default): "
                        ).strip()
                        video_custom_names[default_date_str] = custom_name if custom_name else default_date_str
                    chosen_date_folder = video_custom_names[default_date_str]
                else:
                    chosen_date_folder = default_date_str

                target_folder = os.path.join(folder, "Video Files", chosen_date_folder)
                if dry_run:
                    print(f"[DRY RUN] {file} -> {target_folder}")
                else:
                    os.makedirs(target_folder, exist_ok=True)
                    target_path = os.path.join(target_folder, file)
                    if os.path.exists(target_path):
                        if conflict_resolution == "skip":
                            print(f"Skipping {file} (already exists)")
                            pbar.update(1)
                            continue
                        elif conflict_resolution == "rename":
                            base, ext = os.path.splitext(file)
                            target_path = os.path.join(target_folder, f"{base}_copy{ext}")
                        elif conflict_resolution == "overwrite":
                            os.remove(target_path)
                    os.rename(source_path, target_path)
                    undo_log.append({"source": source_path, "target": target_path})
                pbar.update(1)


def undo_last_operation():
    """
    Reverses the file moves recorded in the undo_log.
    """
    if not undo_log:
        print("No operations to undo.")
        return
    # Process in reverse order to undo moves correctly
    for move in reversed(undo_log):
        source = move["source"]
        target = move["target"]
        if os.path.exists(target):
            os.rename(target, source)
            print(f"Restored {target} to {source}")
        else:
            print(f"File {target} not found; skipping undo for this file.")
    undo_log.clear()
    notify_user("operation_completed")


def multi_folder_support(dry_run, conflict_resolution):
    """
    Organizes files in multiple folders.
    Prompts the user to enter comma-separated folder paths and processes each folder.
    """
    folders_input = input("Enter the folder paths to organize (separated by commas): ").strip()
    folders = [folder.strip() for folder in folders_input.split(",") if folder.strip()]
    for folder in folders:
        if not os.path.isdir(folder):
            print(f"Folder '{folder}' is invalid. Skipping.")
            continue
        if dry_run:
            print(f"[DRY RUN] Preview organization for folder: {folder}")
        else:
            print(f"Organizing folder: {folder}")
        organize_files_by_type(folder, dry_run, conflict_resolution)


def restore_point_update_file_types():
    """
    Presents a submenu for creating a restore point or updating file type categories.
    """
    print("1. Create Restore Point")
    print("2. Update File Types")
    sub_choice = input("Enter your choice: ").strip()
    if sub_choice == "1":
        folder = input("Enter the folder path to create a restore point: ").strip()
        if not os.path.isdir(folder):
            notify_user("invalid_input")
            return
        file_list = []
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                file_list.append(file_path)
        restore_point = {
            "folder": folder,
            "files": file_list,
            "timestamp": time.ctime()
        }
        with open("restore_point.json", "w", encoding="utf-8") as f:
            json.dump(restore_point, f, indent=4)
        print("Restore point created and saved to 'restore_point.json'.")
    elif sub_choice == "2":
        print("Current categories and their extensions:")
        for cat, exts in categories.items():
            print(f"{cat}: {', '.join(exts)}")
        print("1. Add Category")
        print("2. Remove Category")
        print("3. Update Category (Add/Remove Extensions)")
        update_choice = input("Enter your choice: ").strip()
        if update_choice == "1":
            new_cat = input("Enter new category name: ").strip()
            new_exts = input("Enter file extensions for this category (comma-separated): ").split(',')
            new_exts = {ext.strip() for ext in new_exts if ext.strip()}
            if new_cat in categories:
                print("Category already exists.")
            else:
                categories[new_cat] = new_exts
                print(f"Category '{new_cat}' added.")
        elif update_choice == "2":
            del_cat = input("Enter the category name to remove: ").strip()
            if del_cat in categories:
                del categories[del_cat]
                print(f"Category '{del_cat}' removed.")
            else:
                print("Category not found.")

        elif update_choice == "3":
            upd_cat = input("Enter the category name to update: ").strip()
            if upd_cat in categories:
                print(f"Current extensions for '{upd_cat}': {', '.join(categories[upd_cat])}")
                action = input("Do you want to add or remove extensions? (add/remove): ").strip().lower()
                if action == "add":
                    new_ext = input("Enter new extensions to add (comma-separated): ").split(',')
                    new_ext = {ext.strip() for ext in new_ext if ext.strip()}
                    categories[upd_cat].update(new_ext)
                    print("Extensions added.")
                elif action == "remove":
                    rem_ext = input("Enter extensions to remove (comma-separated): ").split(',')
                    rem_ext = {ext.strip() for ext in rem_ext if ext.strip()}
                    categories[upd_cat] = {ext for ext in categories[upd_cat] if ext not in rem_ext}
                    print("Extensions removed.")
                else:
                    print("Invalid action.")
            else:
                print("Category not found.")
        else:
            notify_user("invalid_input")
    else:
        notify_user("invalid_input")


def main():
    """
    Main function for FileOrg.
    Provides a menu-driven interface with the following options:
      1. Sort Files by Type
      2. Sort Files by Type and by Date
      3. Sort Photos and Videos by Type and by Date
      4. Sort Photos by Type and by Date
      5. Sort Videos by Type and by Date
      6. Undo Last Operation
      7. Multi-Folder Support
      8. Restore Point / Update File Types
      9. Change Language
      10. Manage File Categories
      11. Exit
    """
    while True:
        choice = user_menu()  # Show the menu and get the user choice
        if choice is None:
            continue
        elif choice == 11:  # Help Bot Option
            chat_support_interface()

            choice = user_menu()  # Show the menu and get the user choice
        if choice == 11:  # Exit
            notify_user("exiting")
            break
        elif choice == 9:  # Change Language
            change_language()
        elif choice == 10:  # Manage File Categories
            print("\nFile Category Management")
            print("1. View Categories")
            print("2. Add Category")
            print("3. Remove Category")
            sub_choice = input("Enter your choice: ").strip()
            if sub_choice == "1":
                print("Current Categories:")
                for cat, exts in categories.items():
                    print(f"{cat}: {', '.join(exts)}")
            elif sub_choice == "2":
                new_cat = input("Enter new category name: ").strip()
                new_exts = input("Enter file extensions (comma-separated): ").split(',')
                new_exts = {ext.strip() for ext in new_exts if ext.strip()}
                categories[new_cat] = new_exts
                print(f"Category '{new_cat}' added.")
            elif sub_choice == "3":
                del_cat = input("Enter category name to remove: ").strip()
                if del_cat in categories:
                    del categories[del_cat]
                    print(f"Category '{del_cat}' removed.")
                else:
                    print("Category not found.")
            else:
                notify_user("invalid_input")
        elif choice == 6:  # Undo Last Operation
            undo_last_operation()
        elif choice == 7:  # Multi-Folder Support
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            multi_folder_support(dry_run, conflict_resolution)
        elif choice == 8:  # Restore Point / Update File Types
            restore_point_update_file_types()
        elif choice == 1:  # Sort Files by Type
            folder = input("Enter the folder path to organize: ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            if dry_run:
                print(f"[DRY RUN] Preview organization for folder: {folder}")
            else:
                print(f"Organizing folder: {folder}")
            organize_files_by_type(folder, dry_run, conflict_resolution)
        elif choice == 2:  # Sort Files by Type and by Date
            folder = input("Enter the folder path to organize: ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            if dry_run:
                print(f"[DRY RUN] Preview organization for folder: {folder}")
            else:
                print(f"Organizing folder: {folder}")
            organize_files_by_type_and_date(folder, dry_run, conflict_resolution)
        elif choice == 3:  # Sort Photos and Videos by Type and by Date (combined)
            folder = input("Enter the folder path to organize (Photos and Videos only): ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            manual_photos_input = input("Manually name each date folder for photos? (y/n): ").strip().lower()
            manual_videos_input = input("Manually name each date folder for videos? (y/n): ").strip().lower()
            manual_naming_photos = (manual_photos_input == "y")
            manual_naming_videos = (manual_videos_input == "y")
            if dry_run:
                print(f"[DRY RUN] Preview organization for folder: {folder}")
            else:
                print(f"Organizing folder: {folder}")
            organize_photos_videos_by_type_and_date(folder, dry_run, conflict_resolution,
                                                    manual_naming_photos, manual_naming_videos)
        elif choice == 4:  # Sort Photos by Type and by Date (photos only)
            folder = input("Enter the folder path to organize (Photos only): ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            manual_photos_input = input("Manually name each date folder for photos? (y/n): ").strip().lower()
            manual_naming_photos = (manual_photos_input == "y")
            if dry_run:
                print(f"[DRY RUN] Preview organization for folder: {folder}")
            else:
                print(f"Organizing folder: {folder}")
            organize_photos_by_type_and_date(folder, dry_run, conflict_resolution, manual_naming_photos)
        elif choice == 5:  # Sort Videos by Type and by Date (videos only)
            folder = input("Enter the folder path to organize (Videos only): ").strip()
            if not os.path.isdir(folder):
                notify_user("invalid_input")
                continue
            conflict_resolution = input("Choose conflict resolution (skip, rename, overwrite): ").strip().lower()
            dry_run_input = input("Perform a dry run? (y/n): ").strip().lower()
            dry_run = (dry_run_input == "y")
            manual_videos_input = input("Manually name each date folder for videos? (y/n): ").strip().lower()
            manual_naming_videos = (manual_videos_input == "y")
            if dry_run:
                print(f"[DRY RUN] Preview organization for folder: {folder}")
            else:
                print(f"Organizing folder: {folder}")
            organize_videos_by_type_and_date(folder, dry_run, conflict_resolution, manual_naming_videos)

        notify_user("operation_completed")
        pause_and_clear()  # Wait for user input and then clear the screen


if __name__ == "__main__":
    main()
