[app]
# App name
title = MyApp

# Package name, used as the app's identifier
package.name = myapp
package.domain = org.test

# Source code directory
source.dir = .

# Source files
source.include_exts = py,png,jpg,kv,atlas

# Requirements (libraries needed)
requirements = python3,kivy,reportlab,libffi

# Entry point of the app
entrypoint = main.py

# Icon
icon.filename = icon.png

# Orientation
orientation = portrait

# Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Version code and version name
version.code = 1
version.name = 1.0.0

# Presplash (splash screen) - optional
# presplash.filename = presplash.png

# Splash screen timeout
# presplash.duration = 3

# Android API level
android.api = 33

# Android SDK version
android.sdk = 33

# Android NDK version
android.ndk = 23b

# Build mode
# 'debug' or 'release'
android.debug = 1

# Extra options
# (Add any extra build options here)
