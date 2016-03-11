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

    typedef void (*pfnOnNotification_t)(CNotification const* _pNotification, void* _context);

    CManager newCManager(void);
    bool CManagerAddWatcher(CManager, pfnOnNotification_t notification, void* context);

    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
    """
)
ffi.compile()
