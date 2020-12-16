<template>
  <h1>
    <router-link :to="{name: 'home'}">{{header_msg}}</router-link>
  </h1>
</template>
<script lang="ts">

export default {
  data() {
    return {
      header_msg: 'Board'
    }
  },
  beforMount() {
    this.header_msg = this.$route.params.header;
    console.log(this.$route.params.header);
  }
}
</script>