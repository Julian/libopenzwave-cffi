#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    typedef void (*cPfnOnNotification_t)(CNotification const*, void*);

    CManager newCManager(void);
    bool CManagerAddWatcher(CManager, cPfnOnNotification_t, void*);

    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
#ifdef __cplusplus
}
#endif
