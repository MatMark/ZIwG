<template>
  <v-menu bottom offset-y open-on-hover :close-on-content-click="false">
    <template v-slot:activator="{ on: menu }">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-badge
            color="indigo lighten-3"
            :content="getCartLength"
            :value="getCartLength"
            overlap
          >
            <v-btn
              class="mx-1"
              small
              icon
              @click="yourCart()"
              v-on="{ ...tooltip, ...menu }"
            >
              <v-icon color="white"> mdi-cart </v-icon>
            </v-btn>
          </v-badge>
        </template>
        <span>{{ $t("appMenu.cart") }}</span>
      </v-tooltip>
    </template>

    <v-card width="450px" max-height="600px">
      <v-card-title>
        <span> {{ $t("cart.title") }}</span>
      </v-card-title>
      <v-card-subtitle>
        <span> {{ $t("cart.subtitle") }}: {{ getCartLength }}</span>
      </v-card-subtitle>
      <v-card-text class="pa-1">
        <v-container v-if="getCartLength == 0" class="pa-1">
          <v-row justify="center" align="center">
            <span>
              {{ $t("cart.empty") }}
            </span>
          </v-row>
        </v-container>
        <v-container
          style="max-height: 446px; overflow-x: hidden; max-width: 100%"
          class="overflow-y-auto"
        >
          <v-row align="center" justify="center">
            <v-container
              v-for="(product, n) in getProducts"
              :key="n"
              class="pa-1"
            >
              <cart-row :order="product" />
              <v-divider />
            </v-container>
          </v-row>
        </v-container>
      </v-card-text>
      <v-divider />
      <v-card-actions>
        <v-btn @click="yourCart()">
          {{ $t("cart.pay") }}
        </v-btn>
        <v-spacer />
        <span class="title">
          {{ $t("cart.amount") }}: {{ getCartAmount.toFixed(2) }} zł
        </span>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>

<script>
import CartRow from "@/components/CartRow.vue";
import { createNamespacedHelpers } from "vuex";
const { mapGetters } = createNamespacedHelpers("cart");

export default {
  components: {
    CartRow,
  },
  computed: {
    ...mapGetters(["getProductsInCart", "getCartLength", "getCartAmount"]),

    getProducts() {
      return [...this.getProductsInCart].reverse();
    },
  },
  methods: {
    yourCart() {
      if (this.$route.name === "YourCart") {
        window.location.href = "/yourCart";
      } else {
        this.$router.push("/yourCart");
      }
    },
  },
};
</script>
