import wx
import wx.html
from ..utils.generic_class import GenericClass
from ..utils.constants import control, dtype
from ..utils.validator import CharValidator
import os
import pkg_resources as p


class Settings(wx.html.HtmlWindow):

    def __init__(self, parent, counter=0):
        from urllib2 import urlopen
        wx.html.HtmlWindow.__init__(
            self, parent, style=wx.html.HW_SCROLLBAR_AUTO)
        self.SetStandardFonts()

        self.counter = counter

        self.LoadFile(p.resource_filename('CPAC', 'GUI/resources/html/settings.html'))

#        try:
#            code = urlopen("http://fcp-indi.github.io/docs/user/compute_config.html").code
#            if (code / 100 < 4):
#                self.LoadPage('http://fcp-indi.github.io/docs/user/compute_config.html')
#            else:
#                self.LoadFile('html/settings.html')
#        except:
#            self.LoadFile('html/settings.html')

    def get_counter(self):
        return self.counter


class ComputerSettings(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)
        self.counter = counter
        
        fsl = ""
        if os.environ.get('FSLDIR'):
            fsl = os.environ['FSLDIR']
            

        self.page = GenericClass(self, "Computer Settings")
        self.page.add(label="Run CPAC on Grid:",
                      control=control.CHOICE_BOX,
                      name='runOnGrid',
                      type=dtype.BOOL,
                      comment="True = Run on compute cluster, False = Run on non-cluster machine",
                      values=["False", "True"],
                      wkf_switch=True)

        self.page.add(label="FSL Path ",
                      control=control.DIR_COMBO_BOX,
                      name='FSLDIR',
                      type=dtype.STR,
                      values=fsl,
                      comment="Full path to the FSL version to be used by CPAC.\n\nIf you have specified an FSL path in your .bashrc file, this path will be set automatically.")

        self.page.add(label="Job Scheduler / Resource Manager ",
                      control=control.CHOICE_BOX,
                      name='resourceManager',
                      type=dtype.STR,
                      values=["SGE", "PBS"],
                      comment="Sun Grid Engine (SGE) or Portable Batch System (PBS)")

        self.page.add(label='SGE Parallel Environment ',
                      control=control.TEXT_BOX,
                      name='parallelEnvironment',
                      type=dtype.STR,
                      comment='SGE Parallel Environment to use when running CPAC.',
                      values='cpac')

        self.page.add(label='SGE Queue ',
                      control=control.TEXT_BOX,
                      name='queue',
                      type=dtype.STR,
                      comment='SGE Queue to use when running CPAC.',
                      values='all.q')

        self.page.add(label="Number of Cores Per Subject ",
                      control=control.INT_CTRL,
                      name='numCoresPerSubject',
                      type=dtype.NUM,
                      comment="Number of cores (on a single machine) or slots on a node (cluster/grid) per subject. Slots are cores on a cluster/grid node.\n\nIMPORTANT: Number of Cores Per Subject multiplied by Number of Subjects to Run Simultaneously must not be greater than the total number of cores.",
                      values=1)

        self.page.add(label="Number of Subjects to Run Simultaneously ",
                      control=control.INT_CTRL,
                      name='numSubjectsAtOnce',
                      type=dtype.NUM,
                      comment="This number depends on computing resources.",
                      values=2)

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter


class DirectorySettings(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)

        self.page = GenericClass(self, "Output Settings")
        self.counter = counter

        self.page.add(label="Working Directory ",
                      control=control.DIR_COMBO_BOX,
                      name='workingDirectory',
                      type=dtype.STR,
                      comment="Directory where CPAC should store temporary and intermediate files.",
                      validation_req=False)

        self.page.add(label="Crash Log Directory ",
                      control=control.DIR_COMBO_BOX,
                      name='crashLogDirectory',
                      type=dtype.STR,
                      comment="Directory where CPAC should write crash logs.",
                      validation_req=False)

        self.page.add(label="Output Directory ",
                      control=control.DIR_COMBO_BOX,
                      name='outputDirectory',
                      type=dtype.STR,
                      comment="Directory where CPAC should place processed data.",
                      validation_req=False)

        self.page.add(label="Create Symbolic Links ",
                      control=control.CHOICE_BOX,
                      name='runSymbolicLinks',
                      type=dtype.LSTR,
                      comment="Create a user-friendly, well organized version of the output directory.\n\n"
                      "We recommend all users enable this option.",
                      values=["On", "Off"])

        self.page.add(label="Enable Quality Control Interface ",
                      control=control.CHOICE_BOX,
                      name='generateQualityControlImages',
                      type=dtype.LSTR,
                      comment="Generate quality control pages containing preprocessing and derivative outputs.",
                      values=["On", "Off"])

        self.page.add(label="Remove Working Directory ",
                      control=control.CHOICE_BOX,
                      name='removeWorkingDir',
                      type=dtype.BOOL,
                      values=["False", "True"],
                      comment="Deletes the contents of the Working Directory after running.\n\nThis saves disk space, but any additional preprocessing or analysis will have to be completely re-run.")

        self.page.add(label="Regenerate Outputs ",
                      control=control.CHOICE_BOX,
                      name='reGenerateOutputs',
                      type=dtype.BOOL,
                      values=["True", "False"],
                      comment="Uses the contents of the Working Directory to regenerate all outputs and their symbolic links.\n\nRequires an intact Working Directory from a previous CPAC run.")

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter


class WorkflowConfig(wx.ScrolledWindow):

    def __init__(self, parent, counter=0):
        wx.ScrolledWindow.__init__(self, parent)
        self.counter = counter

        self.page = GenericClass(self, "Preprocessing Workflow Selection")

        self.page.add(label="Gather Anatomical Data ",
                      control=control.CHOICE_BOX,
                      name='runAnatomicalDataGathering',
                      type=dtype.LSTR,
                      comment="Loads anatomical images for processing by CPAC.\n\nMust be enabled to run preprocessing and analyses.",
                      values=["On", "Off"])

        self.page.add(label="Gather Functional Data ",
                      control=control.CHOICE_BOX,
                      name='runFunctionalDataGathering',
                      type=dtype.LSTR,
                      comment="Loads functional images for processing by CPAC.\n\nMust be enabled to run preprocessing and analyses.",
                      values=["On", "Off"])

        self.page.add(label="Run Anatomical Preprocessing ",
                      control=control.CHOICE_BOX,
                      name='runAnatomicalPreprocessing',
                      type=dtype.LSTR,
                      comment="Runs the anatomical preprocessing workflow.\n\nMust be enabled to run any subsequent processing or analysis workflows.",
                      values=["On", "Off"])

        self.page.add(label="Run Functional Preprocessing ",
                      control=control.CHOICE_BOX,
                      name='runFunctionalPreprocessing',
                      type=dtype.LSTR,
                      comment="Runs the functional preprocessing workflow.\n\nMust be enabled to run any subsequent processing or analysis workflows.",
                      values=["On", "Off"])

        self.page.set_sizer()
        parent.get_page_list().append(self)

    def get_counter(self):
        return self.counter