<template>
  <div>
    <div>{{ err_msg }}</div>
    <form @submit.prevent="save_store">
      mail: <input type="text" v-model="mail">
      password: <input type="password" v-model="password">
      <input type="submit" value="ログイン">
    </form>
    <p>{{ this.$route.params.ok }}</p>
  </div>
</template>
<script>
export default {
  data() {
    return {
      err_msg: ''
    }
  },
  name: 'Login',
  methods: {
    post_user: async function() {
      let data;
      await this.$axios.post('api/users/login', {
        mail: this.mail,
        pwd: this.password
      })
      .then(res => {
        data = res.data
        if(res.data.state) {
          return data
        } else {
          data = 0;
          return data;
        }
      })
      .catch(err => {
        if(err.response){
          console.log(err)
        }
      });
      return data;
    },
    save_store: async function() {
      let data = await this.post_user()
      if (data == 0) {
        this.err_msg = 'user not found!';
        return 0;
      }

      await this.$store.commit('change_user', data)
      this.$router.push({ name: 'myindex', params: { id: data.user.id} })
    }
  }
}
</script>