<template>
  <nav class="navbar">
    <div class="container-fulid" id="top-nav">
      <div class="row">
        <!-- <div class="col-sm" id="inform">
          <p>woodmate group | Web programming</p>
        </div>-->
        <div class="col-sm my-auto">
          <h2>WoodMate</h2>
        </div>
        <div class="col-sm my-auto">
          <div class="container-fulid">
            <ul class="nav-option">
              <li>
                <a href="#" target="_self">สินค้า</a>
              </li>
              <li>
                <a href="#" target="_self">มาใหม่</a>
              </li>
              <li>
                <a href="#" target="_self">โปรโมชั่น</a>
              </li>
              <li>
                <a href="#" target="_self">เกียวกับ</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-sm my-auto">
          <p>
            <i class="fas fa-search" id="searchIcon"></i>
            <transition>
              <input type="text" placeholder="Search.." name="search" class="inputText">
            </transition>
            <router-link to="/login" class="icon">
              <i class="far fa-user fa-lg"></i>
            </router-link>&ensp;
            <a href="#" class="icon">
              <i class="fas fa-shopping-cart fa-lg"></i>
            </a>
          </p>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "navbar",
  data() {
    return {};
  },
  methods: {}
};
</script>

<style>
#inform {
  color: rgb(156, 156, 156);
}
.icon {
  color: #2f2d2e;
  transition: 0.1s;
}
.icon:hover {
  color: #f18f01;
}
.row {
  width: 100%;
}
#top-nav {
  display: flex;
}
.navbar {
  padding-top: 1em;
  margin: 2em auto;
  display: block;
}
.nav-option {
  /* float: left; */
}

.nav-option > li {
  list-style-type: none;
  display: inline-block;
  float: none;
  padding: 0 1em;
}
.nav-option > li > a {
  color: #2f2d2e;
  text-decoration: none;
  font-size: 1.1em;
  transition: 0.2s;
}
.nav-option > li > a:hover {
  color: #f18f01;
}
.inputText {
  border: none;
  border-bottom: 1px solid #2f2d2e;
  transition: 0.4s;
  margin: 0.5em;
  padding: 0.3em 1em;
}
</style>
