<template>
 <div class="login-header">
     <div class="headerLeft">
         <router-link to="/">
         <
         </router-link>
     </div>
     <div class="headerTitle">
         <div class="title">ログイン</div>
     </div>
 </div>
</template>

<script>
    import {Component, Vue} from "vue-property-decorator";
    @Component({
        components:{}
    })
    export default class Header extends Vue{

    }
</script>

<style scoped lang="stylus">
    .login-header
        display flex
        height .86rem
        line-height .86rem
        border-bottom: 1px solid #e5e5e5;
        width: 100%;
        position: relative
        .headerLeft
            margin-left .3rem
            float left
        .headerTitle
            height .64rem
            font-size .4rem
            padding-left 2.5rem
</style>
