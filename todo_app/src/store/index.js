import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import todoList from './modules/todoList'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    auth,
    todoList,
  },
})
