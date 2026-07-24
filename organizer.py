import argparse
import logging
from pathlib import Path
import shutil

# 1. Configure Logging
logging.basicConfig(
    filename='organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 2. File Extension Category Mapping
CATEGORIES = {
    ".py": "Python_Code",
    ".js": "Web_Code",
    ".html": "Web_Code",
    ".css": "Web_Code",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".docx": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".mp4": "Videos",
    ".zip": "Archives"
}

def get_unique_path(target_path: Path) -> Path:
    """Resolves filename conflicts by appending '_copy' if file exists."""
    counter = 1
    new_path = target_path
    while new_path.exists():
        new_path = target_path.parent / f"{target_path.stem}_copy{counter}{target_path.suffix}"
        counter += 1
    return new_path

def organize_directory(source_dir: Path, dry_run: bool = False):
    """Scans the source directory and moves files to category folders."""
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"❌ Error: Directory '{source_dir}' does not exist.")
        logging.error(f"Invalid directory path: {source_dir}")
        return

    print(f"\n📂 Scanning directory: {source_dir.resolve()}")
    if dry_run:
        print("🔍 [DRY-RUN MODE] No actual files will be moved.\n")

    moved_count = 0
    error_count = 0

    for item in source_dir.iterdir():
        # Process files only (skip directories and hidden files)
        if item.is_file() and not item.name.startswith('.'):
            ext = item.suffix.lower()
            category = CATEGORIES.get(ext, "Other")
            target_folder = source_dir / category

            # Resolve filename conflicts
            desired_target = target_folder / item.name
            final_target = get_unique_path(desired_target) if desired_target.exists() else desired_target

            log_msg = f"Moving: {item.name} ➡️  {category}/{final_target.name}"
            print(log_msg)
            logging.info(f"{'[DRY RUN] ' if dry_run else ''}{log_msg}")

            if not dry_run:
                try:
                    # Create destination directory if it doesn't exist
                    target_folder.mkdir(exist_ok=True)
                    # Move the file safely
                    shutil.move(str(item), str(final_target))
                    moved_count += 1
                except PermissionError:
                    err_msg = f"Permission denied for {item.name}"
                    print(f"⚠️ {err_msg}")
                    logging.error(err_msg)
                    error_count += 1
                except Exception as e:
                    err_msg = f"Failed to move {item.name}: {e}"
                    print(f"⚠️ {err_msg}")
                    logging.error(err_msg)
                    error_count += 1

    print("\n--- Summary ---")
    print(f"Files processed/moved: {moved_count if not dry_run else 'N/A (Dry Run)'}")
    print(f"Errors encountered: {error_count}")
    print("Check 'organizer.log' for detailed log history.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated File Organizer CLI Tool")
    parser.add_argument("source", help="Path to the directory you want to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves without modifying files")

    args = parser.parse_args()
    organize_directory(Path(args.source), dry_run=args.dry_run)