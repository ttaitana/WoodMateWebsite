<template>
    <div class="container-fliud">
        <div class="row setcenter" v-for="itm in cart">
            <div class="col-1 vertical_al">
                <input type="checkbox">
            </div>
            <div class="col-7 vertical_al">
                <div class="row">
                    <div class="col-3">
                        <img :src="itm.item.image" alt="" class="imgct">
                    </div>
                    <div class="col-9">
                        {{ itm.item.product_name }}
                    </div>
                </div>
            </div>
            <div class="col-2 price">
                <p>
                    ฿ {{ itm.item.price.toLocaleString() }}
                </p>
            </div>
            <div class="col-2 amt_con">
                <div class="box"><i class="fas fa-minus"></i></div>
                <input type="number" :value="itm.amount" class="amt_in">
                <div class="box"><i class="fas fa-plus"></i></div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex";

export default {
    name:'cartitem',
    computed:{
        ...mapState(['cart'])
    }
}
</script>

<style>
.imgct{
    width: 100%;
}
.box{
    width: 2em;
    height: 2em;
    border: 1px solid #2F2D2E;
    color: rgb(129, 129, 129);
    cursor: pointer;
    border: none;
    background: rgb(238, 238, 238);
}
.amt_con{
    display: flex;
}
.amt_in{
    width: 3em;
    height: 2em;
    text-align: center;
    margin-left: .5em;
    border: none;
}
.setcenter{
    position: relative;
}
.price{
    color: #f18f01;
    font-size: 1.3em;
}
</style>
