const store = {
  namespaced: true,

  state: {
    language: undefined
  },

  mutations: {
    CHANGE_LANGUAGE(state, language) {
      state.language = language;
    }
  },

  actions: {
    changeLanguage(context, language) {
      context.commit("CHANGE_LANGUAGE", language);
    }
  },

  getters: {
    getLanguage(state) {
      return state.language;
    }
  }
};

export default store;
