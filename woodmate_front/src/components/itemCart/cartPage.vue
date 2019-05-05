<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-8">
                <cartitem/>
            </div>
            <div class="col-4"></div>
        </div>
    </div>
</template>

<script>
import cartitem from './cartItem'
export default {
    name: 'cartpage',
    components:{
        cartitem
    }
    
}
</script>

<style>

</style>
