<template>
  <div id="app">
    <navbar/>
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
import navbar from '@/components/navbar'

export default {
  name: 'App',
  components:{navbar}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 1em;
}
navbar{
  margin-bottom: 1em;
}
</style>
