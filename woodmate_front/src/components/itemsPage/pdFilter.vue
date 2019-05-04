<template>
  <div class="container-fluid" id="ft">
    <p>Filter</p>
    <hr>
    <!-- <p>{{ filter  }}</p> -->
    <label class="pure-material-checkbox">
          <input type="checkbox" id="pd-filter" style="float:right">

          <span>สินค้าใหม่</span>
        </label>
    <p style="margin-bottom:.2em">
      <b>ประเภท</b>
    </p>
    <ul class="filter-list">
      <li v-for="t in type" v-model="selectd" class="filter-items">
        <label class="pure-material-checkbox">
          <input type="checkbox" id="pd-filter" style="float:right" :value="t.product_type_id" v-model="select" @change="pushPull">

          <span>{{ t.product_type_name }}</span>
        </label>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  name: "Product filter",
  data() {
    return {
      select: []
    };
  },
  computed: {
    ...mapState(["type"]),
  },
  methods:{
      pushPull(e){
          this.$store.commit('setFilter', this.select)
      }
  }
};
</script>

<style>
#ft {
  text-align: left;
}
.filter-list {
  list-style-type: none;
}
.filter-items {
}

.pure-material-checkbox {
  z-index: 0;
  position: relative;
  display: inline-block;
  color: rgba(var(--pure-material-onsurface-rgb, 0, 0, 0), 0.87);
  font-family: var(
    --pure-material-font,
    "Roboto",
    "Segoe UI",
    BlinkMacSystemFont,
    system-ui,
    -apple-system
  );
  font-size: 16px;
  line-height: 1.5;
}

/* Input */
.pure-material-checkbox > input {
  appearance: none;
  -moz-appearance: none;
  -webkit-appearance: none;
  z-index: -1;
  position: absolute;
  left: -10px;
  top: -8px;
  display: block;
  margin: 0;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  background-color: rgba(var(--pure-material-onsurface-rgb, 0, 0, 0), 0.6);
  box-shadow: none;
  outline: none;
  opacity: 0;
  transform: scale(1);
  pointer-events: none;
  transition: opacity 0.3s, transform 0.2s;
}

/* Span */
.pure-material-checkbox > span {
  display: inline-block;
  width: 100%;
  cursor: pointer;
}

/* Box */
.pure-material-checkbox > span::before {
  content: "";
  display: inline-block;
  box-sizing: border-box;
  margin: 3px 11px 3px 1px;
  border: solid 2px; /* Safari */
  border-color: rgba(146, 153, 161, 0.644);
  border-radius: 2px;
  width: 18px;
  height: 18px;
  vertical-align: top;
  transition: border-color 0.2s, background-color 0.2s;
}

/* Checkmark */
.pure-material-checkbox > span::after {
  content: "";
  display: block;
  position: absolute;
  top: 3px;
  left: 1px;
  width: 10px;
  height: 5px;
  border: solid 2px transparent;
  border-right: none;
  border-top: none;
  transform: translate(3px, 4px) rotate(-45deg);
}

/* Checked, Indeterminate */
.pure-material-checkbox > input:checked,
.pure-material-checkbox > input:indeterminate {
  background-color: #2c3e50;
}

.pure-material-checkbox > input:checked + span::before,
.pure-material-checkbox > input:indeterminate + span::before {
  border-color: #2c3e50;
  background-color: #2c3e50;
}

.pure-material-checkbox > input:checked + span::after,
.pure-material-checkbox > input:indeterminate + span::after {
  border-color: rgb(var(--pure-material-onprimary-rgb, 255, 255, 255));
}

.pure-material-checkbox > input:indeterminate + span::after {
  border-left: none;
  transform: translate(4px, 3px);
}

/* Disabled */
.pure-material-checkbox > input:disabled {
  opacity: 0;
}

.pure-material-checkbox > input:disabled + span {
  color: rgba(var(--pure-material-onsurface-rgb, 0, 0, 0), 0.38);
  cursor: initial;
}

.pure-material-checkbox > input:disabled + span::before {
  border-color: currentColor;
}

.pure-material-checkbox > input:checked:disabled + span::before,
.pure-material-checkbox > input:indeterminate:disabled + span::before {
  border-color: transparent;
  background-color: currentColor;
}
</style>
