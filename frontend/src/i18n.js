import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

function loadLocaleMessages() {
    const locales = require.context('./locales', true, /[A-Za-z0-9-_,\s]+\.json$/i)
    const messages = {}
    locales.keys().forEach(key => {
        const matched = key.match(/([A-Za-z0-9-_]+)\./i)
        if (matched && matched.length > 1) {
            const locale = matched[1]
            messages[locale] = locales(key)
        }
    })
    return messages
}

function loadLanguage() {
    if (window.localStorage.getItem('store')) {
        const store = JSON.parse(window.localStorage.getItem('store'))
        if (store.context.language) return store.context.language
    }
    const browserLang = navigator.language.substring(0, 2).toLowerCase()
    const availableLang = process.env.VUE_APP_LANGUAGES
    if (availableLang.includes(browserLang)) return browserLang
    else return 'pl'
}

export default new VueI18n(
    {
        locale: loadLanguage(),
        fallbackLocale: 'en',
        messages: loadLocaleMessages()
    },
    loadLanguage()
)
