from cffi import FFI


ffi = FFI()
ffi.set_source(
    "_libopenzwave",
    '#include "libopenzwavec.h"',
    libraries=["openzwavec"],
    source_extension=".cpp",
)
ffi.cdef(
    """
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void* pfnOnNotification_t;
    typedef int... NotificationType;

    CManager newCManager(void);
    void destroyCManager(CManager);
    bool CManagerAddWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerRemoveWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerAddDriver(CManager, const char*);
    bool CManagerRemoveDriver(CManager, const char*);
    bool CManagerCancelControllerCommand(CManager, uint32_t const);
    const char* CManagerGetLibraryTypeName(CManager, uint32_t);
    const char* CManagerGetLibraryVersion(CManager, uint32_t);
    int32_t CManagerGetSendQueueCount(CManager, uint32_t const);
    void CManagerSetNodeName(CManager, uint32_t, uint8_t, const char*);
    void CManagerSetNodeLocation(CManager, uint32_t, uint8_t, const char*);
    void CManagerWriteConfig(CManager, uint32_t const);
    extern "Python" void do_manager_watcher_callback(CManager, void* pythonFn);

    NotificationType CNotificationGetType(CNotification);
    uint32_t CNotificationGetHomeId(CNotification);
    uint8_t CNotificationGetNodeId(CNotification);

    COptions newCOptions(const char*, const char*, const char*);
    void destroyCOptions(COptions);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
    """
)

ffi.compile()
