<template>
  <div id="nav">
    <router-link v-if="this.$store.state.authenticated" to="/">Home</router-link> 
    <router-link to="/about">About</router-link> 
    <router-link v-if="!this.$store.state.authenticated" to="/Login">Login</router-link> 
    <router-link v-if="!this.$store.state.authenticated" to="/signup">Signup</router-link>
    <router-link v-if="this.$store.state.authenticated" to="/Logout">Logout</router-link>
  </div>
  <router-view />
</template>


<script>
export default {
  data(){
    return {
      name: false,    
    }
  },
  methods: {
    checkAuthenticated(){
      if (sessionStorage.getItem('username') == null  && sessionStorage.getItem('password') == null){
        return false;
      }
      else{
        return true;
      }
    }
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
  background-color: rgb(224,189,115);

}

#nav a {
  font-weight: bold;
  color: #2c3e50;
  padding: 20px;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
