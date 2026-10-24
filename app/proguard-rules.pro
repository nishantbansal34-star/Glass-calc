# The page calls these through window.NRRL; keep them for the WebView bridge.
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-keepattributes JavascriptInterface
