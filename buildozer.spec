[app]
title = Game Exam App
package.name = gameexamapp
package.domain = com.obsanurgi
source.dir = .
source.include_exts = py, png, jpg, kv, atlas, json

version = 0.1
requirements = python3, kivy==2.3.0, reportlab, hostpython3, libffi

orientation = portrait
fullscreen = 0

# Android specific
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True
android.enable_androidx = True

# Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
