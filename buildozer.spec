[app]

title = ExamSystem
package.name = examsystem
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 1.0

requirements = python3,kivy,reportlab

orientation = portrait

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b

# 🔥 IMPORTANT FIX FOR AIDL + BUILD TOOLS
android.enable_androidx = True
android.gradle_dependencies =