from _libopenzwave import ffi, lib

from libopenzwave import __version__
from libopenzwave._global import COMMAND_CLASS_DESC, PyNotifications


class PyManager(object):

    COMMAND_CLASS_DESC = COMMAND_CLASS_DESC

    @classmethod
    def getOzwLibraryVersion(cls):
        return ffi.string(lib.CManagerGetVersionAsString())

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

    def getDriverStatistics(self, homeId):
        data = ffi.new("DriverData *")
        statistics = lib.CManagerGetDriverStatistics(
            self.manager, homeId, data,
        )
        return statistics

    def getPythonLibraryVersion(self):
        version = self.getPythonLibraryVersionNumber()
        return "python-openzwave+cffi v%s" % (version,)

    def getPythonLibraryVersionNumber(self):
        return __version__

    def getNodeClassInformation(self, homeId, nodeId, commandClassId):
        className, classVersion = ffi.new("char **"), ffi.new("uint8_t *")
        return lib.CManagerGetNodeClassInformation(
            self.manager,
            homeId,
            nodeId,
            commandClassId,
            className,
            classVersion,
        )

    def getNodeNeighbors(self, homeId, nodeId):
        neighbors = ffi.new("uint8_t*[29]")
        count = lib.CManagerGetNodeNeighbors(
            self.manager, homeId, nodeId, neighbors,
        )
        return list(neighbors[0][0:count])


def _bind(return_type, name):
    wrapped = getattr(lib, "CManager" + name[0].upper() + name[1:])

    if return_type is None:
        def boundManagerFunction(self, *args):
            wrapped(self.manager, *args)
    else:
        def boundManagerFunction(self, *args):
            return return_type(wrapped(self.manager, *args))

    boundManagerFunction.__name__ = name
    return boundManagerFunction


for name, return_type, setter in [
    ("isBridgeController", bool, False),
    ("isNodeFrequentListeningDevice", bool, False),
    ("isNodeBeamingDevice", bool, False),
    ("isNodeListeningDevice", bool, False),
    ("isNodeRoutingDevice", bool, False),
    ("isNodeSecurityDevice", bool, False),
    ("isPrimaryController", bool, False),
    ("isStaticUpdateController", bool, False),
    ("addDriver", bool, False),
    ("removeDriver", bool, False),
    ("cancelControllerCommand", bool, False),
    ("getLibraryTypeName", ffi.string, False),
    ("getLibraryVersion", ffi.string, False),
    ("getNodeManufacturerId", ffi.string, False),
    ("getNodeManufacturerName", ffi.string, True),
    ("getNodeLocation", ffi.string, True),
    ("getNodeName", ffi.string, True),
    ("getNodeProductId", ffi.string, False),
    ("getNodeProductName", ffi.string, True),
    ("getNodeProductType", ffi.string, False),
    ("getNodeVersion", int, False),
    ("getNumGroups", int, False),
    ("getSendQueueCount", int, False),
    ("writeConfig", None, False),
]:
    setattr(PyManager, name, _bind(name=name, return_type=return_type))
    if setter:
        name = name.replace("get", "set")
        setattr(PyManager, name, _bind(return_type=None, name=name))


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
