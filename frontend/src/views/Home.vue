<template>
  <div class="home">
    <div class="container">
      <div class="row">
    <h2 class="mt-3">Welcome <a class="bg-light text-text-success">{{username}}</a></h2>
    
        <div id="filename" class="col  mt-3 mb-5">
         
         
          <input 
            class="btn btn-warning m-3"
            @change="handleFileUpload($event)"
            type="file"
            id="myFile"
            name="filename"
            accept = ".json"
          >
          <button 
          class="btn" 
          :class="{'btn-success': active, 'btn-secondary': !active, 'disabled': !active }"
          @click="fileUpload()" 
          type="submit">
            upload
          </button>
        </div>
      </div>
      <div class="box">
        <div v-for="file in files" :key="file.id" id="file" class="m-3">
          <img
            src="http://cdn.onlinewebfonts.com/svg/img_442842.png"
            alt="{{file.file}}"
            style="width: 100px; height: 120px"
          />
          <p id="fileName">{{ file.file.split("/")[3] }}</p>
          <button
            v-if="!file.data_uploaded"
            @click="upload(file.id)"
            class="btn btn-danger"
            :class="{disabled: clickedId.includes(file.id)}"
          >
            Upload
          </button>
          <button
            v-if="file.data_uploaded"
            @click="view(file.id)"
            class="btn btn-success"
          >
            View
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import { ClientTable } from 'vue-tables-2';

export default {
  name: "Home",
  data() {
    return {
      clickedId: [],
      active: false,
      fileData: null,
      files: {},
      newFile: null,
      username: sessionStorage.getItem("username"),
      password: sessionStorage.getItem("password"),
    };
  },
  async created() {
    console.log(sessionStorage.getItem("username"), sessionStorage.getItem("password"))
    if (this.username, this.password, this.$store.state.authenticated) {
      await this.getData();
    } else {
      this.$router.push({path: '/login'})
    }
  },
  methods: {
    getData() {
      axios
        .get(`http://localhost:8000/file/upload/`, {
          auth: {
            username: this.username,
            password: this.password,
          },
        })
        .then((response) => {
          console.log(response.data);
          this.files = response.data;
        });
    },
    upload(e) {
      this.clickedId.push(e)
      axios
        .post(
          "http://localhost:8000/data/upload/",
          { file_id: e },
          { auth: { username: this.username, password: this.password } }
        )
        .then((res) => {
          if (res.status === 201) {
            this.getData();
          }
        });
    },

    view(id) {
      this.$router.push({ name: "DataView", params: { id: id } });
    },
    handleFileUpload(event) {
      this.file = event.target.files[0];
      this.active = true;
    },
    fileUpload() {
      if (this.file) {
        const payload = {
          file: this.file,
        };

        let formData = new FormData();
        for (const attr in payload) {
          formData.append(attr, payload[attr]);
        }
        axios
          .post("http://localhost:8000/file/upload/", formData, {
            auth: { username: this.username, password: this.password },
          })
          .then((res) => {
            this.getData();
            console.log(res);
          });
      }
      this.active = false;
    },
  },
};
</script>

<style scoped>
.box {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
}

.active{
  text: green;
  disabled: true;
}
</style>
