#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    /* XXX: I can't figure out the right way to do this.
     *      This typedef is OpenZWave::Manager::pfnOnNotification_t. */
    typedef void* cpfnOnNotification_t;

    CManager newCManager(void);
    bool CManagerAddWatcher(CManager, cpfnOnNotification_t, void*);
    bool CManagerAddDriver(CManager, const char*);

    COptions newCOptions(const char*, const char*, const char*);
    bool COptionsAddString(COptions, const char*, const char*, bool);
    bool COptionsAddBool(COptions, const char*, bool);
    bool COptionsAddInt(COptions, const char*, int32_t);
    bool COptionsLock(COptions);
    bool COptionsAreLocked(COptions);
#ifdef __cplusplus
}
#endif
