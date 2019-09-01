import os

class ListFiles():
    def list_files(self, path):
        result = list()

        # r=root, d=directories, f = files
        for root, dir, file in os.walk(path):
            for f in file:
                result.append(os.path.join(root, f))

        return result