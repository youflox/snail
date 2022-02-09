import { createStore } from "vuex";

export default createStore({
  state: {
    baseUrl: "http://127.0.0.1:8000",
    authenticated: false,
    user: {
      id: "",
      username: "",
    },
  },
  mutations: {},
  actions: {},
  modules: {},
});
