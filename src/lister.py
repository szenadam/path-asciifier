import os

class FileLister():
    def list_files(self, path):
        result = list()
        for root, dir, file in os.walk(path):
            for f in file:
                result.append(os.path.join(root, f))
        return result