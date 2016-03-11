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
    """
)
ffi.compile()
