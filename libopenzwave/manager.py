from _libopenzwave import ffi, lib

from libopenzwave._global import PyNotifications


class PyManager(object):
    def create(self):
        self.manager = ffi.gc(lib.newCManager(), lib.destroyCManager)

    def addWatcher(self, callback):
        context = ffi.new_handle(callback)
        self._watcherCallbackSavedReference = context
        if not lib.CManagerAddWatcher(
            self.manager,
            lib.do_manager_watcher_callback,
            context,
        ):
            assert False

    def addDriver(self, controllerPath):
        return lib.CManagerAddDriver(self.manager, controllerPath)

    def getLibraryTypeName(self, homeId):
        return ffi.string(lib.CManagerGetLibraryTypeName(self.manager, homeId))

    def getLibraryVersion(self, homeId):
        return ffi.string(lib.CManagerGetLibraryVersion(self.manager, homeId))


@ffi.def_extern()
def do_manager_watcher_callback(cNotification, context):
    callback = ffi.from_handle(context)
    notification_type_value = int(
        ffi.cast("int", lib.CNotificationGetType(cNotification))
    )
    notification_type = PyNotifications[notification_type_value]
    callback(
        {
            "notificationType" : notification_type,
            "homeId" : lib.CNotificationGetHomeId(cNotification),
            "nodeId" : lib.CNotificationGetNodeId(cNotification),
        },
    )
