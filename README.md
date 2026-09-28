# NRRL Glass Calc

NRRL's business calculator: all-black liquid glass with the gold NRRL logo, an editable cursor, and GST, margin and discount tools.

**Install:** open the latest release on this repo → download the `.apk` → open it to install. New builds install over the old one and keep your history.

Each push to `main` builds a new APK automatically (Actions tab → "Build APK"), published as a release.

The calculator page is `web/index.html`. After editing it, run `python3 tools/make_app_html.py` to refresh the app copy in `app/src/main/assets/`. The app runs fully offline (no INTERNET permission).
