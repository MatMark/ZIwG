<template>
  <v-row v-if="product" class="body-2" style="margin: 0">
    <v-col cols="6" class="py-0">
      <v-row class="text-left" style="margin: 0">
        <v-col cols="2" style="margin-top: auto; margin-bottom: auto">
          <router-link :to="`/product_details/${product.id}`">
            <v-avatar>
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
            </v-avatar>
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
            X
            <!-- {{ product.Realization_time }} -->
            {{ $t("yourCartPage.table.days") }}</span
          >
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span>{{ getByOrderId.amount }}</span>
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span>{{ product.price.toFixed(2) }} zł</span>
        </v-col>
        <v-col class="pa-0" style="margin-top: auto; margin-bottom: auto">
          <span>{{ (getByOrderId.amount * product.price).toFixed(2) }} zł</span>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<script>
import { createNamespacedHelpers } from "vuex";
const { mapGetters } = createNamespacedHelpers("cart");

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
  },
  methods: {
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
    }
  }
};
</script>
