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
  }
}
</script>