""""
Specifying the root path

os.listdir(Path_to_Dir.data_path(__root__))
os.listdir(Path_to_Dir.base_path(__root__))
"""
import os

class path_to_dir(object):

    def base_path(self):
        """"
        Purpose: returning the root path
        :return:
        """
        #self.main_path=os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.dirname(__file__)
        return self.path

    def data_path(self):
        """"
        Purpose: returning the Assets/data path
        :return:
        """
        self.path=os.path.join(os.path.dirname(__file__), './Assets/data')
        return self.path