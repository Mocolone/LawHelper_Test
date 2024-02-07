<template>
<div></div>
</template>
<script>
import { requestUrl } from '@/globalVar';
import axios from 'axios';

export default {
    props: {
    url: {
      type: String,
      required: true,
    },
    requestParam: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      formattedTextBlocks: [],
      url:"",
      requestParam:{
        Ty
      }
    };
  },
  mounted() {
    // 发送GET请求
    axios.post(requestUrl+this.url,this.requestParam)
      .then(response => {
        // 获取响应的数据
        const responseData = response.data;
        // 格式化显示大段文字
        this.formattedTextBlocks = this.formatText(responseData.body);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  },
  methods: {
    // 自定义方法用于格式化文本
    formatText(text) {
      // 在实际应用中，你可能需要使用更复杂的逻辑来分割文本
      const blockSize = 200; // 假设每个文本块的大小为200个字符

      const textBlocks = [];
      for (let i = 0; i < text.length; i += blockSize) {
        textBlocks.push(text.slice(i, i + blockSize));
      }

      return textBlocks;
    },
  },
};
</script>
<style></style>