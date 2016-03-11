from _libopenzwave import ffi, lib


class PyManager(object):
    def create(self):
        self.manager = lib.newCManager()

    def addWatcher(self, callback):
        context = ffi.new_handle(callback)
        self._watcherCallbackSavedReference = context
        if not lib.CManagerAddWatcher(
            self.manager,
            lib.add_manager_callback,
            context,
        ):
            assert False
