import { createI18n } from 'vue-i18n'
import us from './us'
import fa from './fa'

const i18n = createI18n({
    legacy: false,
    locale: (localStorage.getItem("app-language") as "fa" | "us") || "us",
    fallbackLocale: 'us',
    messages: {
        us,
        fa,
    },
})

export default i18n