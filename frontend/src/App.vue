<template>
  <div id="app">
    <Navbar />
    <InputPosts />
    <GetPosts />
  </div>
</template>

<script>

import Navbar from "./components/Navbar.vue";
import InputPosts from "./components/InputPosts.vue";
import GetPosts from "./components/GetPosts.vue";

export default {
  name: "app",
  components: {
    Navbar,
    InputPosts,
    GetPosts,
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>