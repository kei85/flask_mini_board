<template>
  <div id="app">
    <div>
      <Header/>
      <router-link to="/users/login">LoginPage</router-link><br>
      <router-link to="/users/regist">RegistPage</router-link>
    </div>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header'

export default {
  components: {
    Header
  }
}
</script>