<template>
  <div>
    <div v-for="post in posts" :key="post.postname">
      <b-card :title="post.title">
        <b-card-text>
          {{ post.content }}
        </b-card-text>
        <b-card-footer> Postado em: {{ post.created_at }} </b-card-footer>
      </b-card>
    </div>
  </div>
</template>
<script>
import axios from "axios";

const endpoint = process.env.VUE_APP_BACKEND;

export default {
  data() {
    return {
      posts: [],
    };
  },
  created() {
    axios.get(endpoint + "/posts").then((response) => {
      this.posts = response.data;
    });
  },
};
</script>