<template>
  <div class="all-lc">
    <div class="container-dir">
        <div class="law-title">
            <div class="dir-title" style="font-size: 20px;font-weight: bold;padding-bottom: 30px;">基本信息</div>
            <div class="dir-title">效力级别：法律</div>
            <div class="dir-title">发布日期：2017-11-04</div>
            <div class="dir-title">实施日期：2017-11-04</div>
            <div class="dir-title">发布部门：全国人民代表大会</div>
        </div>
        <div>
            <div>目录</div>
            <div class="law-dir">
                <div v-for=""></div>
            </div>
        </div>
    </div>
 
    <div class="container-content">
        <ContentView/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ContentView from './ContentView.vue';
import { requestUrl } from '@/globalVar';

export default{
    component: {
        ContentView
    },
    methods:{
        getDir(){
            
        }
    },
    data(){
        return{
            pageMax:400
        }
    }
}

</script>

<style>
html {
    overflow-x:hidden;
    overflow-y:scroll;
}
.all-lc{
    display: flex;
    flex-direction: row;
    background-color: bisque;
    width: 100%;
    gap: 50px;
    /* background-color:grey; */
}
.container-dir{
    width: 30%;
    display: flex;
    flex-direction: column;   
    gap: 100px;
}
.law-title{
    background-color: white;
    padding-top: 50px;
}
.dir-title{
    padding-left: 30px;
    padding-bottom: 20px;
}
.container-room{
    width: 100px;
    background-color: aqua;
    display: flexbox;
}
.container-content{
    flex: 0 0 auto; 
    box-sizing: content-box;
    display: flex;
    width: 60%;
    background-color: white;
}

.law-dir {
  overflow-y: scroll;
  border: 1px solid black;
  height: 600px;
  background-color: white;
}

/* 定制滚动条样式 */
.law-dir::-webkit-scrollbar {
  width: 12px; /* 设置滚动条宽度 */
}
.law-dir::-webkit-scrollbar-thumb{
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
    border-radius: 10px;
    transition: 0.3s ease-in-out;
}
.law-dir::-webkit-scrollbar-track{
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
    background-color: #F5F5F5;
}
</style>
