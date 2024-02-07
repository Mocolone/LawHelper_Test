<template>
  <div>
    <div class="line">功能介绍</div>
    <div class="block-container">
        <Lpfunctioncomponent name="法条预测"/>
        <Lpfunctioncomponent name="法条查询"/>
        <Lpfunctioncomponent name="相似案件筛选"/>
    </div>
  </div>
</template>
<script>
import Lpfunctioncomponent from './Lpfunctioncomponent.vue'
export default{
  components: {
    Lpfunctioncomponent
  }
}
</script>
<style>
.line{
    text-align: center;
    font-size: 20px;
    color: black;
    background-color: white;
    height: 60px;
    font-weight: bold;
}
.block-container{
  text-align: center;
}

</style>
