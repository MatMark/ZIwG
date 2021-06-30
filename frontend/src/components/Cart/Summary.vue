<template>
  <v-card>
    <v-card-title>
      {{ $t("yourCartPage.stepper.summary") }}
    </v-card-title>
    <v-divider />
    <v-row class="subtitle-2">
      <v-col cols="6">
        {{ $t("yourCartPage.table.product") }}
      </v-col>
      <v-col cols="6">
        <v-row style="margin: 0">
          <v-col class="pa-0">
            {{ $t("yourCartPage.table.realizationTime") }}
          </v-col>
          <v-col class="pa-0">
            {{ $t("yourCartPage.table.quantity") }}
          </v-col>
          <v-col class="pa-0">
            {{ $t("yourCartPage.table.price") }}
          </v-col>
          <v-col class="pa-0">
            {{ $t("yourCartPage.table.totalPrice") }}
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-divider />
    <div v-for="(product, n) in getProducts" :key="n" class="pa-0">
      <CartItemSummary :order="product" />
      <v-divider />
    </div>
    <v-container v-if="getCustomerData">
      <v-row style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.orderNumber") }}:</span>
        </v-col>
        <v-col>
          <span> XXX XXX XXX </span>
        </v-col>
      </v-row>
      <v-row style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.shipmentMethod") }}:</span>
        </v-col>
        <v-col>
          <span>
            {{ $t(`yourCartPage.deliveryForm.${getShipment}`) }}
          </span>
        </v-col>
      </v-row>
      <v-row style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.toPay") }}:</span>
        </v-col>
        <v-col>
          <span> {{ (getCartAmount + deliveryCost).toFixed(2) }} zł </span>
        </v-col>
      </v-row>
      <v-row style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.paymentMethod") }}:</span>
        </v-col>
        <v-col>
          <span>
            {{ paymentMethod }}
          </span>
        </v-col>
      </v-row>
      <v-row style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.invoiceAddress") }}:</span>
        </v-col>
        <v-col>
          <span>
            {{ getCustomerData.yourData.firstName }}
            {{ getCustomerData.yourData.lastName }},
            {{ getCustomerData.address.city }},
            {{ getCustomerData.address.country }}
          </span>
        </v-col>
      </v-row>
      <v-row
        v-if="getCustomerData.address.otherSendAddress"
        style="text-align: left"
      >
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.sendingAddress") }}:</span>
        </v-col>
        <v-col>
          <span>
            {{ getCustomerData.sendAddress.firstName }}
            {{ getCustomerData.sendAddress.lastName }},
            {{ getCustomerData.sendAddress.street }},
            {{ getCustomerData.sendAddress.city }}
            {{ getCustomerData.sendAddress.postCode }},
            {{ getCustomerData.sendAddress.country }}
          </span>
        </v-col>
      </v-row>
      <v-row v-else style="text-align: left">
        <v-col cols="2" style="max-width: 13%">
          <span>{{ $t("yourCartPage.summary.sendingAddress") }}:</span>
        </v-col>
        <v-col>
          <span>
            {{ getCustomerData.yourData.firstName }}
            {{ getCustomerData.yourData.lastName }},
            {{ getCustomerData.address.street }},
            {{ getCustomerData.address.city }}
            {{ getCustomerData.address.postCode }},
            {{ getCustomerData.address.country }}
          </span>
        </v-col>
      </v-row>
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
import CartItemSummary from "@/components/Cart/CartItemSummary.vue";
import { createNamespacedHelpers } from "vuex";
const { mapGetters } = createNamespacedHelpers("cart");
export default {
  components: { CartItemSummary },
  data() {
    return {
      selectedDelivery: undefined,
      payment: undefined,
      realizationTime: undefined
    };
  },
  computed: {
    ...mapGetters([
      "getProductsInCart",
      "getProductsIdsInCart",
      "getCartAmount",
      "getCustomerData",
      "getShipment",
      "getPayment"
    ]),

    getProducts() {
      return [...this.getProductsInCart].reverse();
    },
    deliveryCost() {
      if (!this.selectedDelivery || !this.deliveries) return 0;
      else
        return this.deliveries.find(
          delivery => delivery.name === this.selectedDelivery
        ).price;
    },
    paymentMethod() {
      const payments = ["transfer", "payu", "blik", "credit_card"];
      if (payments.includes(this.getPayment)) {
        return this.$t(`yourCartPage.paymentForm.${this.getPayment}`);
      }
      return null;
    }
  },
  mounted() {
    this.payment = this.getPayment;
    this.selectedDelivery = this.getShipment;
  },
  methods: {
    nextStep() {
      window.scrollTo({ top: 0 });
      this.$emit("nextStep");
    },
    previousStep() {
      window.scrollTo({ top: 0 });
      this.$emit("previousStep");
    }
  }
};
</script>
