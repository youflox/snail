<template>
  <div class="home">
    <div id="filename" class="container">
          <input @change="handleFileUpload($event)" type="file" id="myFile" name="filename">
          <input @click="fileUpload()" type="submit">
    </div>    
    <div v-for="file in files" :key="file.id">
      <div id="file" >
        <img src="http://cdn.onlinewebfonts.com/svg/img_442842.png" alt={{file.file}} style="width:100px;height:120px;">
        <p id="fileName">{{file.file.split('/')[3]}}</p>   
        <button v-if="!file.data_uploaded" @click="upload(file.id)" >Upload</button>  
        <button v-if="file.data_uploaded" @click="view(file.id)" >View</button>  
      </div>
    </div>
  </div>

<table class="table table-hover table-bordered .col-md-8">
  <thead>
    <tr>
      <th scope="col">userId</th>
      <th scope="col">Title</th>
      <th scope="col">Body</th>
    </tr>
  </thead>
  <tbody v-for="data in fileData"  v-bind:key="data.id">
    <tr>
      <td>{{data['userId']}}</td>
      <td>{{data['title']}}</td>
      <td>{{data['body']}}</td>
    </tr>

  </tbody>
</table>

</template>

<script>
import axios from 'axios'
// import { ClientTable } from 'vue-tables-2';

export default {
  name: "Home",
  data(){
    return {
      fileData : null,
      files : {},
      newFile : null,
      username: sessionStorage.getItem('username'),
      password: sessionStorage.getItem('password')
    }
  },
  async created() {
    if (this.username, this.password) {
      await this.getData()

    }
  //   if (this.this.$store.state.authenticated){
  //   }
  },
  methods: {
    getData(){
        axios.get(`http://localhost:8000/file/upload/`, {
        auth:{
        "username":this.username,
        "password":this.password
        }
      })
      .then(response =>{
        console.log(response.data)
        this.files = response.data
      })
    },
    upload(e){
        axios.post('http://localhost:8000/data/upload/',{'file_id':e}, {auth: {'username':'admin','password':'admin'}})
          .then(res => {
            if(res.status === 201){
              this.getData();
            }
            })
    },

    view(id){
      axios.get(`http://localhost:8000/data/upload/${id}`, {
        auth:{
        "username":this.username,
        "password":this.password
        }
      })
      .then(response =>{
        console.log(response.data);
        this.fileData = response.data
      })
    },
    handleFileUpload(event){
      this.file = event.target.files[0]
    },
    fileUpload(){
      if (this.file){
          const payload = {
                file: this.file,
            };

        let formData = new FormData();
        for (const attr in payload) {
          formData.append(attr, payload[attr]);
      }
        axios.post('http://localhost:8000/file/upload/',formData, {auth: {'username':this.username,'password':this.password}})
        .then(res => {console.log(res)})
      }
    }
  },

};
</script>

<style scoped>

</style>