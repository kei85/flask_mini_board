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
  name: 'Login',
  methods: {
    post_user() {
      this.$axios.post('api/users/login', {
        mail: this.mail,
        pwd: this.password
      })
      .then(res => {
        if(res.data.state) {
          this.$router.push({ name: 'myindex', params: { id: res.data.id, name: res.data.name } })
          return 0
        }
      })
      .catch(err => {
        if(err.response){
          console.log(err)
        }
      });
    }
  }
}
</script>