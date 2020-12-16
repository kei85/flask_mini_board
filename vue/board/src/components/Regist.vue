<template>
  <div>
    <form @submit.prevent="regist">
      Name: <input type="text" v-model="name">
      Mail: <input type="text" v-model="mail">
      Password: <input type="password" v-model="pass">
      Age: <input type="number" min="0" max="150" v-model="age">
      <input type="submit" value="登録">
    </form>
  </div>
</template>

<script>
export default {
  name: 'Regist',
  methods: {
    regist: async function() {
      await this.$axios.post('/api/users/add', {
        name: this.name,
        mail: this.mail,
        pwd: this.pass,
        age: this.age
      })
      .then(() => {
        this.$router.push({name: 'login', params: {ok: '登録が完了しました'}});
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>