
class Replacer:

    def replace(self, string):
        """
        Replaces invalid characters from with ASCII equivalent.
        """
        result = self.replace_a(string)
        result = self.replace_upper_a(result)
        result = self.replace_e(result)
        result = self.replace_upper_e(result)
        result = self.replace_i(result)
        result = self.replace_upper_i(result)
        result = self.replace_o(result)
        result = self.replace_upper_o(result)
        result = self.replace_u(result)
        result = self.replace_upper_u(result)
        return result

    def replace_a(self, string):
        """
        Replaces 'à', 'á', 'â', 'ã', 'ä', 'å' with 'a'.
        """
        result = string.replace('\xe0', 'a').replace('\xe1', 'a').replace(
            '\xe2', 'a').replace('\xe3', 'a').replace('\xe4', 'a').replace('\xe5', 'a')
        return result

    def replace_upper_a(self, string):
        """
        Replaces 'À','Á','Â','Ã','Ä','Å' with 'A'.
        """
        result = string.replace('\xc0', 'A').replace('\xc1', 'A').replace(
            '\xc2', 'A').replace('\xc3', 'A').replace('\xc4', 'A').replace('\xc5', 'A')
        return result

    def replace_e(self, string):
        """
        Replaces 'è', 'é', 'ê', 'ë' with 'e'.
        """
        result = string.replace('\xe8', 'e').replace(
            '\xe9', 'e').replace('\xea', 'e').replace('\xeb', 'e')
        return result

    def replace_upper_e(self, string):
        """
        Replaces 'È', 'É', 'Ê', 'Ë' with 'E'.
        """        
        result = string.replace('\xc8', 'E').replace('\xc9', 'E').replace('\xca', 'E').replace('\xcb', 'E')
        return result

    def replace_i(self, string):
        """
        Replaces 'ì', 'í', 'î', 'ï' with 'i'.
        """
        result = string.replace('\xec', 'i').replace(
            '\xed', 'i').replace('\xee', 'i').replace('\xef', 'i')
        return result

    def replace_upper_i(self, string):
        """
        Replaces 'Ì','Í','Î','Ï' with 'I'.
        """
        result = string.replace('\xcc', 'I').replace(
            '\xcd', 'I').replace('\xce', 'I').replace('\xcf', 'I')
        return result

    def replace_o(self, string):
        """
        Replaces 'ò', 'ó', 'ô', 'õ', 'ö' with 'o'.
        """
        result = string.replace('\xf2', 'o').replace(
            '\xf3', 'o').replace('\xf4', 'o').replace('\xf5', 'o').replace('\xf6', 'o')
        return result

    def replace_upper_o(self, string):
        """ 
        Replaces 'Ò', 'Ó', 'Ô', 'Õ', 'Ö' with 'O'.
        """
        result = string.replace('\xd2', 'O').replace(
            '\xd3', 'O').replace('\xd4', 'O').replace('\xd5', 'O').replace('\xd6', 'O')
        return result

    def replace_u(self, string):
        """
        Replaces 'ù', 'ú', 'û', 'ü' with 'u'.
        """
        result = string.replace('\xf9', 'u').replace(
            '\xfa', 'u').replace('\xfb', 'u').replace('\xfc', 'u')
        return result
    
    def replace_upper_u(self, string):
        """
        Replaces 'Ù', 'Ú', 'Û', 'Ü' with 'U'.
        """
        result = string.replace('\xd9', 'U').replace(
            '\xda', 'U').replace('\xdb', 'U').replace('\xdc', 'U')
        return result
