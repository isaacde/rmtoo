'''
 rmtoo
   Free and Open Source Requirements Management Tool
   
  Blackbox rmtoo test
   
 (c) 2010-2012 by flonatel GmbH & Co. KG

 For licensing details see COPYING
'''
import os

from rmtoo.lib.RmtooMain import main_impl
from rmtoo.tests.lib.BBHelper import prepare_result_is_dir, compare_results, \
    cleanup_std_log, delete_result_is_dir, extract_container_files, \
    unify_output_dir, check_file_results

mdir = "tests/BlackboxTest/Bb013Test"

class TestBB007:

    def test_pos_001(self):
        "BB Basic with one requirement - graph output with defined tags"

        os.environ["basedir"] = mdir
        mout, merr = prepare_result_is_dir()
        result = main_impl(["-j", "file://" + mdir + "/input/Config.json"],
                           mout, merr)
        cleanup_std_log(mout, merr)
        check_file_results(mdir)
        delete_result_is_dir()
