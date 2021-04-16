<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Articles</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.article-modal>
          Add Article
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(article, index) in articles" :key="index">
              <td>{{ article.name }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-primary btn-sm">
                    <router-link
                      class="btn btn-primary btn-sm"
                      :to="`/${article.id}`"
                    >Read</router-link>
                  </button>
                  <button
                    type="button"
                    class="btn btn-warning btn-sm">
                    <router-link
                      class="btn btn-warning btn-sm"
                      :to="`edit/${article.id}`"
                    >Update</router-link>
                  </button>
                  <!-- <button
                    type="button"
                    class="btn btn-warning btn-sm"
                    v-b-modal.article-update-modal
                    @click="editArticle(article)">
                    Update
                  </button> -->
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <!-- Add Modal Form -->
    <b-modal ref="addArticleModal"
      id="article-modal"
      title="Add a new article"
      hide-footer>
      <b-form @submit="onSubmitAdd" @reset="onResetAdd" class="w-100">
        <b-form-group id="form-name-group"
          label="Name:"
          label-for="form-name-input">
          <b-form-input id="form-name-input"
            type="text"
            v-model="addArticleForm.name"
            required
            placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-content-group"
          label="Content:"
          label-for="form-content-input">
          <b-form-input id="form-content-input"
            type="text"
            v-model="addArticleForm.content"
            required
            placeholder="Enter content">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <!-- Update Modal Form -->
    <b-modal ref="editArticleModal"
      id="article-update-modal"
      title="Update the article"
      hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
          label="Name:"
          label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
            type="text"
            v-model="editArticleForm.name"
            disabled
            placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-content-edit-group"
          label="Content:"
          label-for="form-content-edit-input">
          <b-form-input id="form-content-edit-input"
            type="text"
            v-model="editArticleForm.content"
            required
            placeholder="Enter content">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      articles: [],
      addArticleForm: {
        name: '',
        content: '',
      },
      message: '',
      showMessage: false,
      editArticleForm: {
        id: '',
        name: '',
        content: '',
      },
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    // Fetch all articles to the page
    getArticles() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.articles = res.data.articles;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    // Add new article
    addArticle(payload) {
      const path = 'http://localhost:5000/';
      axios.post(path, payload)
        .then(() => {
          this.getArticles();
          this.message = 'Article added!!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getArticles();
        });
    },
    // Initialize the add form
    initForm() {
      this.addArticleForm.name = '';
      this.addArticleForm.content = '';
      this.editArticleForm.id = '';
      this.editArticleForm.name = '';
      this.editArticleForm.content = '';
    },
    // Submit the add modal form to the server
    onSubmitAdd(event) {
      event.preventDefault();
      this.$refs.addArticleModal.hide();
      const payload = {
        name: this.addArticleForm.name,
        content: this.addArticleForm.content,
      };
      this.addArticle(payload);
      this.initForm();
    },
    // Reset the add modal form
    onResetAdd(event) {
      event.preventDefault();
      this.$refs.addArticleModal.hide();
      this.initForm();
    },
    // Update the article
    updateArticle(payload, articleId) {
      const path = `http://localhost:5000/edit/${articleId}`;
      axios.put(path, payload)
        .then(() => {
          this.getArticles();
          this.message = 'Article updated!!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getArticles();
        });
    },
    // Fill edit form with the values
    editArticle(article) {
      this.editArticleForm = article;
      this.showMessage = false;
    },
    // Submit the update modal form to the server
    onSubmitUpdate(event) {
      event.preventDefault();
      this.$refs.editArticleModal.hide();
      const payload = {
        name: this.editArticleForm.name,
        content: this.editArticleForm.content,
      };
      this.updateArticle(payload, this.editArticleForm.id);
    },
    // Reset the update modal form
    onResetUpdate(event) {
      event.preventDefault();
      this.$refs.editArticleModal.hide();
      this.initForm();
      this.getArticles();
    },
  },
  created() {
    this.getArticles();
  },
};
</script>
