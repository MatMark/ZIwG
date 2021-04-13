import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import ProductDetails from "@/views/ProductDetails.vue";
import AllProducts from "@/views/AllProducts.vue";
import PageNotFound from "@/views/PageNotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    alias: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/product_details/:id",
    name: "ProductDetails",
    component: ProductDetails
  },
  {
    path: "/all_products",
    name: "AllProducts",
    component: AllProducts
  },
  {
    path: "/*",
    name: "PageNotFound",
    component: PageNotFound
  }
  // {
  //   path: "/about",
  //   name: "About",
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () =>
  //     import(/* webpackChunkName: "about" */ "../views/About.vue")
  // }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
