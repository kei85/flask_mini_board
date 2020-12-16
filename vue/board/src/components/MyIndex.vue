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
          <tr v-for="board in brds" :key="board.id">
            <td>{{ board.name }}</td>
            <td>{{ board.message }}</td>
            <td>{{ board.created_at }}</td>
          </tr>
        </tbody>
      </table>
      <input type="button" value="prev" @click="decrement">
      <input type="button" value="next" @click="increment">
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyIndex',
  methods: {
    increment() {
      this.page += 1;
    },
    decrement() {
      this.page -= 1;
    },
    get_boards: async function(pg) {
      await this.$axios.get('/api/boards/index')//this.$store.state.login_user.user.id)
      .then(res => {
        this.tmp = res.data.boards;
        if (res.data.length < 11) {
          this.brds = res.data.boards;
        } else {
          this.brds = this.tmp.slice(pg * 10, (pg + 1) * 10);
          console.log(pg);
        }
      })
      .catch(err => {
        alert(err);
      })
    }
  },
  data() {
    return {
      tmp: 0,
      brds: 0,
      page: 0
    }
  },
  beforeMount() {
    this.get_boards(this.page);
  },
  watch: {
    page: function(pg) {
      this.brds = this.tmp.slice(pg * 10, (pg + 1) * 10);
    }
  }
}
</script>