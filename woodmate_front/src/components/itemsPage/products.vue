<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-6 items" v-for="p in products">
        <div class="row">
          <div class="col pd-img">
            <img :src="p.image" alt>
          </div>
          <div class="col pd-detail">
            <p class="pd-title">
              <b style="float:left">{{ p.product_name }}</b>
              <b style="float:right" class="pd-price">{{ p.price.toLocaleString() }} ฿</b>
            </p>
            <br>
            <p class="pd-desc">{{ p.product_desc }}</p>
            <br>
            <div class="form-group row">
              <label for="amount" class="col-3 col-form-label">จำนวน</label>
              <input
                type="number"
                min="0"
                :max="p.stock"
                value="1"
                class="form-control"
                style="width: 5em;"
                :id="'item' + p.product_id"
              >
            </div>
            <br>
            <button type="button" class="button" @click="addToCart(p)">
              เพิ่มสินค้าลงตะกร้า
              &ensp;
              <i class="fas fa-arrow-right"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "items",
  data() {
    return {};
  },
  methods: {
    addToCart(pd) {
      let amt = document.querySelector("#item" + pd.product_id);

      if (amt.value > 0) {
        this.$store.commit("addCart", { item: pd, amount: amt.value });
        amt.value = 1;
        alert(
          "เพิ่มสินค้า " + pd.product_name + " จำนวน " + amt.value + " ชิ้น"
        );
      }
    }
  },
  computed: {
    ...mapState(["products"])
  }
};
</script>

<style>
.button {
  padding: 0.7em 2em;
  color: white;
  border-radius: 0;
  border: none;
  background: #ff7865;
}
.items {
  padding: 1em 1em 3em 1em;
}
.pd-title {
  font-size: 1.2em;
}
.pd-detail {
  text-align: left;
}
.pd-desc {
  color: rgb(111, 134, 160);
}
.pd-img > img {
  width: 100%;
  height: auto;
}
</style>
