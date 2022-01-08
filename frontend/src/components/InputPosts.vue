<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <b-form-group label="Post Something:">
        <b-form-input
          v-model="form.title"
          type="text"
          placeholder="Enter title"
          required
        />
        <b-form-input
          v-model="form.content"
          type="text"
          placeholder="Enter content"
          required
        />
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
import axios from "axios";

const endpoint = process.env.VUE_APP_BACKEND;

export default {
  data() {
    return {
      form: {
        host: process.env.VUE_APP_BACKEND,
        env: process.env,
        title: "",
        content: "",
      },
      show: true,
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      const postData = this.form;
      axios.post(endpoint + "/posts", postData);
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.title = "";
      this.form.content = "";
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
