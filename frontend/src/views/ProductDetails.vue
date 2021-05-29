<template>
  <v-container v-if="product">
    <v-row>
      <h1>{{ product[`name_${this.$i18n.locale}`] }} {{ product.code }}</h1>
    </v-row>
    <v-row>
      <v-col xs="12" sm="6" md="9" lg="9" xl="9">
        <v-row align="center" justify="center">
          <v-card flat tile>
            <v-window
              v-model="onboarding"
              vertical
              align="center"
              justify="center"
            >
              <v-window-item
                v-for="(photo, n) in product.photos"
                :key="`card-${n}`"
              >
                <v-card height="375" width="500" flat>
                  <v-row align="center" justify="center">
                    <v-img
                      height="375"
                      max-width="500"
                      contain
                      :src="`${baseUrl}/${photo.url}`"
                    />
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        />
                      </v-row>
                    </template>
                    <img />
                  </v-row>
                </v-card>
              </v-window-item>
              <v-window-item v-if="product.photos.length === 0">
                <v-card height="375" width="500" class="pa-0" flat>
                  <v-row align="center" justify="center">
                    <v-img
                      max-height="375"
                      max-width="500"
                      contain
                      :src="require('@/assets/logo.png')"
                    />
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        />
                      </v-row>
                    </template>
                    <img />
                  </v-row>
                </v-card>
              </v-window-item>
            </v-window>

            <v-card-actions class="justify-space-between">
              <v-slide-group
                v-if="product.photos.length > 1"
                v-model="onboarding"
                class="pa-4"
                show-arrows
                mandatory
                center-active
              >
                <v-slide-item
                  v-for="(photo, n) in product.photos"
                  :key="`btn-${n}`"
                  v-slot:default="{ active, toggle }"
                >
                  <v-card class="ma-4" height="100" width="100" @click="toggle">
                    <v-img
                      :src="`${baseUrl}/${photo.url}`"
                      aspect-ratio="1"
                      :input-value="active"
                    >
                      <template v-slot:placeholder>
                        <v-row
                          class="fill-height ma-0"
                          align="center"
                          justify="center"
                        >
                          <v-progress-circular
                            indeterminate
                            color="grey lighten-5"
                          />
                        </v-row>
                      </template>
                    </v-img>
                  </v-card>
                </v-slide-item>
              </v-slide-group>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-col>
      <v-col xs="12" sm="6" md="3" lg="3" xl="3">
        <v-form ref="form" lazy-validation>
          <v-row>
            <span class="title py-2 mx-5">
              {{ $t("productDetailsPage.price") }}:
              {{ totalItemPrice().toFixed(2) }} zł
            </span>
          </v-row>
          <v-row
            v-for="(input, n) in product.text_boxes"
            :key="`text_box-${n}`"
          >
            <v-text-field
              class="mx-5"
              v-model="inputs.text_boxes[n]"
              :rules="fieldRules(input.is_required)"
              :counter="input.max_length"
              :maxlength="input.max_length"
              outlined
              dense
              clearable
            >
              <template v-if="input.is_required === true" v-slot:label>
                {{ input[`name_${$i18n.locale}`] }} *
              </template>
              <template v-else v-slot:label>
                {{ input[`name_${$i18n.locale}`] }}
              </template>
            </v-text-field>
          </v-row>
          <v-row
            v-for="(input, n) in product.combo_boxes"
            :key="`combo_box-${n}`"
          >
            <v-select
              class="mx-5"
              v-model="inputs.combo_boxes[n]"
              :items="comboboxElements(input.values)"
              chips
              :rules="fieldRules(input.is_required)"
              clearable
              outlined
              dense
              v-on:change="changeModificator($event, input.values, n)"
            >
              <template v-if="input.is_required === true" v-slot:label>
                {{ input[`name_${$i18n.locale}`] }} *
              </template>
              <template v-else v-slot:label>
                {{ input[`name_${$i18n.locale}`] }}
              </template>
            </v-select>
          </v-row>
          <v-row v-for="(input, n) in product.calendars" :key="`calendar-${n}`">
            <v-menu
              v-model="menus[n]"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
              outlined
              dense
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  class="mx-5"
                  v-model="inputs.calendars[n]"
                  :rules="fieldRules(input.is_required)"
                  readonly
                  outlined
                  dense
                  clearable
                  v-on="on"
                >
                  <template v-if="input.is_required === true" v-slot:label>
                    {{ input[`name_${$i18n.locale}`] }} *
                  </template>
                  <template v-else v-slot:label>
                    {{ input[`name_${$i18n.locale}`] }}
                  </template>
                </v-text-field>
              </template>
              <v-date-picker
                v-model="inputs.calendars[n]"
                :locale="langCode"
                :min="today"
                @input="menus[n] = false"
              />
            </v-menu>
          </v-row>
          <v-row>
            <v-menu
              v-model="whenYouNeedMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              transition="scale-transition"
              offset-y
              min-width="290px"
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  class="mx-5"
                  v-model="needDate"
                  :label="$t('productDetailsPage.whenYouNeedCake')"
                  readonly
                  clearable
                  outlined
                  dense
                  v-on="on"
                />
              </template>
              <v-date-picker
                v-model="needDate"
                :locale="langCode"
                :min="minDate"
                @input="whenYouNeedMenu = false"
              />
            </v-menu>
          </v-row>
          <v-row>
            <v-textarea
              class="mx-5"
              v-model="note"
              counter="300"
              maxlength="300"
              :label="$t('productDetailsPage.note')"
              auto-grow
              :rules="fieldRules(false)"
              outlined
              dense
            />
          </v-row>
          <v-row>
            <span class="mx-5">* {{ $t("productDetailsPage.required") }}</span>
          </v-row>
          <v-container class="ma-2">
            <v-row justify="center" align="center">
              <v-col cols="6" justify="center" align="center">
                <v-text-field
                  v-model="amount"
                  class="centered-input"
                  style="width: 110px"
                  dense
                  @change="
                    () => {
                      amount = parseInt(amount);
                      if (!amount > 0 || amount > 999) amount = 1;
                    }
                  "
                >
                  <template v-slot:prepend>
                    <v-btn
                      color="indigo darken-2"
                      dark
                      fab
                      x-small
                      elevation="4"
                      @click="
                        () => {
                          if (amount > 1) amount -= 1;
                        }
                      "
                    >
                      <v-icon> mdi-minus </v-icon>
                    </v-btn>
                  </template>
                  <template v-slot:append-outer>
                    <v-btn
                      color="indigo darken-2"
                      dark
                      fab
                      x-small
                      elevation="4"
                      @click="
                        () => {
                          if (amount < 999) amount += 1;
                        }
                      "
                    >
                      <v-icon> mdi-plus </v-icon>
                    </v-btn>
                  </template>
                </v-text-field>
              </v-col>
            </v-row>
            <v-row justify="center" align="center">
              <v-btn
                small
                color="indigo darken-2"
                dark
                rounded
                elevation="4"
                @click="addToCart"
              >
                <v-icon left> mdi-cart-outline </v-icon>
                {{ $t("productDetailsPage.addToCart") }}
              </v-btn>
            </v-row>
          </v-container>
        </v-form>
      </v-col>
    </v-row>
    <v-card>
      <v-tabs background-color="indigo darken-2" dark grow>
        <v-tab>
          {{ $t("productDetailsPage.description") }}
        </v-tab>
        <v-tab-item>
          <v-card flat>
            <v-card-text
              v-html="product[`product_description_${$i18n.locale}`]"
            >
              {{ product[`product_description_${$i18n.locale}`] }}
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
    <v-container v-if="product.related_products.length !== 0">
      <v-row>
        <h3>{{ $t("productDetailsPage.relatedProducts") }}:</h3>
      </v-row>
      <v-row>
        <v-card flat>
          <v-card-text>
            <v-slide-group show-arrows>
              <v-slide-item
                v-for="related in product.related_products"
                :key="related.id"
                class="ma-5"
              >
                <ProductCard :product="related" />
              </v-slide-item>
            </v-slide-group>
          </v-card-text>
        </v-card>
      </v-row>
    </v-container>
  </v-container>
  <v-container v-else style="height: 100%">
    <v-row justify="center" align="center" style="height: 100%">
      <v-progress-circular
        :size="170"
        :width="7"
        color="gray"
        indeterminate
        style="margin: auto"
      />
    </v-row>
  </v-container>
</template>
<style scoped>
.centered-input >>> input {
  text-align: center;
}
</style>
<script>
import ProductCard from "@/components/ProductCard.vue";
import { createNamespacedHelpers } from "vuex";
const { mapActions } = createNamespacedHelpers("cart");
export default {
  name: "ProductDetails",
  components: {
    ProductCard
  },
  data() {
    return {
      baseUrl: process.env.VUE_APP_DOMAIN,
      product: undefined,
      onboarding: 0,
      inputs: {
        text_boxes: [],
        combo_boxes: [],
        calendars: []
      },
      note: null,
      menus: [],
      amount: 1,
      needDate: null,
      whenYouNeedMenu: false,
      holidays: [],
      price_modificators: {}
    };
  },
  watch: {
    $route() {
      this.$axios
        .get(
          `${process.env.VUE_APP_DOMAIN}/backend/product/${this.$route.params.id}/`
        )
        .then(response => (this.product = response.data));
      this.inputs = {
        text_boxes: [],
        combo_boxes: [],
        calendars: []
      };
      this.note = null;
      this.menus = [];
      this.amount = 1;
      this.needDate = null;
      this.whenYouNeedMenu = false;
      this.price_modificators = {};
    }
  },
  mounted() {
    this.$axios
      .get(
        `${process.env.VUE_APP_DOMAIN}/backend/product/${this.$route.params.id}/`
      )
      .then(response => (this.product = response.data));
    this.$nextTick(function() {
      window.addEventListener("keyup", this.arrowController);
      const year = new Date().getFullYear();
      const easter = () => {
        const Y = new Date().getFullYear();
        var C = Math.floor(Y / 100);
        var N = Y - 19 * Math.floor(Y / 19);
        var K = Math.floor((C - 17) / 25);
        var I = C - Math.floor(C / 4) - Math.floor((C - K) / 3) + 19 * N + 15;
        I = I - 30 * Math.floor(I / 30);
        I =
          I -
          Math.floor(I / 28) *
            (1 -
              Math.floor(I / 28) *
                Math.floor(29 / (I + 1)) *
                Math.floor((21 - N) / 11));
        var J = Y + Math.floor(Y / 4) + I + 2 - C + Math.floor(C / 4);
        J = J - 7 * Math.floor(J / 7);
        var L = I - J;
        var M = 3 + Math.floor((L + 40) / 44);
        var D = L + 28 - 31 * Math.floor(M / 4);
        function padout(number) {
          return number < 10 ? "0" + number : number;
        }
        return new Date(padout(Y) + "-" + padout(M) + "-" + padout(D));
      };
      function addDays(date, days) {
        const result = new Date(date);
        result.setDate(result.getDate() + days);
        return result;
      }
      this.holidays.push(year + "-01-01"); // Nowy Rok
      this.holidays.push(year + "-01-06"); // Trzech Króli
      let date = addDays(easter(), 1)
        .toJSON()
        .slice(0, 10);
      let nDate =
        date.slice(0, 4) + "-" + date.slice(5, 7) + "-" + date.slice(8, 10);
      this.holidays.push(nDate); // Wielkanoc (poniedziałek)
      this.holidays.push(year + "-05-01"); // 1 maja
      this.holidays.push(year + "-05-03"); // 3 maja
      date = addDays(easter(), 60)
        .toJSON()
        .slice(0, 10);
      nDate =
        date.slice(0, 4) + "-" + date.slice(5, 7) + "-" + date.slice(8, 10);
      this.holidays.push(nDate); // Boże Ciało
      this.holidays.push(year + "-08-15"); // Wniebowzięcie Najświętszej Marii Panny, Święto Wojska Polskiego
      this.holidays.push(year + "-11-01"); // Dzień Wszystkich Świętych
      this.holidays.push(year + "-11-11"); // Dzień Niepodległości
      this.holidays.push(year + "-12-25"); // Boże Narodzenie
      this.holidays.push(year + "-12-26"); // Boże Narodzenie
    });
  },
  beforeDestroy: function() {
    window.removeEventListener("keyup", this.arrowController);
  },
  computed: {
    today() {
      let date = new Date();
      date = date.toJSON().slice(0, 10);
      const nDate =
        date.slice(0, 4) + "-" + date.slice(5, 7) + "-" + date.slice(8, 10);
      date = nDate;
      return date;
    },
    langCode() {
      if (this.$i18n.locale === "pl") return "pl-PL";
      else if (this.$i18n.locale === "en") return "en-EN";
      else return "pl-PL";
    },
    minDate() {
      const date = new Date();
      let days = 0;
      // while (days < this.product.realization_time) {
      while (days < 3) {
        date.setDate(date.getDate() + 1);
        if (this.isWorkingDay(date)) days++;
      }
      let nDate = date.toJSON().slice(0, 10);
      nDate =
        nDate.slice(0, 4) + "-" + nDate.slice(5, 7) + "-" + nDate.slice(8, 10);
      return nDate;
    }
  },
  methods: {
    ...mapActions(["addProduct"]),
    arrowController(event) {
      if (event.which === 37) {
        // left arrow
        if (this.onboarding > 0) this.onboarding -= 1;
        else this.onboarding = this.product.photos.length - 1;
      }
      if (event.which === 39) {
        // right arrow
        if (this.onboarding < this.product.photos.length - 1)
          this.onboarding += 1;
        else this.onboarding = 0;
      }
    },
    fieldRules(required) {
      if (required) {
        return [
          value => !!value || this.$t("productDetailsPage.validation.notEmpty")
        ];
      } else return [];
    },
    comboboxElements(elements) {
      return elements.map(e => {
        return (
          e[`text_${this.$i18n.locale}`] + " (+ " + e.price_factor + " zł)"
        );
      });
    },
    addToCart() {
      if (this.$refs.form.validate()) {
        var uuid = require("uuid");
        const userData = {
          order_id: uuid.v4(),
          product_id: this.$route.params.id,
          amount: this.amount,
          personalization: {},
          price: this.totalItemPrice()
        };

        this.inputs.text_boxes.forEach((element, i) => {
          if (element)
            userData.personalization[
              this.product.text_boxes[i][`name_${this.$i18n.locale}`]
            ] = element;
        });

        this.inputs.combo_boxes.forEach((element, i) => {
          if (element)
            userData.personalization[
              this.product.combo_boxes[i][`name_${this.$i18n.locale}`]
            ] = element;
        });

        this.inputs.calendars.forEach((element, i) => {
          if (element)
            userData.personalization[
              this.product.calendars[i][`name_${this.$i18n.locale}`]
            ] = element;
        });

        userData.personalization.needDate = this.needDate;
        userData.personalization.note = this.note;
        this.addProduct(userData);
      }
    },
    isWorkingDay(date) {
      const dayOfWeek = date.getDay();
      let nDate = date.toJSON().slice(0, 10);
      nDate =
        nDate.slice(0, 4) + "-" + nDate.slice(5, 7) + "-" + nDate.slice(8, 10);
      if (dayOfWeek === 5 || dayOfWeek === 6) return false; // Weekend
      if (this.holidays.includes(nDate)) return false; // Holidays
      return true;
    },
    changeModificator(a, b, n) {
      let val;
      if (a) {
        val = b.find(e => {
          return e.text_pl === a.split(" (")[0];
        }).price_factor;
      } else {
        val = 0;
      }
      this.price_modificators[this.product.combo_boxes[n].id] = val;
    },
    totalItemPrice() {
      const modificators = this.price_modificators;
      const modificatorNames = Object.keys(modificators);
      const sum = modificatorNames.reduce(function(accumulator, name) {
        return accumulator + parseFloat(modificators[name]);
      }, this.product.price);
      return sum;
    }
  }
};
</script>
