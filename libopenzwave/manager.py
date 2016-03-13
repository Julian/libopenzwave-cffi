from _libopenzwave import ffi, lib


class PyManager(object):
    def create(self):
        self.manager = ffi.gc(lib.newCManager(), lib.destroyCManager)

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
def manager_watcher_callback(notification, context, _):
    callback = ffi.from_handle(context)
    callback(notification)
