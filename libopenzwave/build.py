from cffi import FFI


ffi = FFI()
ffi.set_source(
    "_libopenzwave",
    """
    #include "libopenzwavec.h"
    """,
    libraries=["openzwavec"],
)
ffi.cdef(
    """
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void (*cPfnOnNotification_t)(CNotification const*, void*);

    CManager newCManager(void);
    bool CManagerAddWatcher(CManager, cPfnOnNotification_t, void*);
    extern "Python" void add_manager_callback(CManager, cPfnOnNotification_t*, void*);

    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
    """
)


@ffi.def_extern()
def add_watcher_callback(context):
    callback = ffi.from_handle(context)
    callback()


ffi.compile()
