#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
#include "openzwave/Manager.h"
#include "openzwave/Notification.h"

extern "C" {
#endif
    typedef void* CManager;
    typedef void* CNotification;
    typedef void* COptions;

    /* XXX: I can't figure out if I can access this from C and not need void* ?
     * */
#ifdef __cplusplus
    typedef OpenZWave::Manager::pfnOnNotification_t pfnOnNotification_t;
    typedef OpenZWave::Notification::NotificationType NotificationType;
#else
    typedef void* pfnOnNotification_t;
    typedef void* NotificationType;
#endif

    CManager newCManager(void);
    void destroyCManager(CManager);
    bool CManagerAddWatcher(CManager, pfnOnNotification_t, void* context);
    bool CManagerAddDriver(CManager, const char*);

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
#ifdef __cplusplus
}
#endif
