#
# Copyright (c) 2007 Elliot Peele <elliot@bentlogic.net>
#
# Licensed under the GNU General Public License Version 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#

from conary import callbacks
from packagekit.backend import *

class UpdateCallback(callbacks.UpdateCallback):
    def resolvingDependencies(self):
        #self.backend.status('Resolving Dependencies')
        self.backend.status(STATUS_DEP_RESOLVE)

    def creatingRollback(self):
        #self.backend.status('Creating Rollback')
        self.backend.status(STATUS_ROLLBACK)

    def committingTransaction(self):
        #self.backend.status('Committing Transaction')
        self.backend.status(STATUS_COMMIT)

    def downloadingFileContents(self, got, need):
        #self.backend.status('Downloading files for changeset')
        self.backend.status(STATUS_DOWNLOAD)

    def downloadingChangeSet(self, got, need):
        self.backend.status(STATUS_DOWNLOAD)

    def requestingFileContents(self):
        #self.backend.status('Requesting File Contents')
        self.backend.status(STATUS_REQUEST)

    def requestingChangeSet(self):
        #self.backend.status('Requesting Changeset')
        self.backend.status(STATUS_REQUEST)

    def done(self):
        #self.backend.status('Done')
        pass

    def preparingUpdate(self, troveNum, troveCount, add=0):
        if not self.currentJob or len(self.currentJob) == 0 or troveNum > troveCount:
            return

        print "troveNum: %s, troveCount: %s" % (troveNum, troveCount)

        if troveNum > 0 and troveCount > 0:
            sub_percent = (add + troveNum) / (2 * float(troveCount)) * 100
            self.backend.sub_percentage(sub_percent)

            if self.smallUpdate:
                self.backend.percentage(sub_percent)

        if troveNum != 0:
            troveNum -= 1

        job = self.currentJob[troveNum]
        name = job[0]
        oldVersion, oldFlavor = job[1]
        newVersion, newFlavor = job[2]

        if oldVersion and newVersion:
            self.backend.status(STATUS_UPDATE)
            id = self.backend.get_package_id(name, newVersion, newFlavor)
            self.backend.package(id, INFO_UPDATING, '')
        elif oldVersion and not newVersion:
            self.backend.status(STATUS_REMOVE)
            id = self.backend.get_package_id(name, oldVersion, oldFlavor)
            self.backend.package(id, INFO_REMOVING, '')
        elif not oldVersion and newVersion:
            self.backend.status(STATUS_INSTALL)
            id = self.backend.get_package_id(name, newVersion, newFlavor)
            self.backend.package(id, INFO_INSTALLING, '')


    def creatingDatabaseTransaction(self, troveNum, troveCount):
        self.preparingUpdate(troveNum, troveCount, add=troveCount)

    def setChangesetHunk(self, num, total):
        pass

    def setUpdateHunk(self, hunk, hunkCount):
        if hunk > 0 and hunkCount > 0:
            percentage = hunk / float(hunkCount) * 100.0
            self.backend.percentage(percentage)
        else:
            self.smallUpdate = True

    def setUpdateJob(self, job):
        self.currentJob = job

    def updateDone(self):
        self.currentJob = None

    def tagHandlerOutput(self, tag, msg, stderr = False):
        pass

    def troveScriptOutput(self, typ, msg):
        pass

    def troveScriptFailure(self, typ, errcode):
        pass

    def __init__(self, backend, cfg=None):
        callbacks.UpdateCallback.__init__(self)
        if cfg:
            self.setTrustThreshold(cfg.trustThreshold)

        self.backend = backend
        self.currentJob = None
        self.smallUpdate = False
