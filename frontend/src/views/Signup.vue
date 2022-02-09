<template>

 <h4 class="m-5">Sign up to Snail</h4>
    <section class="vh-70">
  <div class="container py-2 h-70">
    <div class="row d-flex align-items-center justify-content-center h-100">
      <div class="col-md-8 col-lg-7 col-xl-6">
        <img src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.svg" class="img-fluid" alt="Phone image">
      </div>
      <div class="col-md-7 col-lg-5 col-xl-5 offset-xl-1">
        <form>
          <!-- Username input -->
          <div class="form-outline mb-4">
            <input type="text" id="form1Example13" class="form-control form-control-lg" placeholder="Username" v-model="this.username"/>
          </div>

          <!-- Email input -->
          <div class="form-outline mb-4">
            <input type="email" id="form1Example13" class="form-control form-control-lg" placeholder="Email address" v-model="this.email"/>
          </div>

            <!-- First Name input -->
          <div class="form-outline mb-4">
            <input type="text" id="form1Example13" class="form-control form-control-lg" placeholder="First name" v-model="this.firstName"/>
          </div>

            <!-- Last Name input -->
          <div class="form-outline mb-4">
            <input type="text" id="form1Example13" class="form-control form-control-lg" placeholder="Last name" v-model="this.lastName"/>
          </div>

          <!-- Password input -->
          <div class="form-outline mb-4">
            <input type="password" id="form1Example23" class="form-control form-control-lg" placeholder="Password" v-model="this.password"/>
          </div>
          <!-- Submit button -->
          <button type="submit" class="btn btn-primary btn-lg btn-block" @click="signUp">Sign in</button>
        </form>
      </div>
    </div>
  </div>
</section>
</template>

<script>
import axios from "axios";

export default {
    name: 'Signup',
    data(){
        return {
            username: "",
            email: "",
            firstName: "",
            lastName:"",
            password:"",
        }
    },
    methods: {
        signUp(){
            
            const payload = {
                "username":this.username,
                "email":this.email,
                "first_name":this.firstName,
                "last_name": this.lastName,
                "password": this.password,
            }

            if (this.validatedData){
                
                axios.post(`${this.$store.state.baseUrl}/signup/`, payload)
                    .then(res => {
                        console.log(res)
                    })
            }
                    this.$router.push({ name: "Login" })

        },
        validatedData(){
            if(this.username !=="" &&  this.email !== "" && this.firstName !== "", 
                this.lastName !== "", this.password !== ""){
                return false
            } else {
                return true
            }
        }
    },  
}
</script>
