from cffi import FFI


ffi = FFI()
ffi.set_source(
    "_libopenzwave", '#include "libopenzwavec.h"', libraries=["openzwavec"],
)
ffi.cdef(
    """
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void* pfnOnNotification_t;
    typedef void* NotificationType;

    CManager newCManager(void);
    void destroyCManager(CManager);
    bool CManagerAddWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerAddDriver(CManager, const char*);
    const char* CManagerGetLibraryTypeName(CManager, uint32_t);
    const char* CManagerGetLibraryVersion(CManager, uint32_t);
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
