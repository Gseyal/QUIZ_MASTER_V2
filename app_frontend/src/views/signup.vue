<template>
    <div id="login_box">
      <form @submit.prevent="get_auth">
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Enter your new Email address</label>
          <input v-model="email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
        </div>
       
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Enter your Username</label>
            <input v-model="username" type="text" class="form-control" >
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Enter your new Password</label>
          <input v-model="password" type="password" class="form-control" id="exampleInputPassword1">
        </div>
        
        <button  class="btn primary"><router-link :to="{ path: '/signup' }">SIGN UP</router-link></button>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  
  </template>
  
  <script>
  import { mapActions } from 'vuex';
  export default {
    data() {
      return {
        email: "",
        password: "",
        username:""
  
      }
    },
    methods: {
      ...mapActions(['sendinfo']),
      get_auth() {
        const payload = {
          email: this.email,
          password: this.password,
          username:this.username
        };
        this.sendinfo(payload)
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