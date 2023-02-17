import win32api
import win32con
import logging 
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] %(message)s', filename='watchRegistry.log')
log = logging.getLogger()

hiveToWatch = win32con.HKEY_LOCAL_MACHINE
keyToWatch = r'SOFTWARE\Realtek\SpkProtection'

values = {(hiveToWatch, keyToWatch, 'DateTime'): (win32con.REG_DWORD, 1),
          (hiveToWatch, keyToWatch, 'Templates'): (win32con.REG_DWORD, 0),
          (hiveToWatch, keyToWatch, 'UnitConv'): (win32con.REG_DWORD, 0)}

while True:

    for (hive, key, valueName), (valueType, value) in values.items():
        handleWithSetRights = win32api.RegOpenKeyEx(hive, key, 0, win32con.KEY_SET_VALUE)
        log.info(r'Setting %s\%s\%s = %s' % (hive, key, valueName, value))
        win32api.RegSetValueEx(handleWithSetRights, valueName, 0, valueType, value)
        win32api.RegCloseKey(handleWithSetRights)

    # Open and close the handle here as otherwise the set operation above will trigger a further round
    handleToBeWatched = win32api.RegOpenKeyEx(hiveToWatch, keyToWatch, 0, win32con.KEY_NOTIFY)
    win32api.RegNotifyChangeKeyValue(handleToBeWatched, False, win32api.REG_NOTIFY_CHANGE_LAST_SET, None, False)
    win32api.RegCloseKey(handleToBeWatched)