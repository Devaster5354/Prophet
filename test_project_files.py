import os


def test_core_files_exist():
    root = os.path.dirname(__file__)
    # basic smoke checks
    assert os.path.exists(os.path.join(root, 'dashboard.py'))
    assert os.path.exists(os.path.join(root, 'dashboard_exec.py'))
    assert os.path.exists(os.path.join(root, 'Report_Prophet.pdf'))
