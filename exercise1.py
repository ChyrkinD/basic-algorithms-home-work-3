import os
import shutil
import argparse

def copy_and_sort_files(source_dir, dest_dir):
    """
    Рекурсивно копіює файли із source_dir до dest_dir,
    сортує їх у піддиректорії на основі розширення файлів.
    """
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for item in os.listdir(source_dir):
            item_path = os.path.join(source_dir, item)

            if os.path.isdir(item_path):
                copy_and_sort_files(item_path, dest_dir)
            elif os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[-1].lower().strip('.')

                if not file_extension:
                    file_extension = 'unknown'

                ext_dir = os.path.join(dest_dir, file_extension)
                if not os.path.exists(ext_dir):
                    os.makedirs(ext_dir)

                dest_file_path = os.path.join(ext_dir, item)
                shutil.copy2(item_path, dest_file_path)

    except Exception as e:
        print(f"Error processing directory {source_dir}: {e}")


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description="Recursive file sorter by extension.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument(
        "dest_dir", nargs="?", default="dist", help="Path to the destination directory (default: dist)."
    )

    args = parser.parse_args()

    source_dir = os.path.abspath(args.source_dir)
    dest_dir = os.path.abspath(args.dest_dir)

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return

    copy_and_sort_files(source_dir, dest_dir)
    print(f"Files from {source_dir} have been copied and sorted into {dest_dir}.")


if __name__ == "__main__":
    main()
