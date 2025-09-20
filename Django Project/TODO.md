# Django URL Configuration Improvements

## Issues Fixed:
1. ✅ Fixed import error in views.py (UserRegistrationForm -> CustomRegistrationForm)
2. 🔄 Restructure main URLs to use include() pattern
3. 🔄 Clean up tweet app URLs and remove redundancy
4. 🔄 Add missing tweet detail URL pattern
5. 🔄 Fix template inconsistencies

## Plan:
1. **Main URLs Restructure** (`comment/comment/urls.py`)
   - Remove direct tweet view references
   - Use include() to reference tweet app URLs
   - Keep only project-level URLs

2. **Tweet App URLs Cleanup** (`comment/tweet/urls.py`)
   - Remove redundant URL patterns
   - Add tweet detail URL pattern
   - Organize URLs properly

3. **Add Missing Functionality**
   - Add tweet detail view and URL
   - Ensure proper URL naming

4. **Template Standardization**
   - Standardize template usage between create/edit views
