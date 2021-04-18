<template>
  <v-container v-if="product">
    <v-row>
      <h1>{{ product[`name_${this.$i18n.locale}`] }} {{ product.code }}</h1>
    </v-row>
    <v-row>
      <v-col cols="6">
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
      <v-col cols="2" />
      <v-col cols="4">
        <v-form ref="form" lazy-validation>
          <v-row>
            <span class="title py-2">
              {{ $t("productDetailsPage.price") }}:
              {{ product.price.toFixed(2) }} zł
            </span>
          </v-row>
          <!--:counter="input.Max_length"
              :maxlength="input.Max_length" -->
          <v-row
            v-for="(input, n) in product.text_boxes"
            :key="`text_box-${n}`"
          >
            <v-text-field
              class="mr-5"
              v-model="inputs.text_boxes[n]"
              :rules="fieldRules(input.is_required)"
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
              class="mr-5"
              v-model="inputs.combo_boxes[n]"
              :items="comboboxElements(input.values)"
              chips
              :rules="fieldRules(input.is_required)"
              clearable
              outlined
              dense
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
                  class="mr-5"
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
            <span>* {{ $t("productDetailsPage.required") }}</span>
          </v-row>
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

<script>
import ProductCard from "@/components/ProductCard.vue";
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
      menus: []
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
      this.menus = [];
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
    }
  },
  methods: {
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
        return e[`text_${this.$i18n.locale}`];
      });
    }
  }
};
</script>
