<template>
  <div>
    <p>
      mail: <input type="text" v-model="mail">
    </p>
    <p>
      password: <input type="password" v-model="password">
    </p>
    <input type="button" @click="post_user" value="ログイン">
  </div>
</template>
<script>
export default {
  name: 'Login'
}
</script>