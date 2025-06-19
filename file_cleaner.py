import os
import shutil
import ctypes

class FileCleaner:
    def __init__(self):
        self.temp_path = os.environ.get("TEMP")
        self.chrome_cache = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache")
        self.chrome_cookies = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cookies")

    def count_files_in_folder(self, folder):
        total = 0
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                total += len(files)
        return total

    def get_temp_file_count(self):
        return self.count_files_in_folder(self.temp_path)

    def get_trace_file_count(self):
        count = self.count_files_in_folder(self.chrome_cache)
        if os.path.exists(self.chrome_cookies):
            count += 1
        return count

    def delete_temp_files(self):
        if os.path.exists(self.temp_path):
            for root, dirs, files in os.walk(self.temp_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                    except:
                        pass

    def delete_trace_files(self):
        if os.path.exists(self.chrome_cache):
            for root, dirs, files in os.walk(self.chrome_cache):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                    except:
                        pass

        if os.path.exists(self.chrome_cookies):
            try:
                os.remove(self.chrome_cookies)
            except:
                pass

    def delete_software_distribution_cache(self):
        path = r"C:\\Windows\\SoftwareDistribution\\Download"
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                    except:
                        pass
                for name in dirs:
                    try:
                        shutil.rmtree(os.path.join(root, name))
                    except:
                        pass

    def delete_common_junk(self):
        junk_paths = [
            r"C:\\Windows\\Prefetch",
            os.path.expanduser("~\\AppData\\Local\\CrashDumps"),
            r"C:\\Windows\\Logs",
        ]
        for path in junk_paths:
            if os.path.exists(path):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        try:
                            os.remove(os.path.join(root, file))
                        except:
                            pass

        # Clear Recycle Bin
        try:
            ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
        except:
            pass

    def delete_old_driver_backups(self):
        path = r"C:\\Windows\\System32\\DriverStore\\FileRepository"
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass

    # OPTIONAL
    def delete_registry_junk(self):
        pass  # To be implemented with winreg or external scripts
