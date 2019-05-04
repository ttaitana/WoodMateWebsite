import Vue from 'vue'
import Vuex from 'vuex'
import product from '@/assets/itemList.json'

// Make vue aware of Vuex
Vue.use(Vuex)

// Create an object to hold the initial state when
// the app starts up
const state = {
  products: product.product,
  type: product.product_type,
  // TODO: Set up our initial state
}

// Create an object storing various mutations. We will write the mutation
const mutations = {
  setFilter(state, flt){
    if(flt.length == 0){
      state.products = product.product
    }else{
      state.products = product.product.filter(pdt => {
        console.log(flt.includes(pdt.product_type_id))
        return flt.includes(pdt.product_type_id)
      });
      // console.log(state.products)
    }
  }
  // TODO: set up our mutations
}

const store = new Vuex.Store({
  state,
  mutations
})

// Combine the initial state and the mutations to create a Vuex store.
// This store can be linked to our app.
export default store;