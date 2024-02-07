<template>
    <div class="all">
        <div>法条预测</div>
        <div>
            <p>输入案情描述部分（可以输入1000字）</p>
            <textarea rows="20" cols="50" v-model="description"></textarea>
        </div>
    </div>
</template>
<script>
export default {
  data () {
    return {
      description: ''
    }
  }
}
</script>
<style>

.all{
  text-align: center;
}
</style>
