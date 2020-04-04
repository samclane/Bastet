from PyQt5 import QtCore


from bastet.__main__ import MainWindow


def test_main_window_run(qtbot):
    mw = MainWindow()
    mw.show()
    qtbot.addWidget(mw)

    qtbot.mouseClick(
        mw.check_box,
        QtCore.Qt.LeftButton,
        pos=QtCore.QPoint(2, mw.check_box.height() / 2),
    )

    assert mw.check_box.isChecked()
