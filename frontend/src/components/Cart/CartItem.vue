<template>
  <v-row v-if="product" class="body-2" style="margin: 0">
    <v-col cols="6" class="py-0">
      <v-row class="text-left" style="margin: 0">
        <v-col cols="2" style="margin-top: auto; margin-bottom: auto">
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
              :src="require('@/assets/logo.png')"
              contain
              width="50"
              height="50"
              :alt="`/product_details/${product.id}`"
            />
          </router-link>
        </v-col>
        <v-col style="margin-top: auto; margin-bottom: auto">
          <v-row style="height: 100%; margin: 0">
            <router-link
              :to="`/product_details/${product.id}`"
              style="text-decoration: none; color: black"
            >
              <div>
                <span class="subtitle-2"
                  >{{ product.code }} -
                  {{ product[`name_${this.$i18n.locale}`] }}</span
                >
                <br />
                <div
                  v-for="item in personalizationFields(
                    getByOrderId.personalization
                  )"
                  :key="item.id"
                  class="pa0 ma0 caption"
                >
                  {{ item }}
                </div>
              </div>
            </router-link>
          </v-row>
        </v-col>
      </v-row>
    </v-col>
    <v-col cols="6">
      <v-row style="height: 100%; margin: 0">
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span>
            <!-- {{ product.Realization_time }} -->
            X {{ $t("yourCartPage.table.days") }}</span
          >
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <v-text-field
            v-model="inputValue"
            class="centered-input"
            style="width: 100px; align: center; margin: auto"
            hide-details
            dense
            append-outer-icon="mdi-plus-box"
            prepend-icon="mdi-minus-box"
            @click:prepend="decreaseAmount"
            @click:append-outer="increaseAmount"
            @change="editAmount"
          />
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span>{{ getByOrderId.price.toFixed(2) }} zł</span>
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span
            >{{
              (getByOrderId.amount * getByOrderId.price).toFixed(2)
            }}
            zł</span
          >
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <v-btn icon @click="removeProduct(order.order_id)">
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-icon v-bind="attrs" v-on="on"> mdi-delete </v-icon>
              </template>
              <span>{{ $t("yourCartPage.table.delete") }}</span>
            </v-tooltip>
          </v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
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
      product: null,
      inputValue: 0
    };
  },
  computed: {
    ...mapGetters(["getProductByOrderId"]),

    getByOrderId: {
      get: function() {
        return this.getProductByOrderId(this.order.order_id);
      }
    }
  },
  mounted() {
    this.$axios
      .get(
        `${process.env.VUE_APP_DOMAIN}/backend/product/${this.order.product_id}/`
      )
      .then(response => (this.product = response.data));
    this.inputValue = this.getByOrderId.amount;
  },
  methods: {
    ...mapActions(["removeProduct", "editProduct"]),

    personalizationFields(fields) {
      const textArray = [];
      const context = this;
      const exceptions = [
        "needDate",
        "note",
        "selectedLabel",
        "labelText",
        "labelDate"
      ];
      Object.keys(fields).forEach(function(k) {
        if (fields[k] !== null) {
          if (exceptions.includes(k)) {
            textArray.push(
              context.$i18n.t(`yourCartPage.personalization.${k}`) +
                ": " +
                fields[k]
            );
          } else {
            textArray.push(k + ": " + fields[k]);
          }
        }
      });
      return textArray;
    },
    increaseAmount() {
      if (this.inputValue < 999) {
        this.inputValue += 1;
        this.order.amount += 1;
      }
      this.editProduct(this.order);
    },
    decreaseAmount() {
      if (this.inputValue > 1) {
        this.inputValue -= 1;
        this.order.amount -= 1;
      }
      this.editProduct(this.order);
    },
    editAmount() {
      this.inputValue = parseInt(this.inputValue);
      if (this.inputValue > 0 && this.inputValue < 1000) {
        this.order.amount = this.inputValue;
      } else {
        this.inputValue = 1;
        this.order.amount = 1;
      }
      this.editProduct(this.order);
    }
  }
};
</script>
