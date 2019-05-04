<template>
  <div class="container-fluid" id="frame">
    <div class="jumbotron">
      <h1 class="display-4">Hello, world!</h1>
      <p
        class="lead"
      >This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
      <hr class="my-4">
      <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
      <p class="lead">
        <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
      </p>
    </div>
    <div class="row" id="products">
      <div class="col-3">
        <filters/>
      </div>
      <div class="col">
        <products/>
      </div>
    </div>
  </div>
</template>

<script>
import products from "./products";
import filters from "./pdFilter";
export default {
  name: "itemsPage",
  data(){},
  components: {
    products,
    filters
  },
  data() {
    return {};
  }
};
</script>

<style>
#frame {
  padding: 0 3em;
}
#products{
    padding-top: 1em;
}
</style>
