import winreg
def padding(cnt):
    str = ""
    for i in range(cnt):
        str += '\t'
    return str

def recursive_visit(folder, i):
    subfolders_count, subkeys_count, modified = winreg.QueryInfoKey(folder)
    for subfolder_index in range(subfolders_count):
        try:
            subfolder_name = winreg.EnumKey(folder, subfolder_index)
            print(padding(i)+subfolder_name+":")
            with winreg.OpenKeyEx(folder, subfolder_name) as subfolder:
                recursive_visit(subfolder, i+1)
        except (WindowsError, KeyError, ValueError):
            print("Error reading " + folder)
    for subkey_index in range(subkeys_count):
        print(padding(i)+str(winreg.EnumValue(folder, subkey_index)))
        globals()["cnt"] += 1

cnt = 0 #how many keys we visited

### ENTER INPUT HERE
root = winreg.HKEY_LOCAL_MACHINE
folder = r"SYSTEM\Setup\FirstBoot\Services"
###

with winreg.OpenKey(root, folder) as reg:
    keys_count, values_count, modified = winreg.QueryInfoKey(reg)
    print("Subfolders: " + str(keys_count) + " Subkeys: " + str(values_count))
    recursive_visit(reg, 1)
print("visited " + str(cnt) + " leaf keys")