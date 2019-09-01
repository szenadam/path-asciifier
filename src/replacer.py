"""
Replacer classes and methods
"""

class Replacer:
    """
    The Replacer class is repsonsible for simply string replacements.
    """

    def replace(self, string):
        """
        Replaces invalid characters from with ASCII equivalent.
        """
        result = self.replace_a(string)
        result = self.replace_e(result)
        result = self.replace_i(result)
        result = self.replace_o(result)
        result = self.replace_u(result)
        return result

    def replace_a(self, string):
        """
        Replaces 'à', 'á', 'â', 'ã', 'ä', 'å' with 'a'.
        """
        result = string.replace('\xe0', 'a').replace('\xe1', 'a').replace(
            '\xe2', 'a').replace('\xe3', 'a').replace('\xe4', 'a').replace('\xe5', 'a')
        return result

    def replace_e(self, string):
        """
        Replaces 'è', 'é', 'ê', 'ë' with 'e'.
        """
        result = string.replace('\xe8', 'e').replace(
            '\xe9', 'e').replace('\xea', 'e').replace('\xeb', 'e')
        return result

    def replace_i(self, string):
        """
        Replaces 'ì', 'í', 'î', 'ï' with 'i'.
        """
        result = string.replace('\xec', 'i').replace(
            '\xed', 'i').replace('\xee', 'i').replace('\xef', 'i')
        return result

    def replace_o(self, string):
        """
        Replaces 'ò', 'ó', 'ô', 'õ', 'ö' with 'o'.
        """
        result = string.replace('\xf2', 'o').replace(
            '\xf3', 'o').replace('\xf4', 'o').replace('\xf5', 'o').replace('\xf6', 'o')
        return result

    def replace_u(self, string):
        """
        Replaces 'ù', 'ú', 'û', 'ü' with 'u'.
        """
        result = string.replace('\xf9', 'u').replace(
            '\xfa', 'u').replace('\xfb', 'u').replace('\xfc', 'u')
        return result
