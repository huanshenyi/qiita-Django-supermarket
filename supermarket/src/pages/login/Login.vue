<template>
    <div class="login">
        <login-header></login-header>
        <login-content></login-content>
    </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import LoginHeader from "./components/Header.vue";
import LoginContent from "./components/Content.vue";
@Component({
    components:{
        LoginHeader,
        LoginContent
    }
})
export default class Login extends Vue{

}
</script>

<style scoped>

</style>
