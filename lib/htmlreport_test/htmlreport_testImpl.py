# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import os
from Bio import SeqIO
from pprint import pprint, pformat
from KBaseReport.KBaseReportClient import KBaseReport
from htmlreport_test.Utils.ReportUtil import ReportUtil
import matplotlib
import uuid
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#END_HEADER


class htmlreport_test:
    '''
    Module Name:
    htmlreport_test

    Module Description:
    A KBase module: htmlreport_test
This sample module contains one small method - filter_contigs.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block

    def _mkdir_p(self, path):
        """
        _mkdir_p: make directory for given path
        """
        if not path:
            return
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        
        # Any configuration parameters that are important should be parsed and
        # saved in the constructor.
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
	self.scratch = config['scratch']
        #END_CONSTRUCTOR
        pass


    def filter_contigs(self, ctx, params):
        """
        The actual function is declared using 'funcdef' to specify the name
        and input/return arguments to the function.  For all typical KBase
        Apps that run in the Narrative, your function should have the 
        'authentication required' modifier.
        :param params: instance of type "FilterContigsParams" (A 'typedef'
           can also be used to define compound or container objects, like
           lists, maps, and structures.  The standard KBase convention is to
           use structures, as shown here, to define the input and output of
           your function.  Here the input is a reference to the Assembly data
           object, a workspace to save output, and a length threshold for
           filtering. To define lists and maps, use a syntax similar to C++
           templates to indicate the type contained in the list or map.  For
           example: list <string> list_of_strings; mapping <string, int>
           map_of_ints;) -> structure: parameter "assembly_input_ref" of type
           "assembly_ref" (A 'typedef' allows you to provide a more specific
           name for a type.  Built-in primitive types include 'string',
           'int', 'float'.  Here we define a type named assembly_ref to
           indicate a string that should be set to a KBase ID reference to an
           Assembly data object.), parameter "workspace_name" of String,
           parameter "min_length" of Long
        :returns: instance of type "FilterContigsResults" (Here is the
           definition of the output of the function.  The output can be used
           by other SDK modules which call your code, or the output
           visualizations in the Narrative.  'report_name' and 'report_ref'
           are special output fields- if defined, the Narrative can
           automatically render your Report.) -> structure: parameter
           "report_name" of String, parameter "report_ref" of String,
           parameter "assembly_output" of type "assembly_ref" (A 'typedef'
           allows you to provide a more specific name for a type.  Built-in
           primitive types include 'string', 'int', 'float'.  Here we define
           a type named assembly_ref to indicate a string that should be set
           to a KBase ID reference to an Assembly data object.), parameter
           "n_initial_contigs" of Long, parameter "n_contigs_removed" of
           Long, parameter "n_contigs_remaining" of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN filter_contigs

        # Print statements to stdout/stderr are captured and available as the App log
        print('Starting Filter Contigs function. Params=')
        pprint(params)
        print('Creating image and saving HTML report')

        result_directory = os.path.join(self.scratch, str(uuid.uuid4()))
        self._mkdir_p(result_directory)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(range(100))
        fig.savefig(result_directory + '/plot1.png')
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(range(1000))
        fig.savefig(result_directory + '/plot2.png')

        dummy_html_report_runner = ReportUtil(self.config)
        output = dummy_html_report_runner._generate_report (params, result_directory)




        #END filter_contigs

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method filter_contigs return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
