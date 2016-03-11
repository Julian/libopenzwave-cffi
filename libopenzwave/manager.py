from _libopenzwave import lib


class PyManager(object):
    def create(self):
        self.manager = lib.newCManager()

    def addWatcher(self, callback):
        if not lib.CManagerAddWatcher(self.manager, callback, None):
            pass
