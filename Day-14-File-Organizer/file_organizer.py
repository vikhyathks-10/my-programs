import os
import shutil


class FileOrganizer:

    def __init__(self, folder_path):

        self.folder_path = folder_path

        self.file_categories = {
            "Images": [
                ".jpg",
                ".jpeg",
                ".png",
                ".gif",
                ".bmp",
                ".webp"
            ],

            "Documents": [
                ".pdf",
                ".doc",
                ".docx",
                ".txt",
                ".ppt",
                ".pptx"
            ],

            "Spreadsheets": [
                ".xls",
                ".xlsx",
                ".csv"
            ],

            "Videos": [
                ".mp4",
                ".mkv",
                ".avi",
                ".mov",
                ".webm"
            ],

            "Audio": [
                ".mp3",
                ".wav",
                ".aac",
                ".flac"
            ],

            "Archives": [
                ".zip",
                ".rar",
                ".7z",
                ".tar",
                ".gz"
            ]
        }


    # ======================================
    # CREATE CATEGORY FOLDERS
    # ======================================

    def create_folders(self):

        for category in self.file_categories:

            folder = os.path.join(
                self.folder_path,
                category
            )

            os.makedirs(
                folder,
                exist_ok=True
            )


        others_folder = os.path.join(
            self.folder_path,
            "Others"
        )

        os.makedirs(
            others_folder,
            exist_ok=True
        )


    # ======================================
    # FIND CATEGORY
    # ======================================

    def get_category(self, extension):

        extension = extension.lower()

        for category, extensions in self.file_categories.items():

            if extension in extensions:

                return category

        return "Others"


    # ======================================
    # ORGANIZE FILES
    # ======================================

    def organize_files(self):

        if not os.path.exists(self.folder_path):

            print("Folder does not exist.")
            return


        self.create_folders()


        moved_files = 0


        for filename in os.listdir(self.folder_path):

            source_path = os.path.join(
                self.folder_path,
                filename
            )


            # Ignore directories

            if not os.path.isfile(source_path):

                continue


            extension = os.path.splitext(
                filename
            )[1]


            category = self.get_category(
                extension
            )


            destination_folder = os.path.join(
                self.folder_path,
                category
            )


            destination_path = os.path.join(
                destination_folder,
                filename
            )


            # Handle duplicate filenames

            if os.path.exists(destination_path):

                name, ext = os.path.splitext(filename)

                counter = 1


                while os.path.exists(destination_path):

                    new_filename = (
                        f"{name}_{counter}{ext}"
                    )

                    destination_path = os.path.join(
                        destination_folder,
                        new_filename
                    )

                    counter += 1


            try:

                shutil.move(
                    source_path,
                    destination_path
                )

                print(
                    f"Moved: {filename} → {category}"
                )

                moved_files += 1


            except PermissionError:

                print(
                    f"Permission denied: {filename}"
                )


            except OSError as error:

                print(
                    f"Could not move {filename}: {error}"
                )


        print(
            f"\nSuccessfully organized "
            f"{moved_files} file(s)."
        )


# ==========================================
# MAIN PROGRAM
# ==========================================

print("=" * 50)
print("           FILE ORGANIZER")
print("=" * 50)

folder_path = input(
    "Enter folder path to organize: "
).strip()


organizer = FileOrganizer(
    folder_path
)

organizer.organize_files()