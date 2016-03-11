#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif
    typedef void* COptions;
    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
#ifdef __cplusplus
}
#endif
