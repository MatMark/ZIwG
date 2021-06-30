<template>
  <div>
    <v-row v-if="product" align="center" class="pa-3">
      <v-col cols="2" class="pa-2">
        <router-link :to="`/product_details/${product.id}`">
          <v-img
            v-if="product.photos"
            :src="`${baseUrl}/${product.photos[0].url}`"
            width="50"
            height="50"
            :alt="`/product_details/${product.id}`"
          />
          <v-img
            v-else
            :src="require('@/assets/cookie.png')"
            contain
            width="50"
            height="50"
            :alt="`/product_details/${product.id}`"
          />
        </router-link>
      </v-col>
      <v-col cols="6" class="pa-1">
        <router-link
          :to="`/product_details/${product.id}`"
          style="text-decoration: none; color: black"
        >
          <span
            >{{ order.amount }} x
            <template v-if="this.$i18n.locale === 'pl'"
              ><em>{{ product.name_pl }}</em></template
            >
            <template v-else
              ><em>{{ product.name_en }}</em></template
            ></span
          >
        </router-link>
      </v-col>
      <v-col cols="3" class="caption pa-1">
        <span class="title">{{ order.sumPrice.toFixed(2) }} zł</span>
        <div>{{ $t("cart.pricePerItem") }} {{ order.price.toFixed(2) }} zł</div>
      </v-col>
      <v-col cols="1" justify="space-between" class="pa-0">
        <v-btn icon small @click="removeProductFromCart()">
          <v-icon small> mdi-delete </v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </div>
</template>
<style scoped>
.centered-input >>> input {
  text-align: center;
}
</style>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapGetters, mapActions } = createNamespacedHelpers("cart");

export default {
  components: {},
  props: {
    order: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      baseUrl: process.env.VUE_APP_DOMAIN,
      product: null
    };
  },
  computed: {
    ...mapGetters(["getAmountByOrderId"]),

    getByOrderId: {
      get: function() {
        return this.getAmountByOrderId(this.order.order_id);
      }
    }
  },
  mounted() {
    this.$axios
      .get(
        `${process.env.VUE_APP_DOMAIN}/backend/product/${this.order.product_id}/`
      )
      .then(response => (this.product = response.data));
  },
  methods: {
    ...mapActions(["removeProduct"]),

    removeProductFromCart() {
      const openOrderEdit =
        window.location.pathname === `/orderEdit/${this.order.order_id}`;
      if (openOrderEdit) this.$router.replace("/home");
      this.removeProduct(this.order.order_id);
    }
  }
};
</script>
