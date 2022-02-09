    <br>
<template>
  <div class="about container">
    <h4>Hello <a class="bg-light text-text-success">{{username}}</a> welcome to Snail.</h4>
    <br>
    <p>Please login to go to the Home page where you can upload the file to the server and then transfer the data to a databse.</p>
    <br>
    <p>Once logged in then you can click on the browse to select a 'JSON' format file and upload it to the server.</p>
    <br>
    <p>The file is present in the server but the data is not yet uploaded to the database.</p>
    <br>
    <p>to update the file data to the databse click on <a class="text-danger">upload</a>, the data will be saved to the databse.</p>
    <br>
    <p>To view the data of the file, click on the <a class="text-success">view</a> button.</p>
    <br>
    <p> username : admin</p>
    <p> password : admin</p>
  
  </div>
</template>
<script>
export default {
  name: 'About',
  data(){
    return{
      username: sessionStorage.getItem('username'),
    }
  },
}
</script>
