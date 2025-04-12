from pathlib import Path
import shutil
import argparse
import sys

def copy_and_sort_files(src_dir: Path, dest_dir: Path):
    """
    Рекурсивно копіює файли з src_dir до dest_dir, сортує їх у підпапки за розширенням.
    """
    try:
        for item in src_dir.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для підкаталогів
                copy_and_sort_files(item, dest_dir)
            elif item.is_file():
                ext = item.suffix[1:].lower() if item.suffix else "no_extension"
                target_subdir = dest_dir / ext
                target_subdir.mkdir(parents=True, exist_ok=True)

                target_file_path = target_subdir / item.name

                try:
                    shutil.copy2(item, target_file_path)
                    print(f"✅ Скопійовано: {item} → {target_file_path}")
                except Exception as e:
                    print(f"❌ Помилка при копіюванні {item}: {e}")
    except Exception as e:
        print(f"❌ Помилка при доступі до директорії {src_dir}: {e}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли та сортує за розширенням.")
    parser.add_argument("src", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument("dest", type=Path, nargs="?", default=Path("dist"), help="Шлях до директорії призначення (за замовчуванням: dist)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    src_dir = args.src.resolve()
    dest_dir = args.dest.resolve()

    if not src_dir.exists() or not src_dir.is_dir():
        print(f"❌ Вихідна директорія не існує або недоступна: {src_dir}")
        sys.exit(1)

    dest_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Починаємо копіювання з {src_dir} до {dest_dir}...\n")
    copy_and_sort_files(src_dir, dest_dir)
    print("\n✅ Копіювання завершено.")


if __name__ == "__main__":
    main()
