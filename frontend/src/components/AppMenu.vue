<template>
  <v-app-bar app color="deep-purple darken-5" dark>
    <template v-slot:img="{ props }">
      <v-img
        v-bind="props"
        gradient="to top right, rgba(0,0,63,.7), rgba(0,63,255,.7)"
      />
    </template>
    <router-link to="/home">
      <div class="d-flex align-center">
        <v-img
          alt="Cookie Logo"
          class="shrink mr-2"
          contain
          :src="require('@/assets/cookie.png')"
          transition="scale-transition"
          width="40"
        />
        <h1
          class="hidden-sm-and-down"
          style='font-family: "Roboto", sans-serif; color: white; text-decoration: underline'
        >
          Cukiernia W4
        </h1>
      </div>
    </router-link>

    <v-row align="center" justify="center">
      <v-btn-toggle tile group>
        <v-menu
          v-model="openMenu"
          transition="slide-y-transition"
          bottom
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-btn text color="deep-purple lighten-5" v-on="on">
              {{ $t("appMenu.menu") }}
              <v-icon right> mdi-chevron-down </v-icon>
            </v-btn>
          </template>

          <v-list>
            <v-list-item-group>
              <v-list-item dense :to="'/all_products'">
                <v-list-item-title>
                  {{ $t("appMenu.allProducts") }}
                </v-list-item-title>
              </v-list-item>
              <v-menu
                v-for="(category, index) in categories"
                :key="index"
                open-on-hover
                transition="slide-x-transition"
                right
                bottom
                offset-x
              >
                <template v-slot:activator="{ on }">
                  <v-list-item dense :to="`/products/${category.id}`" v-on="on">
                    <v-list-item-title>
                      {{
                        capitalizeFirstLetter(
                          category[`name_${$i18n.locale.toLocaleLowerCase()}`]
                        )
                      }}
                    </v-list-item-title>
                  </v-list-item>
                </template>
              </v-menu>
            </v-list-item-group>
          </v-list>
        </v-menu>

        <v-btn
          class="hidden-sm-and-down"
          :to="`/faq`"
          text
          color="deep-purple lighten-5"
        >
          {{ $t("appMenu.faq") }}
        </v-btn>

        <v-btn
          class="hidden-sm-and-down"
          :to="`/contact`"
          text
          color="deep-purple lighten-5"
        >
          {{ $t("appMenu.contact") }}
        </v-btn>
      </v-btn-toggle>
    </v-row>
    <div>
      <v-toolbar color="transparent" flat>
        <LanguageSwitcher />
        <CartButton />
      </v-toolbar>
    </div>
  </v-app-bar>
</template>

<script>
import LanguageSwitcher from "@/components/LanguageSwitcher.vue";
import CartButton from "@/components/CartButton.vue";

export default {
  components: {
    LanguageSwitcher,
    CartButton
  },
  data() {
    return {
      baseUrl: process.env.VUE_APP_DOMAIN,
      openMenu: false,
      categories: undefined
    };
  },
  mounted() {
    this.$axios
      .get(`${process.env.VUE_APP_DOMAIN}/backend/categories/`)
      .then(response => (this.categories = response.data));
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    }
  }
};
</script>
