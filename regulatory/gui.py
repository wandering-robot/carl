class GUI:
    """Gets file parameters and AI parameters and new/retain/display settings from User and returns them to Main"""
    def __init__(self):
        self.ai_param = {'alpha':None}
        self.settings = {'mode':None}
        self.file_param = {'name':None}

    def get_ai_param(self):
        """get AI parameters and return them"""
        pass

    def get_settings(self):
        """get settings and return them"""
        pass

    def get_file_param(self):
        """get file parameters and return them"""
        pass

    def update_attribute(self,key,value):
        """assigns a key-value pair to the defined attribute"""
        for attr_dict in self.__dict__.values():
            if key in attr_dict.keys():
                attr_dict[key] = value
                break