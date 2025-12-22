import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.tinco.app',
  appName: 'tinco',
  webDir: 'dist',
  plugins: {
    SplashScreen: {
      launchShowDuration: 3000, // مدت نمایش (میلی‌ثانیه)
      launchAutoHide: true,     // بعد از لود شدن Vue مخفی شود
      backgroundColor: "#000000", // رنگ پس‌زمینه
      androidScaleType: "CENTER_CROP",
      showSpinner: true
    }
  }
}
export default config;
