<template>
  <div class="container">
    <alert :message=message v-if="showMessage"></alert>
    <div v-if="!showMessage">
      <h1>{{ article.name }}</h1>
      <hr>
      <b-form @submit="onSubmit">
        <b-form-input id="form-content-edit-input"
          type="text"
          v-model="article.content"
          required
          placeholder="Enter content">
        </b-form-input>
        <br><br>
        <b-button-group>
          <b-button type="submit" variant="primary">Save</b-button>
          <b-button type="reset" variant="danger">
            <router-link
              class="btn btn-danger btn-sm"
              to="/"
            >Cancel</router-link>
          </b-button>
        </b-button-group>
      </b-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Update',
  data() {
    return {
      article: {},
      showMessage: false,
      message: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getArticle(articleId) {
      const path = `http://localhost:5000/${articleId}`;
      axios.get(path)
        .then((res) => {
          this.article = res.data.article;
          if (Object.entries(this.article).length === 0) {
            this.showMessage = true;
            this.message = 'Article not found';
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.showMessage = true;
          this.message = 'Article not found';
        });
    },
    // Submit the update modal form to the server
    onSubmit(event) {
      event.preventDefault();
      console.log(this.article.content);
      const payload = {
        name: this.article.name,
        content: this.article.content,
      };
      this.updateArticle(payload, this.article.id);
    },
    updateArticle(payload, articleId) {
      const path = `http://localhost:5000/edit/${articleId}`;
      axios.put(path, payload)
        .then(() => {
          this.message = 'Article updated!!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getArticles();
        });
    },
    // Reset the update modal form
    onReset(event) {
      event.preventDefault();
      this.$refs.editArticleModal.hide();
      this.initForm();
      this.getArticles();
    },
  },
  created() {
    this.getArticle(this.$route.params.id);
  },
};
</script>
