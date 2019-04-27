from functools import partial

from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper

def toolsSetup(parent):
    parent.materialFwdBtn.clicked.connect(partial(materialFwd, parent))
    parent.materialBackBtn.clicked.connect(partial(materialBack, parent))
    parent.thicknessFwdBtn.clicked.connect(partial(thicknessFwd, parent))
    parent.thicknessBackBtn.clicked.connect(partial(thicknessBack, parent))
    parent.nozzleFwdBtn.clicked.connect(partial(nozzleFwd, parent))
    parent.nozzleBackBtn.clicked.connect(partial(nozzleBack, parent))

    materialInit(parent)


def materialInit(parent):
    parent.materialMapper = QDataWidgetMapper(parent)
    parent.materialModel = QSqlQueryModel(parent)
    parent.materialModel.setQuery('SELECT DISTINCT material FROM cut_chart')
    parent.materialMapper.setModel(parent.materialModel)
    parent.materialMapper.addMapping(parent.materialLbl, 0, b'text')
    parent.materialMapper.toLast()
    parent.materialLast = parent.materialMapper.currentIndex()
    parent.materialMapper.toFirst()
    thicknessInit(parent)


def materialFwd(parent):
    if parent.materialMapper.currentIndex() != parent.materialLast:
        parent.materialMapper.toNext()
    else:
        parent.materialMapper.toFirst()
    thicknessInit(parent)

def materialBack(parent):
    if parent.materialMapper.currentIndex() != 0:
        parent.materialMapper.toPrevious()
    else:
        parent.materialMapper.toLast()
    thicknessInit(parent)

def thicknessInit(parent):
    parent.thicknessMapper = QDataWidgetMapper(parent)
    parent.thicknessModel = QSqlQueryModel(parent)
    material = parent.materialLbl.text()
    parent.thicknessModel.setQuery("SELECT DISTINCT gauge FROM cut_chart \
        WHERE material = '{}'".format(material))
    parent.thicknessMapper.setModel(parent.thicknessModel)
    parent.thicknessMapper.addMapping(parent.thicknessLbl, 0, b'text')
    parent.thicknessMapper.toLast()
    parent.thicknessLast = parent.thicknessMapper.currentIndex()
    parent.thicknessMapper.toFirst()
    nozzleInit(parent)


def thicknessFwd(parent):
    if parent.thicknessMapper.currentIndex() != parent.thicknessLast:
        parent.thicknessMapper.toNext()
    else:
        parent.thicknessMapper.toFirst()
    nozzleInit(parent)

def thicknessBack(parent):
    if parent.thicknessMapper.currentIndex() != 0:
        parent.thicknessMapper.toPrevious()
    else:
        parent.thicknessMapper.toLast()
    nozzleInit(parent)


def nozzleInit(parent):
    parent.nozzleMapper = QDataWidgetMapper(parent)
    parent.nozzleModel = QSqlQueryModel(parent)
    thickness = parent.thicknessLbl.text()
    parent.nozzleModel.setQuery("SELECT DISTINCT nozzle FROM cut_chart \
        WHERE thickness = '{}'".format(thickness))
    parent.nozzleMapper.setModel(parent.nozzleModel)
    parent.nozzleMapper.addMapping(parent.nozzleLbl, 0, b'text')
    parent.nozzleMapper.toLast()
    parent.nozzleLast = parent.nozzleMapper.currentIndex()
    parent.nozzleMapper.toFirst()
    #currentInit(parent)

def nozzleFwd(parent):
    if parent.nozzleMapper.currentIndex() != parent.nozzleLast:
        parent.nozzleMapper.toNext()
    else:
        parent.nozzleMapper.toFirst()
    #currentInit(parent)

def nozzleBack(parent):
    if parent.nozzleMapper.currentIndex() != 0:
        parent.nozzleMapper.toPrevious()
    else:
        parent.nozzleMapper.toLast()
    #currentInit(parent)




