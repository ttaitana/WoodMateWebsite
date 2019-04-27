<template>
  <div id="app">
    <navbar v-if="['login', 'register'].indexOf($route.name) < 0"/>
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
import navbar from '@/components/navbar'
import store from './vuex/store'

export default {
  name: 'App',
  components:{navbar},
  store,
  mounted(){
      console.log(this.$route.name);
      console.log(['login'].indexOf(this.$route.name))
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 1em; */
}
navbar{
  margin-bottom: 1em;
}
</style>
