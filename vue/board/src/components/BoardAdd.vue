<template>
  <div>
    <form @submit.prevent="store_board">
      Message: <input type="textarea" v-model="message">
      <input type="submit" value="投稿">
    </form>
  </div>
</template>

<script>
export default {
  name: 'BoardAdd',
  methods: {
    store_board: async function() {
      await this.$axios.post('/api/boards/add/' + this.$store.state.login_user.user.id, {
        message: this.message
      })
      .then(() => {
        this.$router.push({ 
          name: 'myindex',
          params: { id: this.$store.state.login_user.user.id }
        });
      })
      .catch(err => {
        alert(err)
      });
    }
  }
}
</script>