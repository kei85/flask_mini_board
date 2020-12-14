<template>
  <div>
    <div>
      <h4>welcome, {{ $store.state.login_user.user.name }}!</h4>
      <router-link :to="{
        name: 'add',
        params: {id: $store.state.login_user.user.id}
      }">
        <input type="button" value="投稿フォーム">
      </router-link>
      <table>
        <tbody>
          <tr v-for="board in brds.boards" :key="board.id">
            <td>{{ board.name }}</td>
            <td>{{ board.message }}</td>
            <td>{{ board.created_at }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyIndex',
  methods: {
    get_boards: async function() {
      await this.$axios.get('/api/boards/index')//this.$store.state.login_user.user.id)
      .then(res => {
        console.log(res.data)
        this.brds = res.data;
      })
      .catch(err => {
        alert(err);
      })
    }
  },
  data() {
    return {
      brds: 0
    }
  },
  beforeMount() {
    this.get_boards();
  }
}
</script>