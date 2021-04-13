import Vue from "vue";
import Vuex from "vuex";
import VuexPersist from "vuex-persist";
import context from "./modules/context";
import cart from "./modules/cart";

Vue.use(Vuex);

const vuexLocalStorage = new VuexPersist({
  key: "store",
  storage: window.localStorage
});

export default new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    context,
    cart
  },
  getters: {},
  plugins: [vuexLocalStorage.plugin]
});
