import sys
import python_logging_tools as _


def import_():
    from python_logging_tools.main import git_path_loader as gpl
    sys.path.append(gpl())


if sys.argv.count("-git") > 0:
    import_()
