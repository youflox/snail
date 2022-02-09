<template>
  <div>
  </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'Logout',
    data(){
        return {
        }
    },
    methods: {
        logout(){
            console.log(`${this.$store.state.baseUrl}`)
            axios.get(`${this.$store.state.baseUrl}/logout/`)
        }
    },
    created() {
        this.logout()
        this.$store.state.authenticated = false
        sessionStorage.removeItem('username')
        sessionStorage.removeItem('password')
        this.$router.push({ name: "Login" })
    },
}

</script>

<style>
.divider:after,
.divider:before {
  content: "";
  flex: 1;
  height: 1px;
  background: #eee;
}
</style>