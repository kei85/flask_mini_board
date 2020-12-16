<template>
  <div>
    Home!<br>
    <router-link :to="{name: 'login', params: {header: 'User/Login'}}">LoginPage</router-link><br>
    <router-link :to="{name: 'regist', params: {header: 'User/Regist'}}">RegistPage</router-link>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>