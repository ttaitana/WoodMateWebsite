<template>
  <div class="container-fulid" id="frame">
    <img src="https://d26iwjla857pn6.cloudfront.net/2.0/og-image.jpg" alt>
    <div class="container" id="text-holder">
      <p class="title">Dream house</p>
      <hr>
      <p>สวยอย่างคลาสสิกด้วยเฟอร์นิเจอร์ไม้จาก woodmate</p>
      <a href="#">
          <button type="button" class="btn btn-outline-dark" id="mainbtn">
              ดูสินค้า
          </button>
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: "recommend",
  data() {
    return {};
  }
};
</script>

<style>
hr{
    width: 15vh;
    border: 1.5px solid #2f2d2e;
}
#text-holder{
    
}
.title {
  text-transform: uppercase;
  font-size: 2em;
}
img {
  width: 100%;
  /* transform: translateY(-30vh);  */
  position: absolute;
  left: 0px;
  top: 0px;
  z-index: -10;
}
#frame {
    padding-top: 15vh;
  margin: 0 auto;
  position: relative;
  height: 86vh;
  overflow: hidden;
}
#mainbtn{
    width: 10em;
    border-radius: 0;
}
</style>
