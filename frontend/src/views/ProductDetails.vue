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
            <!-- v-for="n in product.photos.length" -->
              <v-window-item
                v-for="n in product.photos"
                :key="`card-${n}`"
              >
                <v-card height="375" width="500" class="pa-0" flat>
                  <v-row align="center" justify="center">
                    <v-img
                      max-height="375"
                      max-width="500"
                      contain
                      :src="product.photos[n - 1].url"
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
              <!-- <v-window-item v-if="product.photos.length === 0"> -->
              <v-window-item v-if="!product.photos">
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
              <!-- v-if="product.photos.length > 1" -->
              <v-slide-group
                v-if="product.photos"
                v-model="onboarding"
                class="pa-4"
                show-arrows
                mandatory
                center-active
              >
                <v-slide-item
                  v-for="n in product.photos.length"
                  :key="`btn-${n}`"
                  v-slot:default="{ active, toggle }"
                >
                  <v-card class="ma-4" height="100" width="100" @click="toggle">
                    <v-img
                      :src="gqlurl + product.photos[n - 1].url"
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
        <v-row>
          <span class="title py-2">
            {{ $t("productDetailsPage.price") }}:
            {{ product.price.toFixed(2) }} zł
          </span>
        </v-row>
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
              v-html="product[`product_description_${this.$i18n.locale}`]"
            >
              {{ product[`product_description_${this.$i18n.locale}`] }}
            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>
    <!-- <v-container v-if="product.related_products.length !== 0">
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
                <product-card :id="related.id" />
              </v-slide-item>
            </v-slide-group>
          </v-card-text>
        </v-card>
      </v-row>
    </v-container> -->
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
export default {
  name: "ProductDetails",
  components: {},
  data() {
    return {
      product: undefined,
      onboarding: 0
    };
  },
  mounted() {
    this.$axios
      // .get(`${window.location.origin}/backend/product/${this.$route.params.id}/`)
      .get(`http://127.0.0.1:8000/backend/product/${this.$route.params.id}/`)
      .then(response => (this.product = response.data));
  }
};
</script>
