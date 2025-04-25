<template>
  <div id="login_box">
    <form @submit.prevent="get_auth">
      <div class="mb-3">
        <label for="exampleInputEmail1" class="form-label">Email address</label>
        <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
      </div>
      <div class="mb-3">
        <label for="exampleInputPassword1" class="form-label">Password</label>
        <input v-model="password" type="password" class="form-control" id="exampleInputPassword1">
      </div>
      <div class="mb-3 form-check">
        <input type="checkbox" class="form-check-input" id="exampleCheck1">
      </div>
      
      <button  class="btn primary"><router-link :to="{ path: '/signup' }">SIGN UP</router-link></button>
      <button type="submit" class="btn btn-warning">Submit</button>
    </form>
  </div>

</template>

<script>
import { mapActions } from 'vuex';
export default {
  data() {
    return {
      email: "",
      password: ""

    }
  },
  methods: {
    ...mapActions(['getinfo']),
    get_auth() {
      const payload = {
        email: this.email,
        password: this.password
      };
      this.getinfo(payload)
      const redirect = this.$route.query.redirect || '/';
      this.$router.push(redirect)
    }
  }
}
</script>
<style>
#login_box{
  margin-top: 5rem;
}
</style>