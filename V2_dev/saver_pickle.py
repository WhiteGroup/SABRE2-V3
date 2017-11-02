from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4.QtOpenGL import *
from PyQt4 import QtCore
import numpy as np
from PyQt4 import QtGui
import SABRE2_GUI

from DropDownActions import *
import math
from tempfile import TemporaryFile
from PyQt4.QtGui import *
from PyQt4 import QtCore
import numpy as np
from PyQt4 import QtGui
import SABRE2_GUI


class SaverPicker(QGLWidget, QMainWindow):
    def __init__(self, ui_layout, parent=None):
        super(SaverPicker, self).__init__(parent)
        self.ui = ui_layout

        self.Members_table_position = 3

        self.joint_values = None
        self.member_properties_values = None
        self.members_table_values = None
        self.shear_panel_values = None
        self.ground_spring_values = None
        self.torsional_spring_values = None
        self.My_release_values = None
        self.Mz_release_values = None
        self.Warping_release_values = None
        self.uniform_data_values = None
        self.point_data_values = None

    def save_fun(self):

        import SABRE2_main_subclass

        self.joint_values = SABRE2_main_subclass.SABRE2_main_subclass.update_joints_table(self, SABRE2_GUI.Ui_SABRE2_V3.Joints_Table)
        self.member_properties_values = SABRE2_main_subclass.SABRE2_main_subclass.update_member_properties_table(self,
                                                                                                      self.ui.Member_Properties_Table)
        self.members_table_values = SABRE2_main_subclass.SABRE2_main_subclass.update_members_table(self, self.ui.Members_table,
                                                                                        self.Members_table_position)
        self.shear_panel_values = SABRE2_main_subclass.SABRE2_main_subclass.update_shear_panel_table(self,
                                                                                          self.ui.Shear_panel_table)
        self.ground_spring_values = SABRE2_main_subclass.SABRE2_main_subclass.update_ground_table(self,
                                                                                       self.ui.Discrete_grounded_spring_table)
        self.torsional_spring_values = SABRE2_main_subclass.SABRE2_main_subclass.update_torsional_release(self,
                                                                                               self.ui.Torsional_Release)
        self.My_release_values = SABRE2_main_subclass.SABRE2_main_subclass.update_My_release(self, self.ui.My_release)
        self.Mz_release_values = SABRE2_main_subclass.SABRE2_main_subclass.update_Mz_release(self, self.ui.Mz_release)
        self.Warping_release_values = SABRE2_main_subclass.SABRE2_main_subclass.update_warping_release(self,
                                                                                            self.ui.Warping_Release)
        self.uniform_data_values = SABRE2_main_subclass.SABRE2_main_subclass.update_uniform_data(self,
                                                                                      self.ui.Uniform_loading_table,
                                                                                      combo_flag=0)
        self.point_data_values = SABRE2_main_subclass.SABRE2_main_subclass.update_point_data(self, self.ui.Point_load_table,
                                                                                  combo_flag=0)

        print("test", self.joint_values)
        file = TemporaryFile()
        f = file("tmp.bin", "wb")
        np.save(f, self.joint_values)
        np.save(f, self.member_properties_values)
        np.save(f, self.members_table_values)
        f.close()

    def read_fun(self):
        file = TemporaryFile()
        f = file("tmp.bin", "rb")
        aa = np.load(f)
        bb = np.load(f)
        cc = np.load(f)

        print("joint values", aa, "member properties", bb, "member table values", cc)
        f.close()
