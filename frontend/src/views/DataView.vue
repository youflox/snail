<template>
  <div v-if="fileData" class="dataView m-5">
    <div class="container">
      <table class="table table-hover table-bordered">
        <thead>
          <tr>
            <th scope="col">userId</th>
            <th scope="col">Title</th>
            <th scope="col">Body</th>
          </tr>
        </thead>
        <tbody v-for="data in fileData" v-bind:key="data.id">
          <tr>
            <td>{{ data["userId"] }}</td>
            <td>{{ data["title"] }}</td>
            <td>{{ data["body"] }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "DataView",
  props: {
  	id: {
      type: Number,
      required: true,
  	},
  },
  data() {
    return {
      fileData : null,
    };
  },
  async created() {
    if(this.$store.state.authenticated, sessionStorage.getItem('username'), 
      sessionStorage.getItem('password')) {
        axios.get(`http://localhost:8000/data/upload/${this.id}`, {
          auth:{
          "username":sessionStorage.getItem('username'),
          "password":sessionStorage.getItem('password')
          }
        })
        .then(response =>{
          if (response.status === 200) {
            this.fileData = response.data;
          }
        })
      }
    },
};
</script>
<style>
.{
  background-color: grey;
}
</style>