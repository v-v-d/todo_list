<template>
  <div id="app">
    <NavBar/>
    <TodoList/>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar";
import TodoList from "@/components/TodoList";

export default {
  name: 'App',
  components: {
    NavBar,
    TodoList,
  },
}
</script>

<style>

</style>
