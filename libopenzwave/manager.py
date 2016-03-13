from _libopenzwave import ffi, lib

from libopenzwave import __version__
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

    def removeWatcher(self, _):
        # NOTE: not sure why the arg here is unused, but it is in the original
        #       code too. Probably at very least it should be used to check
        #       that the handle we saved was to that pythonFunc
        try:
            assert lib.CManagerRemoveWatcher(
                self.manager,
                lib.do_manager_watcher_callback,
                self._watcherCallbackSavedReference,
            )
        finally:
            self._watcherCallbackSavedReference = None

    def isBridgeController(self, homeId):
        return lib.CManagerIsBridgeController(self.manager, homeId)

    def isNodeFrequentListeningDevice(self, homeId, nodeId):
        return lib.CManagerIsNodeFrequentListeningDevice(self.manager, homeId, nodeId)

    def isNodeBeamingDevice(self, homeId, nodeId):
        return lib.CManagerIsNodeBeamingDevice(self.manager, homeId, nodeId)

    def isNodeListeningDevice(self, homeId, nodeId):
        return lib.CManagerIsNodeListeningDevice(self.manager, homeId, nodeId)

    def isNodeRoutingDevice(self, homeId, nodeId):
        return lib.CManagerIsNodeRoutingDevice(self.manager, homeId, nodeId)

    def isNodeSecurityDevice(self, homeId, nodeId):
        return lib.CManagerIsNodeSecurityDevice(self.manager, homeId, nodeId)

    def isPrimaryController(self, homeId):
        return lib.CManagerIsPrimaryController(self.manager, homeId)

    def isStaticUpdateController(self, homeId):
        return lib.CManagerIsStaticUpdateController(self.manager, homeId)

    def addDriver(self, controllerPath):
        return lib.CManagerAddDriver(self.manager, controllerPath)

    def removeDriver(self, controllerPath):
        return lib.CManagerRemoveDriver(self.manager, controllerPath)

    def cancelControllerCommand(self, homeId):
        return lib.CManagerCancelControllerCommand(self.manager, homeId)

    def getDriverStatistics(self, homeId):
        data = ffi.new("struct DriverData*")
        statistics = lib.CManagerGetDriverStatistics(homeId, data)
        return statistics

    def getLibraryTypeName(self, homeId):
        return ffi.string(lib.CManagerGetLibraryTypeName(self.manager, homeId))

    def getLibraryVersion(self, homeId):
        return ffi.string(lib.CManagerGetLibraryVersion(self.manager, homeId))

    def getNodeVersion(self, homeId, nodeId):
        return int(lib.CManagerGetNodeVersion(self.manager, homeId, nodeId))

    def getPythonLibraryVersion(self):
        version = self.getPythonLibraryVersionNumber()
        return "python-openzwave+cffi v%s" % (version,)

    def getPythonLibraryVersionNumber(self):
        return __version__

    @classmethod
    def getOzwLibraryVersion(cls):
        return ffi.string(lib.CManagerGetVersionAsString())

    def getSendQueueCount(self, homeId):
        return lib.CManagerGetSendQueueCount(self.manager, homeId)

    def getNodeName(self, homeId, nodeId):
        return ffi.string(
            lib.CManagerGetNodeName(self.manager, homeId, nodeId),
        )

    def setNodeName(self, homeId, nodeId, nodeName):
        lib.CManagerSetNodeName(self.manager, homeId, nodeId, nodeName)

    def getNodeLocation(self, homeId, nodeId):
        return lib.CManagerSetNodeLocation(self.manager, homeId, nodeId)

    def setNodeLocation(self, homeId, nodeId, nodeLocation):
        lib.CManagerSetNodeLocation(self.manager, homeId, nodeId, nodeLocation)

    def getNodeProductName(self, homeId, nodeId):
        return ffi.string(
            lib.CManagerGetNodeProductName(self.manager, homeId, nodeId),
        )

    def setNodeProductName(self, homeId, nodeId, nodeProductName):
        lib.CManagerSetNodeProductName(
            self.manager, homeId, nodeId, nodeProductName,
        )

    def writeConfig(self, homeId):
        lib.CManagerWriteConfig(self.manager, homeId)


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
