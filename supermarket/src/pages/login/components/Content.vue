<template>
    <div class="login-content">
        <div class="logo">
            <img class="logoimg"
                 src="data:image/jpeg;base64,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" alt="">
        </div>
        <div class="itemContent">
            <div class="login">
                <div class="input-container">
                    <input type="text" class="username" v-model="userName" placeholder="ユーザーネーム/アドレス">
                </div>
                <div class="input-container">
                    <input type="password" class="username" v-model="passWord" placeholder="パスワード">
                    <div class="agin">パスワード再発行</div>
                </div>
            </div>
            <div class="loginbtn" @click="loginfuc">ログイン</div>
            <div class="registration">
                <div class="registerbtn">新規登録</div>
            </div>
            <div class="logintype">
                <div class="quick-login">
                    <h4 class="txt-otherLogin">それ以外のログイン</h4>
                    <a href="" class="icon">GitHub</a>
                    <a href="" class="icon">Qiita</a>
                </div>
                <div class="agreement-tips">
                    <p>https://github.com/huanshenyi/qiita-Django-supermarket</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
    import {Component, Vue, Provide} from "vue-property-decorator";
    @Component({
        components:{}
    })
    export default class Content extends Vue{
     @Provide() userName:string = "";
     @Provide() passWord:string = "" ;
     loginfuc () {
        console.log("ログインが推された");
        (this as any).$router.push("/")
     }
    }
</script>

<style scoped lang="stylus">
    .login-content
        padding: 0 .25rem .25rem;
        .logo
            width 100%
            height 20%
            text-align center
            .logoimg
                width 2rem
                height 2rem
        .itemContent
            max-width: 7.5rem;
            margin: 0 auto;
            .input-container
                height: 100%;
                padding-top: .2rem;
                padding-bottom: .2rem;
                position: relative;
                overflow: hidden;
                margin-top: .4rem;
                background: #fff;
                border-bottom: .01rem solid #efefef;
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                box-sizing: border-box;
                .agin
                    border-left: 1px solid #ccc;
                    float right
                    font-size: .2rem;
                    padding-left: .16rem;
                .username
                    float left
                    padding: 0 .3rem 0 0;
                    font-size: .3rem;
                    line-height: normal;
                    border-radius: 0;
                    border: 0;
            .loginbtn
                margin-top .8rem
                width: 100%;
                height: .8rem;
                line-height: .8rem;
                display: block;
                background-color: #efefef;
                border-radius: .25rem;
                font-size: .36rem;
                color: #fff;
                background-image: linear-gradient(90deg,#fab3b3,#ffbcb3 73%,#ffcaba);
                box-shadow: 0 0.1rem 0.2rem 0 rgba(255,62,62,.2);
                text-align: center;
                font-family: PingFangSC-Semibold;
            .registration
                margin-top: .2rem;
                text-align: center;
                .registerbtn
                    width: 100%;
                    height: .8rem;
                    line-height: .8rem;
                    display: block;
                    border-radius: .25rem;
                    box-sizing: border-box;
                    border: 1px solid #ff2000;
                    color: #f10000;
                    background: #fff;
                    margin-top: .1rem;
            .logintype
                margin-top: .88rem;
                .quick-login
                    height: .8rem;
                    position: relative;
                    padding: .5rem 0 0;
                    border-top: 1px solid #efefef;
                    text-align: center;
                    .txt-otherLogin
                        font-size: .3rem;
                        font-weight: 400;
                        position: absolute;
                        top: -.14rem;
                        left: 50%;
                        background-color: #fff;
                        padding: .05rem .15rem;
                        color: #ccc;
                        -webkit-transform: translateX(-50%);
                        transform: translateX(-50%);
                        .icon
                            position: relative;
                            width: .48rem;
                            height: .48rem;
                            color: #616161;
                            margin: 0 .15rem;
                            font-size: .14rem;
            .agreement-tips
                margin-top: .12rem;
                text-align: center;
                font-size: .3rem;
                color: #bebebe;
</style>
