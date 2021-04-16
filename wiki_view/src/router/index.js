import Vue from 'vue';
import VueRouter from 'vue-router';
import Articles from '../components/Articles.vue';
import ReadArticle from '../components/Read_Article.vue';
import UpdateArticle from '../components/Update_Article.vue';

Vue.use(VueRouter);

export default new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Articles',
      component: Articles,
    },
    {
      path: '/edit/:id',
      name: 'Update',
      component: UpdateArticle,
    },
    {
      path: '/:id',
      name: 'Read',
      component: ReadArticle,
    },
  ],
});
