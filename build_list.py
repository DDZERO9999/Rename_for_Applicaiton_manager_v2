class Create_list:
    #build lists from CSV file
    def __init__(self, string):
        self.string = string
        
    def create_list(self):
        #Create lists for ^ place holder for search and replace
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f'{str1}^{str2}')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list

    def create_list_quote(self):
        #Create lists for ^ place holder for search and replace with '
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f'\'{str1}^{str2}\'')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list

    def create_list_space(self):
        #Create lists for ^ place holder for search and replace with space at end
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f'{str1}^{str2} ')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list

    def create_list_2space(self):
        #Create lists for ^ place holder for search and replace with space pre, apended
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f' {str1}^{str2} ')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list

    def create_list_pspace(self):
        #Create lists for ^ place holder for search and replace with space pre, apended
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f' {str1}^{str2}~~')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list
    
    def create_list_espace(self):
        #Create lists for ^ place holder for search and replace with space pre, apended
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f'={str1}^{str2}~~')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list


    def create_list_slash(self):
        #Create lists for ^ place holder for search and replace with space pre, apended
        count = (len(self.string))
        fstr_pos = 1
        frst_char = 1
        the_list = []
        #Add ^ to string  
        while count >= 1:
            str1 = self.string[0:frst_char]
            str2 = self.string[fstr_pos:]
            the_list.append(f' {str1}^{str2}/')
            fstr_pos += 1
            frst_char +=1
            count -= 1
        return the_list


