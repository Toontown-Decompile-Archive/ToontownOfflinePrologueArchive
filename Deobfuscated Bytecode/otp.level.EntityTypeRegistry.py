# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:30:55) [MSC v.1500 32 bit (Intel)]
# Embedded file name: otp.level.EntityTypeRegistry
# Compiled at: 2014-04-30 09:53:54
from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
import types, AttribDesc, EntityTypeDesc
from direct.showbase.PythonUtil import mostDerivedLast
import os, string

class EntityTypeRegistry:
    notify = DirectNotifyGlobal.directNotify.newCategory('EntityTypeRegistry')

    def __init__(self, entityTypeModule):
        self.entTypeModule = entityTypeModule
        hv = HashVal()
        import EntityTypes
        reload(EntityTypes)
        reload(self.entTypeModule)

        def getPyExtVersion(filename):
            base, ext = os.path.splitext(filename)
            if ext == '.pyc' or ext == '.pyo':
                filename = base + '.py'
            return filename

        fileLines = file(getPyExtVersion(EntityTypes.__file__)).readlines()
        hv.hashString(string.join(fileLines))
        s = str(hv.asHex())
        s += '.'
        fileLines = file(getPyExtVersion(self.entTypeModule.__file__)).readlines()
        hv.hashString(string.join(fileLines))
        s += str(hv.asHex())
        self.hashStr = s
        getPyExtVersion = None
        classes = []
        for key, value in entityTypeModule.__dict__.items():
            if type(value) is types.ClassType:
                if issubclass(value, EntityTypeDesc.EntityTypeDesc):
                    classes.append(value)

        self.entTypeName2typeDesc = {}
        mostDerivedLast(classes)
        for c in classes:
            if c.__dict__.has_key('type'):
                if self.entTypeName2typeDesc.has_key(c.type):
                    EntityTypeRegistry.notify.debug("replacing %s with %s for entity type '%s'" % (self.entTypeName2typeDesc[c.type].__class__, c, c.type))
                self.entTypeName2typeDesc[c.type] = c()

        self.output2typeNames = {}
        for typename, typeDesc in self.entTypeName2typeDesc.items():
            if typeDesc.isConcrete():
                if hasattr(typeDesc, 'output'):
                    outputType = typeDesc.output
                    self.output2typeNames.setdefault(outputType, [])
                    self.output2typeNames[outputType].append(typename)

        self.permanentTypeNames = []
        for typename, typeDesc in self.entTypeName2typeDesc.items():
            if typeDesc.isPermanent():
                self.permanentTypeNames.append(typename)

        self.typeName2derivedTypeNames = {}
        for typename, typeDesc in self.entTypeName2typeDesc.items():
            typenames = []
            for tn, td in self.entTypeName2typeDesc.items():
                if td.isConcrete():
                    if issubclass(td.__class__, typeDesc.__class__):
                        typenames.append(tn)

            self.typeName2derivedTypeNames[typename] = typenames

        return

    def getAllTypeNames(self):
        return self.entTypeName2typeDesc.keys()

    def getTypeDesc(self, entTypeName):
        return self.entTypeName2typeDesc[entTypeName]

    def getTypeNamesFromOutputType(self, outputType):
        return self.output2typeNames.get(outputType, [])

    def getDerivedTypeNames(self, entTypeName):
        return self.typeName2derivedTypeNames[entTypeName]

    def isDerivedAndBase(self, entType, baseEntType):
        return entType in self.getDerivedTypeNames(baseEntType)

    def getPermanentTypeNames(self):
        return self.permanentTypeNames

    def getHashStr(self):
        return self.hashStr

    def __hash__(self):
        return hash(repr(self))

    def __repr__(self):
        return str(self.entTypeName2typeDesc)