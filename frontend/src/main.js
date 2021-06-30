import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import i18n from "./i18n";
import axios from "axios";
import VueMask from "v-mask";

Vue.prototype.$axios = axios;
Vue.config.productionTip = false;
Vue.use(VueMask);

new Vue({
  router,
  store,
  vuetify,
  i18n,
  render: h => h(App)
}).$mount("#app");
