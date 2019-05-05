import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'
import product from '@/assets/itemList.json'

// defin vuexPersist
const vuexPersist = new VuexPersist({
  key: 'my-app',
  storage: localStorage
})

// Make vue aware of Vuex
Vue.use(Vuex)

// Create an object to hold the initial state when
// the app starts up
const state = {
  products: product.product,
  type: product.product_type,
  cart: [],
  cartsize: 0
  // TODO: Set up our initial state
}

// Create an object storing various mutations. We will write the mutation
const mutations = {
  setFilter(state, flt){
    if(flt.length == 0){
      state.products = product.product
    }else{
      state.products = product.product.filter(pdt => {
        // console.log(flt.includes(pdt.product_type_id))
        return flt.includes(pdt.product_type_id)
      });
      // console.log(state.products)
    }
  },
  addCart(state, item){

    function isInCart(base, obj){
      console.log('item')
      // console.log(obj.item.product_id)
      // console.log(base)
      let ss = true
      let index = 0
      for(let i in base){
        if(base[i].item.product_id === obj.item.product_id){
          console.log('pass')
          state.cart[index] = {'item': obj.item, 'amount':Number(obj.amount) + state.cart[index].amount}
          ss = false
          break
        }
        index++
      }

      if(ss){
        state.cart.push({'item': obj.item, 'amount':Number(obj.amount)})
      }
    }
    isInCart(state.cart, item)
    console.log(state.cart)
    // state.cart.push(item)
    // if(state.cart.has(item.item.product_id)){
    //   console.log(state.cart.get(item.item.product_id).amount)
    //   state.cart.set(item.item.product_id, {'item':item.item, 'amount':Number(item.amount) + state.cart.get(item.item.product_id).amount})
    // }else{
    //   state.cart.set(item.item.product_id, {'item':item.item, 'amount':Number(item.amount)})
    // }


    let amt = 0
    function logMapElements(value, key, map) {
      amt += value.amount;
    }

    let items = state.cart
    items.forEach(logMapElements)
    // console.log(amt)
    state.cartsize = amt
    // console.log(state.cart)
  }
  // TODO: set up our mutations
}

const store = new Vuex.Store({
  state,
  mutations,
  plugins: [vuexPersist.plugin]
})

// Combine the initial state and the mutations to create a Vuex store.
// This store can be linked to our app.
export default store;