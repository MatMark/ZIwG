<template>
  <v-card>
    <v-card-title>
      {{ $t("yourCartPage.stepper.cart") }}
    </v-card-title>
    <v-container>
      <v-divider />
      <v-row class="subtitle-2">
        <v-col xs="2" sm="2" md="6" lg="6" xl="6">
          {{ $t("yourCartPage.table.product") }}
        </v-col>
        <v-col xs="10" sm="10" md="6" lg="6" xl="6">
          <v-row style="margin: 0">
            <!-- <v-col class="pa-0">
              {{ $t("yourCartPage.table.realizationTime") }}
            </v-col> -->
            <v-col class="py-0 hidden-sm-and-down">
              {{ $t("yourCartPage.table.quantity") }}
            </v-col>
            <v-col class="py-0 hidden-sm-and-down">
              {{ $t("yourCartPage.table.price") }}
            </v-col>
            <v-col class="pa-0">
              {{ $t("yourCartPage.table.totalPrice") }}
            </v-col>
            <v-col class="pa-0">
              {{ $t("yourCartPage.table.actions") }}
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-divider />
      <div v-for="(product, n) in getProducts" :key="n" class="pa-0">
        <CartItem :order="product" />
        <v-divider />
      </div>
      <v-row>
        <v-col>
          <v-card flat>
            <v-card-title class="subtitle-2 py-0">
              {{ $t("yourCartPage.delivery") }}:
            </v-card-title>
            <v-card-text>
              <v-radio-group
                v-model="selectedDelivery"
                column
                @change="changeShipment(selectedDelivery)"
              >
                <v-radio
                  v-for="(delivery, n) in deliveries"
                  :key="n"
                  :label="
                    $t(`yourCartPage.deliveryForm.${delivery.name}`) +
                      ` - ${delivery.price.toFixed(2)} zł`
                  "
                  color="primary"
                  :value="delivery.name"
                />
              </v-radio-group>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card flat>
            <v-card-title class="subtitle-2 py-0">
              {{ $t("yourCartPage.payment") }}:
            </v-card-title>
            <v-card-text>
              <v-radio-group
                v-model="payment"
                column
                @change="changePayment(payment)"
              >
                <v-radio
                  :label="`${$t('yourCartPage.paymentForm.transfer')}`"
                  color="primary"
                  value="transfer"
                />
                <v-radio
                  :label="`${$t('yourCartPage.paymentForm.payu')}`"
                  color="primary"
                  value="payu"
                />
                <v-radio
                  :label="`${$t('yourCartPage.paymentForm.blik')}`"
                  color="primary"
                  value="blik"
                />
                <v-radio
                  :label="`${$t('yourCartPage.paymentForm.credit_card')}`"
                  color="primary"
                  value="credit_card"
                />
              </v-radio-group>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col>
          <v-card flat style="text-align: end">
            <span
              >{{ $t("yourCartPage.totalValue") }}:
              {{ getCartAmount.toFixed(2) }} zł</span
            >
            <br />
            <span
              >{{ $t("yourCartPage.deliveryCost") }}:
              {{ deliveryCost.toFixed(2) }} zł</span
            >
            <br />
            <span class="title"
              >{{ $t("yourCartPage.toPay") }}:
              {{ (getCartAmount + deliveryCost).toFixed(2) }} zł</span
            >
          </v-card>
        </v-col>
      </v-row>
    </v-container>
    <v-card-actions>
      <v-btn tile to="/home">
        {{ $t("yourCartPage.continueShopping") }}
      </v-btn>
      <v-spacer />
      <v-btn
        tile
        :disabled="getProducts.length === 0 || !selectedDelivery || !payment"
        @click="openDialog"
      >
        {{ $t("yourCartPage.buy") }}
      </v-btn>
      <v-dialog v-model="dialog" max-width="600px">
        <v-card>
          <v-card-title>
            <span class="headline">{{
              $t("yourCartPage.noRegisterModal.title")
            }}</span>
          </v-card-title>
          <v-card-text>
            {{ $t("yourCartPage.noRegisterModal.details") }}
          </v-card-text>
          <v-card-actions>
            <v-btn tile @click="dialog = false">
              {{ $t("yourCartPage.stepper.back") }}
            </v-btn>
            <v-spacer />
            <v-btn tile @click="order">
              {{ $t("yourCartPage.noRegisterModal.submit") }}
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card-actions>
  </v-card>
</template>

<script>
import CartItem from "@/components/Cart/CartItem.vue";
import { createNamespacedHelpers } from "vuex";
const { mapGetters, mapActions } = createNamespacedHelpers("cart");

export default {
  components: {
    CartItem
  },
  data() {
    return {
      selectedDelivery: undefined,
      payment: undefined,
      dialog: false,
      deliveries: [
        {
          name: "courier",
          price: 10
        },
        {
          name: "personal_pickup",
          price: 0
        }
      ]
    };
  },
  computed: {
    ...mapGetters([
      "getProductsInCart",
      "getCartAmount",
      "getShipment",
      "getPayment"
    ]),

    deliveryCost() {
      if (!this.selectedDelivery || !this.deliveries) return 0;
      else
        return this.deliveries.find(
          delivery => delivery.name === this.selectedDelivery
        ).price;
    },

    getProducts() {
      return [...this.getProductsInCart].reverse();
    }
  },
  watch: {
    getProducts() {
      if (this.getProducts.length === 0) {
        this.changeShipment(undefined);
        this.selectedDelivery = undefined;
        this.changePayment(undefined);
        this.payment = undefined;
      }
    }
  },
  mounted() {
    this.payment = this.getPayment;
    this.selectedDelivery = this.getShipment;
  },
  methods: {
    ...mapActions(["changeShipment", "changePayment"]),

    openDialog() {
      const tags = this.getProducts.map(item => {
        return item.tag_id;
      });
      const properlyOrder = tags.some(item => {
        return item !== 2;
      });
      if (properlyOrder) {
        this.dialog = true;
      } else {
        this.vignettes_dialog = true;
      }
    },

    order() {
      window.scrollTo({ top: 0 });
      this.dialog = false;
      this.$emit("nextStep");
    }
  }
};
</script>
