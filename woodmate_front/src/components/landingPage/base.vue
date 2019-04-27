<template>
  <div class="container-fulid">
    <recom/>
  </div>
</template>

<script>
import recom from './recommend'

export default {
  name: "landingPage",
  components: {recom},
  data() {
    return {
      mas: "none"
    };
  }
};
</script>

<style>
</style>
