# # importing required module
# import winreg as wrg

# # Store location of HKEY_CURRENT_USER
# location = wrg.HKEY_CURRENT_USER

# # Store path in soft
# soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
# key_1 = wrg.CreateKey(soft, "sandeep")

# # Creating values in sandeep
# wrg.SetValueEx(key_1, "value One", 0, wrg.REG_SZ,
# 			"sandeeppatel")
# wrg.SetValueEx(key_1, "value Two", 0, wrg.REG_SZ,
# 			"Participate in Technical Scripter")

# if key_1:
# 	wrg.CloseKey(key_1)
# importing required module
# import winreg as wrg

# # Store location of HKEY_CURRENT_USER
# location = wrg.HKEY_CURRENT_USER

# # Storing path in soft
# soft = wrg.OpenKeyEx(location,r"SOFTWARE\\sandeep\\")

# # reading values in value_1 and value_2
# value_1 = wrg.QueryValueEx(soft,"Value One")
# value_2 = wrg.QueryValueEx(soft,"Value Two")

# # Closing folder
# if soft:
# 	wrg.CloseKey(soft)

# # Printing values
# print(value_1)
# print(value_2)
#////////////////////////////
import winreg as wrg
  
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_CURRENT_USER
  
# Store path in soft
# soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
# key_1 = wrg.CreateKey(soft, "sandeep")
  
# # Deleting Value One in sandeep
# del_val_one = wrg.DeleteValue(key_1, "Value One")
  
# # Deleting Value Two in sandeep
# del_val_two = wrg.DeleteValue(key_1, "Value Two")
  
# # Closing folder
# if key_1:
#     wrg.CloseKey(key_1)
#///////////////////////
import winreg as wrg
  
# Store location of HKEY_CURRENT_USER
location = wrg.HKEY_CURRENT_USER
  
# Store complete path in soft
soft = wrg.OpenKeyEx(location, r"SOFTWARE\\")
key_1 = wrg.CreateKey(soft, "sandeep")
  
# Deleting the foler sandeep
del_key = wrg.DeleteKey(key_1, "")
  
# Closing folder
if key_1:
    wrg.CloseKey(key_1)