import os


class FileLister:
    def list_files(self, path, recursive=False):
        result = list()
        for root, dirs, file in os.walk(path):
            for f in file:
                result.append(os.path.join(root, f))
        return result

    def list_dirs(self, path, recursive=False):
        result = list()
        for root, dirs, file in os.walk(path):
            for d in dirs:
                result.append(os.path.join(root, d))
        return result
