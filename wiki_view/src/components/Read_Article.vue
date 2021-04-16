<template>
    <div class="container">
        <alert :message=message v-if="showMessage"></alert>
        <table class="table table-hover" v-if="!showMessage">
            <thead>
                <tr>
                    <th scope="col">{{ article.name }}</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>
                        <b-form-textarea
                            id="textarea-plaintext"
                            plaintext
                            :value="article.content">
                        </b-form-textarea>
                    </td>
                </tr>
                <tr>
                    <td>
                        <button
                            type="button"
                            class="btn btn-warning btn-sm">
                            <router-link
                            class="btn btn-warning btn-sm"
                            :to="`edit/${article.id}`">Update</router-link>
                  </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Read',
  data() {
    return {
      article: {},
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    // Fetch all articles to the page
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
  },
  created() {
    this.getArticle(this.$route.params.id);
  },
};
</script>
