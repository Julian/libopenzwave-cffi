from _libopenzwave import ffi, lib


class PyManager(object):
    def create(self):
        self.manager = lib.newCManager()

    def addWatcher(self, callback):
        context = ffi.new_handle(callback)
        self._watcherCallbackSavedReference = context
        if not lib.CManagerAddWatcher(
            self.manager,
            lib.manager_watcher_callback,
            context,
        ):
            assert False

    def addDriver(self, controllerPath):
        return lib.CManagerAddDriver(self.manager, controllerPath)


@ffi.def_extern()
def manager_watcher_callback(context):
    callback = ffi.from_handle(context)
    callback()
