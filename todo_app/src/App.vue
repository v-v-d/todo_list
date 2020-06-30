<template>
  <div id="app">
    <NavBar/>
    <TodoList/>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import NavBar from "@/components/NavBar";
import TodoList from "@/components/TodoList";

export default {
  name: 'App',
  components: {
    NavBar,
    TodoList,
  },
  computed: mapGetters(['isToken']),
  methods: mapActions(['getTokenFromLocalStorage', 'getUser']),
  mounted() {
    this.getTokenFromLocalStorage();

    if (this.isToken) {
      this.getUser();
    }
  },
}
</script>

<style>

</style>
