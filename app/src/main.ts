import { createApp } from 'vue'
import { createPinia } from 'pinia'
// @ts-ignore
import { SplashScreen } from '@capacitor/splash-screen'
import 'mini-k-tailwind/skeleton.css'
import './assets/styles.scss'
SplashScreen.hide()

import App from './App.vue'
import router from './router'
import i18n from './lang/i18n'

const app = createApp(App)

app.use(createPinia())
app.use(i18n)
app.use(router)

app.mount('#app')
