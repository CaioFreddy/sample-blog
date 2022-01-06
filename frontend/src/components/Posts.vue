<template>
    <div>
        <div v-for="post in posts"  :key="post.postname">
            <b-card :title="post.title"> 
                <b-card-text>
                    {{ post.content }}
                </b-card-text>
                <b-card-footer>
                    Postado em: {{ post.created_at }}
                </b-card-footer>
            </b-card>
        </div>
    </div>
</template>
<script>
import axios from "axios";

const endpoint = "http://localhost:8000/";

export default {
  data() {
    return {
      posts: [
        { title: "titulo", content: "teste de content", created_at:"2021-01-06 03:28:55", uid:"sdkgjdskgd-fdhsd-hdhdh5-fd" },
        { title: "titulo 2", content: "teste de content2", created_at:"2021-01-06 01:04:41", uid:"sdkgjdskgd-fdhsd-hdhdh5-fd" },
        { title: "titulo 3", content: "teste de content3", created_at:"2021-01-06 00:42:32", uid:"sdkgjdskgd-fdhsd-hdhdh5-fd" },
        { title: "titulo 4", content: "teste de content4", created_at:"2021-01-05 023:18:25", uid:"sdkgjdskgd-fdhsd-hdhdh5-fd" },
     
      ],
    };
  },
  created() {
    axios.get(endpoint + "api/posts/").then((response) => {
      this.posts = response.data.data;
    });
  },
};
</script>