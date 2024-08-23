import sys


if sys.argv.count("-git") > 0:
    from pylogging_tools.tests import git_path_loader as gpl
    sys.path.append(gpl())
