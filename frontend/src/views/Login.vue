<template>
  <div class="cards content uk-margin uk-margin-small-right uk-width-1-2">
    <div class="card card--lg">
      <div class="card__inner">
        <div class="card__heading" style="align-items: center">
          <h2 style="margin-top: 20px !important">SNAIL</h2>
          {{username}}
          {{password}}
          <h2 style="margin-top: 20px !important">Please Sign In</h2>

          <form class="login form" ref="formContainer">
            <div class="field">
              <label for="id_username" class="uk-form-label uk-inline"
                >Username</label
              >
              <input
                v-model="this.username"
                type="text"
                placeholder="Username"
                maxlength="150"
                id="paswword"
                class="uk-input"
              />
            </div>

             <div class="field">
              <label for="id_username" class="uk-form-label uk-inline"
                >Password</label
              >
              <input
                v-model="this.password"
                type="text"
                placeholder="Password"
                maxlength="150"
                id="password"
                class="uk-input"
              />
            </div>
            <button @click="authenticate">Sign in</button>
          </form>
        </div>
      </div>
    </div>
  </div>
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