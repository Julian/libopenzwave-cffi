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
    typedef void* COptions;
    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
    """
)
ffi.compile()
