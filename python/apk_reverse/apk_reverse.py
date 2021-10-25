from pyaxmlparser import APK


apk = APK('web_221_20200810.apk')
print(apk.package)
print(apk.version_name)
print(apk.version_code)
print(apk.icon_info)
print(apk.icon_data)
print(apk.application)