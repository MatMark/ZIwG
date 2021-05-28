<template>
  <v-container>
    <v-row class="text-center">
      <v-col>
        <v-stepper v-model="currentStep">
          <v-stepper-header style="-webkit-box-shadow: none;box-shadow: none;">
            <v-stepper-step
              step="1"
              class="py-0"
              :editable="editable(1)"
              style="background: none;"
              @click.native="setStep(1)"
            >
              {{ $t("yourCartPage.stepper.cart") }}
            </v-stepper-step>

            <v-divider />

            <v-stepper-step
              step="2"
              class="py-0"
              :editable="editable(2)"
              style="background: none;"
              @click.native="setStep(2)"
            >
              {{ $t("yourCartPage.stepper.yourData") }}
            </v-stepper-step>

            <v-divider />

            <v-stepper-step
              step="3"
              class="py-0"
              :editable="editable(3)"
              style="background: none;"
              @click.native="setStep(3)"
            >
              {{ $t("yourCartPage.stepper.summary") }}
            </v-stepper-step>
            <v-divider />

            <v-stepper-step
              step="4"
              class="py-0"
              :editable="editable(4)"
              style="background: none;"
              @click.native="setStep(4)"
            >
              {{ $t("yourCartPage.stepper.confirmation") }}
            </v-stepper-step>
          </v-stepper-header>
          <v-stepper-content step="1" class="pt-0">
            <Cart @nextStep="nextStep" />
          </v-stepper-content>
          <v-stepper-content step="2" class="pt-0">
            <YourData @previousStep="previousStep" @nextStep="nextStep" />
          </v-stepper-content>
          <v-stepper-content step="3" class="pt-0">
            <Summary @previousStep="previousStep" @nextStep="nextStep" />
          </v-stepper-content>
          <v-stepper-content step="4" class="pt-0">
            <Confirmation @previousStep="previousStep" @nextStep="nextStep" />
          </v-stepper-content>
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Cart from "@/components/Cart/Cart.vue";
import YourData from "@/components/Cart/YourData.vue";
import Summary from "@/components/Cart/Summary.vue";
import Confirmation from "@/components/Cart/Confirmation.vue";
import { createNamespacedHelpers } from "vuex";
const { mapActions, mapGetters } = createNamespacedHelpers("cart");

export default {
  components: {
    Cart,
    YourData,
    Summary,
    Confirmation
  },
  data() {
    return {
      currentStep: 1
    };
  },
  computed: {
    ...mapGetters([
      "getProductsInCart",
      "getCartLength",
      "getCartAmount",
      "getOrderInfo"
    ])
  },
  mounted() {
    const d = new Date(this.getOrderInfo.updated);
    d.setHours(d.getHours() + 1);
    if (new Date() > d) {
      this.clearOrderInfo();
    }
  },
  methods: {
    ...mapActions(["clearOrderInfo"]),

    nextStep() {
      if (this.currentStep < 4) {
        this.currentStep++;
        this.$router.push({
          path: "yourCart",
          query: { step: this.currentStep }
        });
      }
    },
    previousStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
        this.$router.push({
          path: "yourCart",
          query: { step: this.currentStep }
        });
      }
    },
    editable(step) {
      if (step < this.currentStep) return true;
      else return false;
    },
    setStep() {
      this.$router.push({
        path: "yourCart",
        query: { step: this.currentStep }
      });
    }
  }
};
</script>
