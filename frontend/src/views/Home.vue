<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <HomePageCarousel />
        <v-card>
          <v-card-title>
            {{ $t("home.recomendations") }}
          </v-card-title>
          <v-container>
            <v-row v-if="products.length !== 0" align="center" justify="center">
              <v-col
                v-for="product in products"
                :key="product.id"
                xs="12"
                sm="6"
                md="3"
                lg="2"
                xl="2"
              >
                <v-row align="center" justify="center">
                  <ProductCard :product="product" />
                </v-row>
              </v-col>
            </v-row>
            <v-row v-else>
              <v-col
                v-for="(item, i) in 3"
                :key="i"
                xs="12"
                sm="6"
                md="3"
                lg="2"
                xl="2"
              >
                <v-row align="center" justify="center">
                  <v-skeleton-loader
                    class="mx-auto"
                    width="300"
                    height="425"
                    type="card"
                  />
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import HomePageCarousel from "@/components/HomePageCarousel.vue";
import ProductCard from "@/components/ProductCard.vue";
export default {
  name: "Home",
  components: {
    HomePageCarousel,
    ProductCard
  },
  data() {
    return {
      products: []
    };
  },
  mounted() {
    this.$axios
      // .get(`${window.location.origin}/backend/products/?recommend=True`)
      .get("http://127.0.0.1:8000/backend/products/?recommend=True")
      .then(response => (this.products = response.data));
  }
};
</script>
