<template>
 <h4 class="m-5">Welcome to Snail</h4>
    <section class="vh-80">
  <div class="container py-2 h-70">
    <div class="row d-flex align-items-center justify-content-center h-100">
      <div class="col-md-8 col-lg-7 col-xl-6">
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg" class="img-fluid" alt="Phone image">
      </div>
      <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
      <h2 class='m-3'>Please Sign in</h2>
        <form>
          <!-- Email input -->
          <div class="form-outline mb-4">
            <input type="text" id="form1Example13" class="form-control form-control-lg" placeholder="Username" v-model="this.username"/>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input type="password" id="form1Example23" class="form-control form-control-lg" placeholder="Password" v-model="this.password"/>
          </div>
          <!-- Submit button -->
          <button type="submit" class="btn btn-primary btn-lg btn-block" @click="authenticate">Sign in</button>
        </form>
      </div>
    </div>
  </div>
</section>
</template>

<script>

import axios from "axios";
export default {

  name: "Login",
  data(){
      return {
          username: "",
          password: "",
          isLoading: false,
      }
  },
  created(){
        if (sessionStorage.getItem('username') !== null && sessionStorage.getItem('password') !== null) {
        const payload = {
            username: sessionStorage.getItem('username'),
            password: sessionStorage.getItem('password')
        }            
            axios.post(`http://localhost:8000/login/`, payload)
            .then(response => {
                if(response.status == 200) {
                    this.$store.state.authenticated = true
                    this.$router.push({ name: "Home" })
                }
            })
        }  
    },
  methods : {    
        authenticate(){

                sessionStorage.setItem("username", this.username)
                sessionStorage.setItem("password", this.password)
                
                const url = this.$store.state.baseUrl

                if (this.username !== ""  && this.password !== ""){
                    this.isLoading =  true;

                    const payload = {
                        username: this.username,
                        password: this.password
                    } 
                    axios.post(`${url}/login/`, payload)
                    .then(response =>{
                    if (response.status == 200){
                            this.$router.push({ name: "Home" })
                            this.$store.state.authenticated = true
                            sessionStorage.setItem("username", this.username)
                            sessionStorage.setItem("password", this.username)
                    }
                    })
                }    
            },
  },

};
</script>

<style scoped>
.container{
    background-color: rgb(254,254,255);
}
</style>