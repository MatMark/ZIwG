<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <v-card>
          <v-col class="pb-0">
            <v-row justify="space-between" align="center" no-gutters>
              <v-card-title class="py-0">
                {{ $t("appMenu.allProducts") }}
              </v-card-title>
              <v-col cols="4">
                <v-autocomplete
                  style="max-width: 200px; margin-left: auto; margin-right: 5%"
                  v-model="search"
                  :items="products"
                  :item-text="`name_${this.$i18n.locale}`"
                  :item-value="`name_${this.$i18n.locale}`"
                  :label="`${$t('productsPage.search')}`"
                  prepend-icon="mdi-magnify"
                  clearable
                ></v-autocomplete>
              </v-col>
            </v-row>
          </v-col>
          <v-container>
            <v-row v-if="products" align="center" justify="center">
              <v-col v-if="products.length === 0">
                {{ $t("productsPage.noProducts") }}
              </v-col>
              <v-col
                v-for="product in filteredList"
                v-else
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
                v-for="(item, i) in 6"
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
                    width="150"
                    height="400"
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
import ProductCard from "@/components/ProductCard.vue";

export default {
  components: {
    ProductCard
  },
  data() {
    return {
      products: [],
      search: null
    };
  },
  computed: {
    filteredList() {
      if (this.search === null) return this.products;
      return this.products.filter(item => {
        return (
          item[`name_${this.$i18n.locale}`]
            .toLowerCase()
            .indexOf(this.search.toLowerCase()) > -1
        );
      });
    }
  },
  mounted() {
    this.$axios
      .get(`${process.env.VUE_APP_DOMAIN}/backend/products/`)
      .then(response => (this.products = response.data));
  }
};
</script>
