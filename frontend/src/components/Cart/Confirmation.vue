<template>
  <v-card>
    <v-card-title>
      {{ $t("yourCartPage.stepper.confirmation") }}
    </v-card-title>
    <v-container>
      <v-divider />
    </v-container>
    <v-card-actions>
      <v-btn tile @click="previousStep">
        {{ $t("yourCartPage.stepper.back") }}
      </v-btn>
      <v-spacer />
      <v-btn tile @click="nextStep">
        {{ $t("yourCartPage.stepper.continue") }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("cart");
export default {
  components: {},
  data() {
    return {};
  },
  computed: {},
  mounted() {},
  methods: {
    ...mapActions(["clearCart"]),
    nextStep() {
      this.clearCart();
      window.scrollTo({ top: 0 });
      this.$router.push("/home");
      // this.$emit('nextStep')
    },
    previousStep() {
      window.scrollTo({ top: 0 });
      this.$emit("previousStep");
    }
  }
};
</script>
