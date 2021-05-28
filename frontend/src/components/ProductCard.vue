<template>
  <div style="height: 420px">
    <v-card :id="product.id" v-if="product" width="170" tile>
      <router-link class="pa-1" :to="`/product_details/${product.id}`">
        <v-img
          v-if="product.photo"
          :src="`${baseUrl}/${product.photo}`"
          contain
          width="150"
          height="160"
          class="ma-auto"
          :alt="'product_details/' + product.id"
        />
        <v-img
          v-else
          :src="require('@/assets/logo.png')"
          contain
          width="150"
          height="160"
          class="ma-auto"
          :alt="'product_details/' + product.id"
        />
      </router-link>

      <v-card-text class="pa-2">
        <v-container class="py-2">
          <v-row>
            <v-card style="height: 100px" class="caption text-left" flat>
              {{ $t("productCard.code") }}: <em>{{ product.code }}</em>
              <br />
              {{ $t("productCard.name") }}: ><em>{{
                `product.name_${this.$i18n.locale}`
              }}</em>
              >
            </v-card>
          </v-row>
        </v-container>
      </v-card-text>
      <v-card-actions class="pt-0 mt-4">
        <v-container class="py-0">
          <v-row class="subtitle-2 text-right" justify="end" align="center">
            {{ $t("productCard.price") }}: {{ product.price.toFixed(2) }} zł
          </v-row>
          <v-row justify="center" align="center">
            <v-btn
              x-small
              color="blue lighten-5"
              elevation="4"
              class="overline pa-4 mt-4 mb-4"
              @click="addToCart"
            >
              <v-icon small left> mdi-cart-outline </v-icon>
              {{ $t("productCard.addToCart") }}
            </v-btn>
          </v-row>
        </v-container>
      </v-card-actions>
    </v-card>
  </div>
</template>
<style scoped>
.centered-input >>> input {
  text-align: center;
}
</style>
<script>
export default {
  props: {
    product: {
      type: Object,
      default: undefined
    }
  },
  data() {
    return {
      baseUrl: process.env.VUE_APP_DOMAIN
    };
  },
  methods: {
    addToCart() {
      this.$router.push(`/product_details/${this.product.id}`);
    }
  }
};
</script>
