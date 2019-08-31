
class Replacer:

    def replace(self, string):
        """
        Replaces invalid characters from with ASCII equivalent
        """
        result = self.replace_a(string)
        result = self.replace_e(result)
        return result

    def replace_a(self, string):
        """
        Replaces 'à', 'á', 'â', 'ã', 'ä', 'å' with 'a'
        """
        result = string.replace('\xe0', 'a').replace('\xe1', 'a').replace(
            '\xe2', 'a').replace('\xe3', 'a').replace('\xe4', 'a').replace('\xe5', 'a')
        return result

    def replace_e(self, string):
        """
        Replaces 'è', 'é', 'ê', 'ë' with 'e'
        """
        result = string.replace('\xe8', 'e').replace(
            '\xe9', 'e').replace('\xea', 'e').replace('\xeb', 'e')
        return result
