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

    CManager newCManager(void);
    void destroyCManager(CManager);
    bool CManagerAddWatcher(CManager, ...);
    extern "Python" void manager_watcher_callback(CManager, void*, void*);
    bool CManagerAddDriver(CManager, const char*);

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
